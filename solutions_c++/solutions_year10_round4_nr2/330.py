#define forn(i, n) for(int i = 0; i<(int) n; i++)
#define ford(i, n) for(int i = (int)n -1; i>=0 ; i--)
#define pb push_back 
#define mp make_pair
#define se second
#define fi first
#define ll long long
#define PI 	3.14159265358979323846264338327950288

#include <vector>
#include <list>
#include <map>
#include <set>
//#include <multiset>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define sss 2000000
using namespace std;
 long long mm[sss+10];
 //pair<int,int> cell[1010];
int miss[2000];
int price[2000];
int t,p;
long long maxx = 1000000000;
long long table[1050][1050][14];
long long calc(int a, int b, int v, int lpr){
	
	if (table[a][b][v]!=-1) 
		return table[a][b][v];
	long long tans;
	if (b==a+1) 
		if (v+miss[a]>=p)
			tans = 0;
		else
			tans = maxx;
	else{
		int mid = (a+b)/2;
		tans = min(calc(a,mid, v, lpr*2+1)+calc(mid,b, v, lpr*2+2),calc(a,mid, v+1, lpr*2+1)+calc(mid,b, v+1, lpr*2+2)+price[lpr]);
		
	}
	table[a][b][v] = tans;
	//cerr<<a<<" "<<b<<" "<<v<<" "<<lpr<<endl;
//	cerr<<tans<<endl;
	return tans;
}
int main(){
	freopen("bl.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &t);
	forn(tn, t)
	{
		scanf("%d", &p);
		forn(i, 1<<p)
			scanf("%d", &miss[(1<<p)-1-i]);
		int games = (1<<p) -1;
		forn(i, games)
			scanf("%d", &price[games-1-i]);
		forn(i, (1<<p)+3)
			forn(j, (1<<p)+4)
				forn(k, p+2)
					table[i][j][k] = -1;
		long long ans = calc(0, 1<<p, 0,0);
		printf("Case #%d: ", tn+1);
		printf("%d", ans);
		printf("\n");
	}
	return 0;
}
