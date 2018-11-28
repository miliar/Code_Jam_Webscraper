#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <vector>
using namespace std;
#define FOR(i,a,b) for(i=(a);i<=(b);i++)
#define N 10010

typedef long long ll;

int t,T;
int n;
ll l,h,freq[N];


struct num{
	num() : gearing(1){}
	num(ll div_,ll mul_) : div(div_), mul(mul_), gearing(1){}
	bool isdiv(){
		return div!=0 && mul==0;
	}
	bool ismul(){
		return mul!=0 && div==0;
	}

	ll div;
	ll mul;
	ll gearing;
};

num zeronum(){
	num ret;
	ret.div=ret.mul=ret.gearing=0;
	return ret;
}

ll gcd(ll a, ll b){
	if (a < b) return gcd(b,a);
	if (b==0) return a;
	return gcd(b,a%b);
}

ll lcm(ll a, ll b){
	ll x;
	x = gcd(a,b);
	if (b/x > h/a) throw 0;
	return a*b/x;
}

num output(num a,num b){
	num ret;
	if (a.isdiv() && b.isdiv()){
		ret.div = gcd(a.div,b.div);
		ret.gearing = gcd(a.gearing,b.gearing);
	}
	else if (a.ismul() && b.ismul()){
		ll v = gcd(a.mul,b.mul);
		if (v * a.mul > h*10/b.mul) return zeronum();
	}
	else if (a.isdiv() && b.ismul()){
	}
	return ret;
}

void process(){
	vector<num> list;
	list.push_back(num(0,freq[1]));
	list.push_back(num(freq[1],0));

	int i,j,k;
	FOR(i,2,n){
		vector<num> newv;
		FOR(j,0,1){
			num val,out;
			if (j==0) val = num(0,freq[i]);
			else val = num(freq[i],0);
			FOR(k,0,(int)list.size()-1){
				try{
					out = output(list[k],val);
					newv.push_back(out);
				}
				catch(...){
				}
			}
		}
	}

	printf("Case #%d: ",t);
}


void process2(){
	int i,j;
	FOR(i,l,h){
		FOR(j,1,n){
			if (i%freq[j]==0 || freq[j]%i==0);
			else break;
		}
		if (j==n+1){
			break;
		}
	}
	printf("Case #%d: ",t);
	if (i==h+1){
		printf("NO\n");
	}
	else{
		printf("%d\n",i);
	}
}

int main(){
	freopen("c-small.in","rt",stdin);
	freopen("c-small.out","wt",stdout);
	scanf("%d",&T);
	FOR(t,1,T){
		scanf("%d %lld %lld",&n,&l,&h);
		int i;
		FOR(i,1,n) scanf("%lld",&freq[i]);
		process2();
		//process();
	}
	return 0;
}