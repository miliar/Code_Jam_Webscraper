#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <iomanip>
#include<cstdlib>
#include<cstdio>
#define pb push_back
#define mp make_pair
#define PI 3.14159265358979
#define forn(i, n) for(int i = 0; i < n; ++i)
#define fort(i, n) for(int i = 1; i <= n; ++i)
#define ALL(x) x.begin(), x.end()
#define L(s) (int)((s).size())
#define ms(x) memset(x,0,sizeof(x));
#define del(y,x) erase(y.begin()+x)
typedef long long ll;
using namespace std;
#pragma comment(linker, "/stack:240000000")
typedef pair<int,int> pii;
const int INF = 2147483647;
const ll LLINF = 9223372036854775807LL;
const int ST = 100010;
const int ST1 = 1000010;
bool myf (pair <int, int> i ,pair <ll, int> j) { if (i.first == j.first) return (i.second < j.second);  else return (i.first>j.first); }
bool myf2 (int i , int j) { return (i>j); }
int ABS(int a)
{
        if(a<0)
                return a*(-1);
        else
                return a;
}
int st[31];
int os[31];
void gen()
{
	for(int i = 1;i<=30;i++)
	{
		st[i] = (i-1)/3+1;
		if((i-1)%3==0)
		{
			os[i] = (i-1)/3+1;
		}
		else
			os[i] = (i-1)/3+2;
	}
}

int main()
{
ios_base::sync_with_stdio(0);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	int test = 1;
	gen();
	while(T)
	{
		int n,s,p,ans = 0,k = 0;
		cin >> n >> s >> p;
		for(int i = 0;i < n;i++)
		{
			int a;
			cin >> a;
			if(st[a]>=p)
				ans++;
			else
				if(os[a]>=p && k<s)
				{
					ans++;
					k++;
				}
		}
		cout << "Case #" << test << ": "  << ans << endl;
		test++;
		T--;
	}
}
