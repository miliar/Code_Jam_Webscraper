#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;


int readtime()
{
	int H,M;
	char ch;
	cin>>H>>ch>>M;
	return H*60+M;
}

int main()
{
	
	vector<pair<int,pair<int,int> > > v;
	int was[201]={0};
	int N,t,NA,NB,i,T,j;
	cin>>N;
	for(t=1;t<=N;t++)
	{
		int ansA=0,ansB=0,beg,en;
		cin>>T;
		cin>>NA>>NB;
		for(i=0;i<NA+NB;i++)was[i]=0;
		v.clear();
		for(i=0;i<NA;i++)
		{
			beg=readtime();
			en=readtime()+T;
			v.push_back(make_pair(beg,make_pair(en,0)));
		}
		for(i=0;i<NB;i++)
		{
			beg=readtime();
			en=readtime()+T;
			v.push_back(make_pair(beg,make_pair(en,1)));
		}
		sort(v.begin(),v.end());
		int d=0;
		while(d!=NA+NB)
		{
			for(i=0;i<v.size();i++)if(was[i]==0)break;
			if(v[i].second.second==0)ansA++;
			else ansB++;
			d++;
			was[i]=1;
			for(j=i+1;j<v.size();j++)
			{
				if((was[j]==0)&&(v[i].second.first<=v[j].first)&&(v[i].second.second!=v[j].second.second))
				{
					was[j]=1;
					d++;
					i=j;
				}
			}
		}
		cout<<"Case #"<<t<<": "<<ansA<<" "<<ansB<<endl;
	}
	return 0;
}