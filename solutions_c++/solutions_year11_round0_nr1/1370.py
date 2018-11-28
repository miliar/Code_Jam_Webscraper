#pragma comment (linker, "/STACK:90000000")
#include <string>
#include <memory.h>
#include <cassert>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <sstream>
#include <utility>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define forv(i, v) for (int i = 0; i < (int)(v.size()); ++i)
#define fors(i, s) for (int i = 0; i < (int)(s.length()); ++i)
#define all(a) (a).begin(), (a).end()
#define pb push_back
#define mp make_pair
#define lng long long
#define eps 1e-9
#define iinf 1000000000
#define SQ(a) ((a)*(a))
#define EQ(a,b) fabs((a)-(b))<eps

int src[110];
int n;
queue<int> qu[2];

int main(){
#ifdef __ASD__
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#endif

	int tc;
	cin>>tc;
	forn(qqq,tc){

		cin>>n;
		forn(i,n){
			char c;
			int v;
			cin>>c>>v;
			--v;
			int t=c=='O';
			qu[t].push(v);
			src[i]=t;
		}
		qu[0].push(iinf);
		qu[1].push(iinf);

		int g[2]={qu[0].front(),qu[1].front()};
		int res=0;
		forn(i,n){
			int b=src[i];
			res+=g[b]+1;
			g[1-b]=max(0,g[1-b]-g[b]-1);
			int t=qu[b].front();
			qu[b].pop();
			g[b]=abs(t-qu[b].front());
		}

		forn(i,2)
			qu[i].pop();

		printf("Case #%d: %d\n",qqq+1,res);
	}

    return 0;
}