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

int t,ti,n,m,i,j,k;
char s[1000], a[1000];
char c[40][5]; int cn;
char o[100][5]; int on;

int main(){
	freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
	
	cin>>t;
	
	For(ti,1,t+1){
		cin>>cn;
		For(i,0,cn) cin>>c[i]; 
		
		cin>>on; 
		For(i,0,on) cin>>o[i];
		
		cin>>n>>s;
		
		m=0;
		
		For(i,0,n){
			a[m++]=s[i];
			if(m>1)
			For(j,0,cn){
				if(c[j][0]==a[m-2] && c[j][1]==a[m-1]){
					--m; 
					a[m-1]=c[j][2];
					break;
				}
				if(c[j][1]==a[m-2] && c[j][0]==a[m-1]){
					--m; 
					a[m-1]=c[j][2];
					break;
				}
			}
			
			For(j,0,on){
				bool f=false;
				For(k,0,m-1){
					if(a[m-1]==o[j][1] && a[k]==o[j][0]){
						f=true;
						break;
					}
					if(a[m-1]==o[j][0] && a[k]==o[j][1]){
						f=true;
						break;
					}
				}
				if(f){
					m=0;
					break;
				}
			}
		}
		
		cout<<"Case #"<<ti<<": [";
		For(i,0,m){
			cout<<a[i];
			if(i<m-1) cout<<", ";
		}
		cout<<"]\n";
	}
	
	return 0;
}