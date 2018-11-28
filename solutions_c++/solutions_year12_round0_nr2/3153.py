#include<iostream>
#include<stdio.h>
#include<assert.h>
#include<string.h>
#include<time.h>
#include<stdlib.h>
#include<math.h>
#include<string>
#include<sstream>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<vector>
#include<algorithm>
#pragma comment(linker, "/STACK:16777216")
#define pb push_back
#define ppb pop_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define LL long long
#define bit __builtin_popcountll
using namespace std;
template<class T> inline T sqr(T x) { return x * x; }
typedef pair<int, int> pii;
const double eps = 1e-9;
const double pi = acos(-1.0);
int a[111],d[33],ds[33];
int sample(int x, int y, int z)
{
	return max(x,max(y,z)) - min(x,min(y,z));
}
int main()
{
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif
	int T,n,s,p;
	for(int i = 0; i <= 30; i++)
	{
		for(int x = 0; x <= 10; x++)
			for(int y = 0; y <= 10; y++)
				for(int z = 0; z <= 10; z++)
				{
					if (x + y + z != i) continue;
					if (sample(x,y,z) < 2) d[i] = max(d[i],max(x,max(y,z)));
					if (sample(x,y,z) <= 2) ds[i] = max(ds[i],max(x,max(y,z)));
				}
	}
	cin>>T;
	for(int t = 0; t < T; t++)
	{
		cin>>n>>s>>p;
		int x = 0,y = 0;
		for(int i = 0; i < n; i++)
		{
			cin>>a[i];
			if (d[a[i]] >= p) x++; else
			if (ds[a[i]] >= p) y++;
		}
		printf("Case #%d: %d\n",t + 1,x + min(y,s));
	}
	return 0;
}
