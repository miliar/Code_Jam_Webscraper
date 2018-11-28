#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <algorithm>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<int(b);++i)
#define SZ(v) ((int)v.size())
#define FORSZ(i,a,v) FOR(i,a,SZ(v))
#define REPSZ(i,v) FORSZ(i,0,v)
#define ALL(v) (v).begin(),(v).end()
#define SS stringstream
#define VI vector<int>
#define VS vector<string>
#define PB push_back

bool used[101];

int main()
{
freopen ("A-large.in","r",stdin);
freopen ("out.txt","w",stdout);
	int N,Q,S;
	cin>>N;
	FOR(i,0,N)
	{
		cin>>S;
		cin.ignore();
		int len=S;
		int ans=0;
		VS eng;
		eng.clear();
		string str;
		memset(used,false,sizeof(used));
		FOR(j,0,S)
		{	
			getline(cin,str);
			eng.PB(str);
		}
		cin>>Q;
		cin.ignore();
		FOR(j,0,Q)
		{
			getline(cin,str);
			VS::iterator it=find(ALL(eng),str);
			int k=it-eng.begin();
			if(!used[k])
			{
				if(len==1)
				{
					ans++;
					memset(used,false,sizeof(used));
					len=S;
				}
				len--;
				used[k]=true;

			}
			

		}
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	
	}

	return 0;
}

