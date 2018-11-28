#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<set>
#include<fstream>
#include<queue>
#include<fstream>
#include<map>

using namespace std;


int main()
{
	//ifstream cin("B-small-attempt0.in");
	//ofstream cout("B-small.out");
	ifstream cin("B-large.in");
	ofstream cout("B-large.out");


	int T;
	cin>>T;
	for(int j=0;j<T;j++)
	{
		map< pair<char,char>, char> comb;
		map<pair<int,int> ,bool> opp;
		int C;
		cin>>C;
		for(int k=0;k<C;k++)
		{
			char a,b,c;
			cin>>a>>b>>c;
			comb[make_pair(a,b)]=c;
			comb[make_pair(b,a)]=c;
		}

		int D;
		cin>>D;
		for(int k=0;k<D;k++)
		{
			char a,b;
			cin>>a>>b;
			opp[make_pair(a,b)]=true;
			opp[make_pair(b,a)]=true;

		}

		int N;
		cin>>N;
		string series;
		
		for(int i=0;i<N;i++)
		{
			char a;
			cin>>a;
			series+=a;
			if(series.size()>1)
			{
				map< pair<char,char>, char>::iterator it=comb.find(make_pair(a,series[series.size()-2]));
				if(it!=comb.end())
				{
					string x;
					x+=(*it).second;
					series.replace(series.size()-2,2,x);
				}
				else
				{
					for(int q=0;q<series.size()-1;q++)
					{
						map<pair<int,int> ,bool> ::iterator it=opp.find(make_pair(a,series[q]));
						if(it!=opp.end())
						{
							series.clear();
							break;
						}
					}
				}

			}
		}


		cout<<"Case #"<<(j+1)<<": [";
		for(int p=0;p<series.size();p++)
		{
			if(p!=series.size()-1)
				cout<<series[p]<<", ";
			else cout<<series[p];
		}
		cout<<"]\n";



	}

	//system("pause");
	return 0;
}