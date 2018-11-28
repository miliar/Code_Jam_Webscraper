#pragma comment(linker,"/STACK:64000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <cmath>
#include <map>
#include <set>
#include <ctime>
#include <algorithm>
#include <memory.h>

using namespace std;

#define WR printf
#define RE scanf
#define PB push_back
#define SE second
#define FI first

#define FOR(i,k,n) for(int i=(k); i<=(n); i++)
#define DFOR(i,k,n) for(int i=(k); i>=(n); i--)
#define SZ(a) (int)((a).size())
#define FA(i,v) FOR(i,0,SZ(v)-1)
#define RFA(i,v) DFOR(i,SZ(v)-1,0)
#define CLR(a) memset(a, 0, sizeof(a))

#define LL long long
#define VI  vector<int>
#define PAR pair<int ,int>
#define o_O 1000000000 
void __never(int a){printf("\nOPS %d", a);}
#define ass(s) {if (!(s)) {__never(__LINE__);cout.flush();cerr.flush();abort();}}

int n, m;
int be[10], en[10];
int color[10];
bool used[10];

bool has(VI & v, int i)
{
	FA(a,v) if (v[a]==i) return true;
	return false;
}

void sol()
{
	set< VI > Set;
	VI v;
	FOR(a,0,n-1) v.push_back(a);
	Set.insert(v);

	FOR(a,1,m)
	{
		set< VI >::iterator it;
		for (it = Set.begin(); it != Set.end(); it++)
			if (has((*it), be[a]) && has((*it), en[a]))
			{
				VI vec = *it;
				Set.erase(it);
				VI v1, v2;
				bool flag=false;
				FA(b,vec)
					if (vec[b]==be[a] || vec[b]==en[a])
					{
						flag=!flag;
						v1.push_back(vec[b]);
						v2.push_back(vec[b]);
					}
					else if (flag) v1.push_back(vec[b]);
					else v2.push_back(vec[b]);
				Set.insert(v1);
				Set.insert(v2);
				break;
			}
	}

	/*set< VI >::iterator it;
	for (it = Set.begin(); it != Set.end(); it++)
	{
		FA(a,*it) cout << (*it)[a] << " ";
		cout << "\n";
	}*/

	VI ans;
	int max_used=0;
	FOR(a,0,(1<<(3*n))-1)
	{
		CLR(used);
		FOR(b,0,n-1)
		{
			color[b] = ((a>>(3*b))&7);
			used[(a>>(3*b))&7]=true;
		}
		bool flag1=true;
		FOR(b,1,7) if (used[b] && !used[b-1]) flag1=false;
		if (!flag1) continue;
		int colors=0;
		FOR(b,0,7) if (used[b]) colors++;
		if (colors > max_used)
		{
			set< VI >::iterator it;
			bool flag=true;
			for (it = Set.begin(); it != Set.end(); it++)
			{
				CLR(used);
				FA(b,*it) used[color[(*it)[b]]]=true;
				int cnt=0;
				FOR(b,0,7) if (used[b]) cnt++;
				if (cnt!=colors)
				{
					flag=false;
					break;
				}
			}
			if (flag)
			{
				max_used=colors;
				VI vec;
				FOR(b,0,n-1) vec.push_back(color[b]);
				ans = vec;
			}
		}
	}

	cout << max_used << "\n";
	FA(a,ans) cout << ans[a]+1 << " ";
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin >> T;
	FOR(z,1,T)
	{
		cerr << z << "\n";
		cin >> n >> m;
		FOR(a,1,m)
		{
			cin >> be[a];
			be[a]--;
		}
		FOR(a,1,m)
		{
			cin >> en[a];
			en[a]--;
		}
		cout << "Case #" << z << ": ";
		sol();
		cout << "\n";
	}
	return 0;
}