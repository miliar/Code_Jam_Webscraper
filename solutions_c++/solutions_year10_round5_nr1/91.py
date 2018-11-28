
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
#include <cassert>
using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
#define f first
#define s second


template<class T>
void exgcd(T x, T y, T &a, T &b, T &c){
	//0<x,0<y に対して、ax+by=c となるa,b,c(c=gcd(x,y)) を求める
	T c0=x,c1=y;
	T a0=1,a1=0;
	T b0=0,b1=1;

	while(c1){
		T p=c0/c1;
		c0%=c1;
		a0-=p*a1;
		b0-=p*b1;
		swap(a0,a1); swap(b0,b1); swap(c0,c1);
	}

	a=a0; b=b0; c=c0;
}

//for 0<x,0<y, return a,b s.t. ax+by=z (it is possible a<0 and/or b<0)
//if(a,b) is one solution, (a+k*da, b+k*db) is another solution.
template <class T>
void eq_solve(T x, T y, T z, T &a, T &b, T &da, T &db, T &error){
	error=0;
	T c;
	exgcd(x,y,a,b,c); //Now aX+bY==c && c==gcd(X,Y)
	if(z%c){error=1;return;}
	T v=z/c;
	a*=v;b*=v; //be careful to overflow!
	da=y/c,db=-x/c;
}

const int N=1000*1000+10;
char pp[N]={0};
int p[N/10];
int np=0;

int main(){
	pp[0]=pp[1]=1;
	p[np++]=2;
	for(int i=2*2;i<N;i+=2)pp[i]=2;
	for(int i=3;i<N;i+=2)if(pp[i]==0){
		p[np++]=i;
		for(int k=2*i;k<N;k+=i)pp[k]=i;
	}
	//for(int i=0;i<np;i++)cout<<i<<" "<<p[i]<<endl;

	int nn;scanf("%d",&nn);
	for(int npr=1;npr<=nn;npr++){
		int amb=0;
		int ans=-1;
		int D,K;scanf("%d%d",&D,&K);

		int tenD=1;
		for(int i=0;i<D;i++)tenD*=10;

		int v[K];
		for(int i=0;i<K;i++)scanf("%d",v+i);

		int maxv=-1;
		for(int i=0;i<K;i++)maxv=max(maxv,v[i]);

		if(K==1){amb=1;goto output;}
		if(K==2){
			if(v[0]==v[1]){ans=v[0];goto output;}
			else {amb=1;goto output;}
		}

		ll dw[K-1];
		for(int i=0;i<K-1;i++)dw[i]=(v[i+1]-v[i]);
		//now dw[1]=A*dw[0] (mod P)

		for(int i=0;i<np && p[i]<tenD;i++){
			if(p[i]<=maxv)continue;

			ll P=p[i];
			//cout<<"P"<<P<<endl;
			ll dn[K-1];
			for(int i=0;i<K-1;i++)dn[i]=(dw[i]%P+P)%P;

			int cand=-1;
			int okay=1;
			for(int i=0;i<K-2;i++){
				ll a,b,da,db,err;
//for 0<x,0<y, return a,b s.t. ax+by=z (it is possible a<0 and/or b<0)
//if(a,b) is one solution, (a+k*da, b+k*db) is another solution.
				eq_solve(dn[i],P,dn[i+1], a,b,da,db, err);
				assert(err==0);//if(err){okay=0;break;}

				int val=(a%P+P)%P;
				//cout<<"val"<<val<<" cand"<<cand<<endl;

				if(cand==-1)cand=val;
				else{
					if(cand!=val){okay=0;break;}
				}
			}
			//cout<<"A"<<cand<<" diff"<<v[K-1]-v[K-2]<<" "<<v[K-1]<<endl;
			cand=((cand*(ll)(v[K-1]-v[K-2])+v[K-1])%P+P)%P;
			//cout<<" real cand"<<cand<<endl;

			if(okay==1){
				if(ans==-1)ans=cand;
				else if(ans==cand);
				else{amb=1;goto output;}
			}
		}
		assert(ans!=-1);

output:
		printf("Case #%d: ",npr);
		if(amb)puts("I don't know.");
		else printf("%d\n",ans);
	}
	return 0;
}
