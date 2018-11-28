#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<cmath>
using namespace std;

#define F(i,n) for(i=0;i<n;i++)
#define FF(i,n) for(i=1;i<=n;i++)
#define LL __int64

char s[110][110];

double a[110], b[110], c[110], p[110];

int main(){
     int i, j, T, TT=1, k, n;
	double x, y;
     freopen("A-large.in","r",stdin);
     freopen("A.out","w",stdout);
     scanf("%d",&T);
     while(T--){
		scanf("%d",&n);
		F(i,n)scanf("%s",s[i]);
		// wp
		F(i,n){
			x = y = 0.0;
			F(j,n){
				if(s[i][j]=='1') x+=1;
				if(s[i][j]!='.') y+=1;
			}
			a[i] = x/y;
			p[i] = y;
//			cout<<a[i]<<endl;
		}
		// owp
		F(i,n){
			x = y = 0;
			F(j,n)if(s[i][j]!='.'){
				
				if(s[j][i]=='1') x += (a[j]*p[j]-1)/(p[j]-1);
				else x += (a[j]*p[j])/(p[j]-1);
					
				y += 1.0;
			}
			b[i] = x/y;
//			cout<<b[i]<<' '<<x<<' '<<y<<endl;
		}
		// oowp
		F(i,n){
			x = y = 0;
			F(j,n)if(s[i][j]!='.'){
				x += b[j];
				y += 1.0;
			}
			c[i] = x/y;
//			cout<<c[i]<<endl;
		}
//		cout<<a[0]<<endl;
		printf("Case #%d:\n",TT++);
		F(i,n) printf("%.10lf\n", a[i]*0.25+b[i]/2.0+c[i]/4.0);
	}
     
     return 0;
}
