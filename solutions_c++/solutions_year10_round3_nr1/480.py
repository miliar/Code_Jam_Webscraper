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
#define MAXN 1001
const double Eps=1e-9;
const double Pi=2*acos(0.0);
const int inf=1000*1000*1000;

vector<PII>p;
int main()
{
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	int t,cnt=0;
	scanf("%d",&t);
	FOR(cur,t)
	{
		int n;
		scanf("%d",&n);
		
		int pos=0;
		cnt=0;
		p.clear();
		FOR(i,n)
		{
			int x,y;
			scanf("%d%d",&x,&y);
			p.PB(MP(x,y));
		}
		sort(p.begin(),p.end());
		FOR(i,n)
		{
			FR(j,i+1,n)
			{
				if((p[i].A> p[j].A && p[i].B>p[j].B) || p[i].A<p[j].A && p[i].B<p[j].B)
				{
					//nothing
				}
				else cnt++;
			}
		}
		printf("Case #%d: ",cur+1);
		printf("%d\n",cnt);
	}
	return 0;
}