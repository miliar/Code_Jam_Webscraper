#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <memory.h>
using namespace std;
    
#define pb push_back
#define fi first
#define sc second
#define mp make_pair
#define cs c_str
#define ALL(c) (c).begin(), (c).end()
#define RALL(c) (c).rbegin(), (c).rend()
#define RESET(c,x) memset (c, x, sizeof (c))
#define ren(a,b,c) for (int a=b;a<c;a++)
#define red(a,b,c) for (int a=b;a>=c;a--)
#define repi(it,c) for (__typeof ((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define pqd(c) priority_queue <__typeof(c)>
#define pqi(c) priority_queue < __typeof(c),vector<__typeof(c)>,greater<__typeof(c)> >

const double eps = 1e-9;

typedef long long ll;
typedef pair <int,int> pii;

//lintaor1's template

int main()
{
	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	
	int T;
	scanf("%d",&T);
	ren (N,0,T)
	{
		char i[1000];
		int c, d, n;
		vector <char> v;
		map < char,vector<char> > opp;
		map < pair<char,char>,char > ivk;
		map < char,int > lho;
		
		scanf("%d",&c);
		while (c--)
		{
			scanf("%s",i);
			ivk[mp(i[0],i[1])] = i[2];
			ivk[mp(i[1],i[0])] = i[2];
		}
		scanf("%d",&d);
		while (d--)
		{
			scanf("%s",i);
			opp[i[0]].pb(i[1]);
			opp[i[1]].pb(i[0]);
		}
		
		scanf("%d",&n);
		scanf("%s",i);
		ren (x,0,n)
		{
			if (v.empty()) v.pb(i[x]), ++lho[i[x]]; else
			{
				char tmp = i[x];
				while ((!v.empty()) && (ivk.count(mp(v.back(),tmp))))
				{
					tmp = ivk[mp(v.back(),tmp)];
					if (--lho[v.back()]<=0) lho.erase(v.back());
					v.pop_back();
				}
				repi (it,opp[tmp]) if ((lho.count(*it)) && (lho[*it]>0))
				{
					v.clear(), lho.clear(), tmp=0;
					break;
				}
				if (tmp != 0) v.pb(tmp), ++lho[tmp];
			}
			//repi(it,s) printf("%c ",*it); printf("\n");
		}
		
		int sz = v.size();
		printf("Case #%d: [",N+1);
		ren (x,0,sz) printf("%c%s",v[x],(x<sz-1)?", ":"");
		printf("]\n");
		
	}
	return 0;
}
