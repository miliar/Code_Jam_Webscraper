#include<iostream>
#include<stdio.h>
#define fr(i,a,b) for(i=a;i<=b;++i)
using namespace std;
struct point{
	int x,y,z;
	point(int a=0,int b=0,int c=0):x(a),y(b),z(c){}
};
point operator+(point a,point b){
	return point(a.x+b.x,a.y+b.y,a.z+b.z);
}
point operator-(point a,point b){
	return point(a.x-b.x,a.y-b.y,a.z-b.z);
}
const int maxn=502;
char g[maxn][maxn];
point x[maxn][maxn],s[maxn][maxn];
int i,j,k,ca,ti,n,m,d;
int main(){
	freopen("b2.in","r",stdin);
	freopen("b2.out","w",stdout);
	cin>>ca;
	fr(ti,1,ca){
		cin>>n>>m>>d;
		fr(i,1,n)
			scanf("%s",g[i]+1);
		fr(i,1,n)
			fr(j,1,m){
				x[i][j]=point(i*(g[i][j]-'0'),j*(g[i][j]-'0'),g[i][j]-'0');
				s[i][j]=x[i][j]+s[i-1][j]+s[i][j-1]-s[i-1][j-1];
			}
		bool found=false;
		for(k=min(n,m);k>=3;k--){
			fr(i,1,n-k+1){
				fr(j,1,m-k+1){
					point p=s[i+k-1][j+k-1]-s[i-1][j+k-1]-s[i+k-1][j-1]+s[i-1][j-1]-x[i][j]-x[i+k-1][j+k-1]-x[i][j+k-1]-x[i+k-1][j];
					if(p.x*2==2*i*p.z+(k-1)*p.z&&p.y*2==2*j*p.z+(k-1)*p.z){
						cout<<"Case #"<<ti<<": "<<k<<endl;
						found=true;
						break;
					}
				}
				if(found)
					break;
			}					
			if(found)
				break;
		}
		if(!found)
			cout<<"Case #"<<ti<<": IMPOSSIBLE"<<endl;
	}
}