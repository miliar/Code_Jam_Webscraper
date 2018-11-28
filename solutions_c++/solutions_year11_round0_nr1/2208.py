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
#define abs(a) ((a)>0?(a):(-(a)))
#define swap(a,b) {typeof(a) t_=a; a=b; b=t_;}
#define For(i,a,b) for(int &i_=i=(a), e_=(b); i_<e_; ++i_)
#define cinar(m,n) for(int i_=0; i_<n; ++i_) cin>>m[i_];
#define fill(m) memset(m,0,sizeof(m));
#define null NULL
#define pi 3.141592653589793
#define y1 stupid_math
typedef long long int64;
typedef unsigned char byte;
using namespace std;

int t, n, i, ti;
char c[105];
int d[105];

int main(){
	freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
	
	cin>>t;
	
	For(ti,1,t+1){
		cin>>n;
		For(i,0,n) cin>>c[i]>>d[i];
		
		int tmb=0, tmo=0, tm=0;
		int o=1, b=1;
		
		For(i,0,n){
			if(c[i]=='O'){
				tmo=max(tmb,tmo+abs(d[i]-o))+1;
				o=d[i];
			}else{
				tmb=max(tmo,tmb+abs(d[i]-b))+1;
				b=d[i];
			}
			
		}
		
		cout<<"Case #"<<ti<<": "<<max(tmb,tmo)<<endl;
	}
	
	
	
	
	return 0;
}