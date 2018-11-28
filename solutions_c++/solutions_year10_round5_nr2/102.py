
#include <iostream>
#include <sstream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <string>
#include <complex>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

typedef long long ll;
typedef pair<ll,int> pli;
typedef pair<pli,pli> pplipli;
#define f first
#define s second

int main(){
	int nn;scanf("%d",&nn);
	for(int npr=1;npr<=nn;npr++){
		ll L;
		int n;scanf("%lld%d",&L,&n);
		ll v[n];
		for(int i=0;i<n;i++)scanf("%lld",v+i);
		sort(v,v+n);
		int maxv=v[n-1];

		int mincnt[maxv];
		ll  minval[maxv];memset(minval,-1,sizeof(minval));
		priority_queue<pplipli> q;q.push(pplipli(pli(0,0),pli(0,0)));
		while(q.size()){
			int cnt=q.top().f.s;
			ll  val=q.top().s.f;
			int rem=q.top().s.s;q.pop();

			if(L<val)break;
			if(minval[rem]!=-1)continue;
			mincnt[rem]=cnt;
			minval[rem]=val;

			for(int i=0;i<n-1;i++){
				int newcnt=cnt+1;
				ll newval=val+v[i];
				if(L<newval)break;
				int newrem=newval%maxv;
				if(minval[newrem]!=-1)continue;

				ll vlg=newval-newcnt*maxv;
				q.push(pplipli(pli(vlg,newcnt),pli(newval,newrem)));
			}
		}

		printf("Case #%d: ",npr);
		if(minval[ L%maxv ]==-1)puts("IMPOSSIBLE");
		else printf("%lld\n",mincnt[ L%maxv ]+(L-minval[ L%maxv ])/maxv);
	}
	return 0;
}
