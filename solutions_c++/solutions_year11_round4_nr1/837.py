#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <cstring>
#include <memory.h>
#include <algorithm>
#define sqr(x) ((x)*(x))
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define abs(a) ((a)<0?(-(a)):(a))
#define swap(a,b) {typeof(a) t_=a; a=b; b=t_;}
#define For(i,a,b) for(int &i_=i=(a), e_=(b); i_<e_; ++i_)
#define cinar(m,n) for(int i_=0; i_<n; ++i_) cin>>m[i_];
#define in(x,l,r) ((x)>=(l) && (x)<=(r))
#define fill(m) memset(m,0,sizeof(m));
#define pi 3.141592653589793
#define y1 stupid_math
#define tm stupid_time
typedef long long int64;
typedef unsigned char byte;
using namespace std;

int T, ti;

double s,r,t,x,b[1005],e[1004],w[1003];
int q[1003];
int n,i,j,k,l;

double d,tm;

void sortw(int l, int r){
	int i=l, j=r, t;
	double x=b[(i+j)>>1];
	do{
		while(b[i]<x) ++i;
		while(b[j]>x) --j;
		if(i<=j){
			swap(b[i], b[j]);
			swap(e[i], e[j]);
			++i; --j;
		}
	}while(i<=j);
	if(i<r) sortw(i,r);
	if(l<j) sortw(l,j);
}

void sortt(int l, int r){
	int i=l, j=r, t;
	double x=w[q[(i+j)>>1]];
	do{
		while(w[q[i]]<x) ++i;
		while(w[q[j]]>x) --j;
		if(i<=j){
			swap(q[i], q[j]);
			++i; --j;
		}
	}while(i<=j);
	if(i<r) sortt(i,r);
	if(l<j) sortt(l,j);
}

int main(){
	freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
	
	cin>>T;
	for(ti=1;ti<=T;++ti){
		cin>>x>>s>>r>>t>>n;
		
		for(i=0;i<n;++i) {
			cin>>b[i]>>e[i]>>w[i];
			x-=(e[i]-b[i]);
			q[i]=i;
		}
		w[n]=0;
		b[n]=1e9;
		e[n]=1e9+x;
		q[n]=n;
		++n;
		
		sortw(0,n-1);
		sortt(0,n-1);
		
		double res=0.0;
		
		for(i=0;i<n;++i){
			tm=(e[q[i]]-b[q[i]])/(w[q[i]]+r);
			
			//cout<<e[q[i]]-b[q[i]]<<endl;
			if(tm<=t){
				t-=tm;
				res+=tm;
			}else{
				d=t*(w[q[i]]+r);
				res+=t+(e[q[i]]-b[q[i]]-d)/(s+w[q[i]]);
				t=0;
			}
			
			//cout<<res<<endl;
		}
		
		printf("Case #%d: %.10lf\n",ti,res);
	}
	
	return 0;
}