/* Asyamov Igor
e-mail: igor9669@gmail.com*/

#include <iostream>
#include <deque>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <map>
#include <fstream>
#include <cstdlib>
#include <queue>
#include <bitset>
#include <set>
#include <stack>
#include <utility>
#include<cassert>
using namespace std;
#define FR(i,a,b) for(int i=(a);i<(b);++i)
#define FOR(i,n) FR(i,0,n)
#define CLR(x,a) memset(x,a,sizeof(x))
#define MP make_pair
#define PB push_back
#define A first
#define B second
#define Len(a) (int)a.length()
#define Sz(a) (int)a.size()
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<VI > VVI;
#define MAXN 51
const double Eps=1e-9;
const double Pi=2*acos(0.0);
const int inf=1000*1000*1000;
int x[MAXN],v[MAXN],s[MAXN],tt[MAXN];
int main()
{
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	FOR(cur,t)
	{
		int n,k,b,time;
		scanf("%d%d%d%d",&n,&k,&b,&time);
		FOR(i,n)scanf("%d",&x[i]);
		FOR(i,n)scanf("%d",&v[i]);
		
		FOR(i,n)s[i]=b-x[i];
		FOR(i,n)
		{
			if(s[i]%v[i]==0)tt[i]=s[i]/v[i];
			else tt[i]=s[i]/v[i]+1;
		}
		int cnt=0,sw=0,tmp=0;
		for(int i=n-1;i>=0;--i)
		{
			if(tt[i]<=time)
			{
				cnt++;
				sw+=tmp;
				if(cnt==k)break;
			}
			else
			{
				tmp++;
			}
		}
		printf("Case #%d: ",cur+1);
		if(cnt<k)printf("IMPOSSIBLE\n");
		else printf("%d\n",sw);
	}
	return 0;
}