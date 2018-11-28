#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#pragma comment(linker,"/STACK:268435456")

struct match
{
	vector<int> teams;
	int num;
};

struct miss
{
	int team;
	int mx;
};

bool operator < ( miss a, miss b )
{
	return a.mx < b.mx;
}


miss Miss[10000];
match Matches[10000];
vector<int> Plays[10000];
int misses[10000];
bool plays[2500][10000];


int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);

	int i,j,l,k,n,t,tt,p,tnum, mnum,w,f;
	int ans;
	cin>>t;
	int zibil;
	int teams;
	for(l=1;l<=t;++l)
	{
		cin>>p;
		teams = (int)pow(2.0, p);
		ans = 0;
		for(i=0;i<teams;++i)
		{
			cin>>Miss[i].mx;
			Miss[i].team = i;
			Plays[i].clear();
			misses[i] = p;
			for(j=0;j<teams;++j)
				plays[i][j] = false;
			Matches[i].teams.clear();
		}

		for(i=1;i<teams;++i)
			cin>>zibil;

		sort(Miss, Miss+teams);

		for(i=0;i<teams;i+=2)
		{
			Matches[i/2].teams.push_back(i);
			Matches[i/2].teams.push_back(i+1);
			Matches[i/2].num = i/2;
			Plays[i].push_back(i/2);
			Plays[i+1].push_back(i/2);
		}
		i = 0;
		j = teams/2;
		while(i+1<j)
		{
			Matches[j].num = Matches[j-1].num + 1;
			k = Matches[i].teams.size();
			for(tt=0;tt<k;++tt)
			{
				Matches[j].teams.push_back(Matches[i].teams[tt]);
				Plays[ Matches[i].teams[tt] ].push_back(Matches[j].num);
			}
			
			for(tt=0;tt<k;++tt)
			{
				Matches[j].teams.push_back(Matches[i+1].teams[tt]);
				Plays[ Matches[i+1].teams[tt] ].push_back(Matches[j].num);
			}
			i+=2;
			++j;
		}

		for(i=0;i<teams;++i)
		{
			tnum = Miss[i].team;
			k = Plays[tnum].size();
			j = k-1;
			while(Miss[i].mx < misses[ Miss[i].team ])
			{
				while(plays[tnum][ Plays[tnum][j] ] )
					--j;
				mnum = Plays[tnum][j];
				w = Matches[mnum].teams.size();
				++ans;
				for(f=0;f<w;++f)
				{
					plays[ Matches[mnum].teams[f] ][ mnum ] = true;
					-- misses[ Matches[mnum].teams[f] ];
				}
			}
		}
		cout<<"Case #"<<l<<": "<<ans<<endl;
	}
	return 0;
}


/*

2

3
1 1 0 0 1 1 3 2
1 1 1 1 1 1 1

3
0 0 0 0 0 0 0 0
1 1 1 1 1 1 1

*/