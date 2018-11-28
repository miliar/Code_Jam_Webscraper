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



int main(){
#ifdef __ASD__
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#endif

	int tc;
	cin>>tc;
	forn(qqq,tc){
		int n;
		cin>>n;
		int sum=0;
		int mn=iinf;
		int xor=0;
		forn(i,n){
			int v;
			cin>>v;
			sum+=v;
			mn=min(mn,v);
			xor^=v;
		}
		if(xor!=0)
			printf("Case #%d: NO\n",qqq+1);
		else
			printf("Case #%d: %d\n",qqq+1,sum-mn);
	}

    return 0;
}