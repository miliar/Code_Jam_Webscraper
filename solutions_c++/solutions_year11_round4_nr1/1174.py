#include<cstdio>
#include<algorithm>
#define MN 1002
using namespace std;
struct rapi {
	long double p,k,s;
	rapi():p(0),k(0),s(0){};
	rapi(long double P,long double K, long double S):p(P),k(K),s(S){};
};
long double abs(long double xx) { return xx<0?-xx:xx; }
bool taniej(rapi rapia, rapi rapib) { return (abs((rapia.s-rapib.s))<1e-6)?rapia.p<rapib.p:rapia.s<rapib.s; }
bool wczesniej(rapi rapia, rapi rapib) { return rapia.p<rapib.p; }
int test,ntest,n,a,i;
long double x,b,s,r,w;
rapi t[MN+MN];

int main()
{
	scanf("%d",&ntest);
	for(test=1; test<=ntest; ++test) {
		w=0;
		scanf("%Lf%Lf%Lf%Lf%d",&x,&s,&r,&b,&n);
		for(i=0; i<n; ++i) scanf("%Lf%Lf%Lf",&t[i].p,&t[i].k,&t[i].s);
		sort(t,t+n,wczesniej);
		a=n;
		if(t[0].p>0) t[n++]=rapi(0,t[0].p,0);
		if(t[a-1].k<x) t[n++]=rapi(t[a-1].k,x,0);
		for(i=1; i<a; ++i)
			if(t[i].p>t[i-1].k)
				t[n++]=rapi(t[i-1].k,t[i].p,0);
		sort(t,t+n,taniej);
		for(i=0; i<n; ++i) {
			if(b>0) {
				if(t[i].k-t[i].p<(t[i].s+r)*b) { //biegniemy cały
					b-=(t[i].k-t[i].p)/(t[i].s+r);
					w+=(t[i].k-t[i].p)/(t[i].s+r);
				} else { // biegniemy ile się da
					w+=b;
					t[i].p+=(t[i].s+r)*b;
					b=0;
					w+=(t[i].k-t[i].p)/(t[i].s+s);
				}
			} //idziemy
			else w+=(t[i].k-t[i].p)/(t[i].s+s);
		}
		printf("Case #%d: %.12Lf\n",test,w);
	}
}

