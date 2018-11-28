#include<vector>
#include<iostream>
#include<algorithm>
#include<set>
#include<queue>
#include<cstring>
#include<string>
#include<map>
#include<fstream>
using namespace std;

#define FOR(i,a,b) for(int (i)=(a);(i)<(b);++(i))
#define all(a) (a).begin(),(a).end()
int main()
{
	ifstream fin("C:\\A-smal.txt");
	ofstream fout("C:\\AAA.out");
	int t;
	fin>>t;
	int rr=1;
	while(rr<=t)
	{
		int N,M;
		fin>>N>>M;
		vector<string> ori;
		vector<string> req;
		if(N>0)
			ori.resize(N);
		if(M>0)
			req.resize(M);
		FOR(i,0,N)
		{
			fin>>ori[i];
		}
		FOR(i,0,M)
		{
			fin>>req[i];
		}
		set< string > s;
		int word=0;
		FOR(i,0,N)
		{
			string temp;
			int level=0;
			FOR(j,1,ori[i].size())
			{
				
				if(ori[i][j]=='/' || j==ori[i].size()-1)
				{
					if(j==ori[i].size()-1) temp+=ori[i][j];
					if(temp=="")continue;
					s.insert(temp);
					//cout<<temp<<endl;
					level++;
				}
				temp+=ori[i][j];
			}
		}
		int total=0;
		int inside=0;
		FOR(i,0,M)
		{
			string temp;
			int level=0;
			FOR(j,1,req[i].size())
			{
				if(req[i][j]=='/' || j==req[i].size()-1)
				{
					if(j==req[i].size()-1) temp+=req[i][j];
					if(s.count(temp)==0)
					{
						total++;
						//cout<<"$$ "<<temp<<endl;
						s.insert(temp);
					}
					level++;
				}
				temp+=req[i][j];
			}
		}
		/*cout<<endl;
		cout<<"S"<<endl;
		for(set< pair<string,int> >:: iterator it=s.begin();it!=s.end();it++)
		{
			cout<<(*it).first<<" "<<(*it).second<<endl;
		}*/
		fout<<"Case #"<<rr<<": "<<total<<endl;
		rr++;
	}
}