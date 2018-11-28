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
#define Forw(i,a,u) for(i=(a); u; ++i)
#define cinar(m,n) for(int i_=0; i_<n; ++i_) cin>>m[i_];
#define fill(m) memset(m,0,sizeof(m));
#define pi 3.141592653589793
#define y1 stupid_math
typedef long long int64;
typedef unsigned char byte;
using namespace std;

int t,ti;

int n,i,j,k,l,m;
char s[1000][1000];
double wp[200],owp[200],oowp[200],rpi[200];

int main(){
	freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
	
	cin>>t;
	For(ti,0,t){
		cin>>n;
		For(i,0,n) cin>>s[i];
		
		For(i,0,n){
			wp[i]=0; m=0;
			For(j,0,n){
				if(s[i][j]=='1') ++wp[i];
				if(s[i][j]!='.') ++m;
			}
			if(m) wp[i]/=m;
			
			owp[i]=0; m=0;
			For(j,0,n)if(s[i][j]!='.'){
				double w=0; int d=0;
				For(k,0,n) if(k!=i){
					if(s[j][k]=='1') ++w;
					if(s[j][k]!='.') ++d;
				}
				if(d){
					w/=d;
					owp[i]+=w;
					++m;
				}
			}
			if(m) owp[i]/=m;
			
		}
		For(i,0,n){
			oowp[i]=0; m=0;
			For(j,0,n) if(s[i][j]!='.'){
				oowp[i]+=owp[j];
				++m;
			}
			
			if(m) oowp[i]/=m;
			
			rpi[i] = 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i];
		}
		
		printf("Case #%d:\n",ti+1);
		For(i,0,n) printf("%.06lf\n",rpi[i]); 
	}
	
	return 0;
}