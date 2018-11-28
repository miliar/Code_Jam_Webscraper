#include <cmath>
#include <ctime>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#define maxl 1000000000
#define maxn 510
using namespace std;

typedef long long ll;

const double eps=1e-8;

ll a1[maxn][maxn],a2[maxn][maxn],a3[maxn][maxn],sum3[maxn][maxn],sum1[maxn][maxn],sum2[maxn][maxn];

int getIt(int x,int n){
	if(n&1)return x-(n+1)/2;else {
		if(x<=n/2)return -(((n/2+1)-x)*2-1);else return (x-n/2)*2-1;
	}
}

char s[maxn];

void solve(){
	int n,m,d,i,j,x,l;
	ll temp1,temp2,temp3,xx,yy;
	scanf("%d%d%d",&n,&m,&d);
	//cout<<n<<" "<<m<<" "<<d<<endl;
	for(i=1;i<=n;++i){
		scanf("%s",s+1);
		for(j=1;j<=m;++j){
			x=s[j]-'0';
			//cout<<x<<endl;
			x+=d;
			a1[i][j]=x;
			sum1[i][j]=sum1[i-1][j]+sum1[i][j-1]-sum1[i-1][j-1]+x;
			a2[i][j]=(ll)x*i;
			sum2[i][j]=sum2[i-1][j]+sum2[i][j-1]-sum2[i-1][j-1]+(ll)x*i;
			a3[i][j]=(ll)x*j;
			sum3[i][j]=sum3[i-1][j]+sum3[i][j-1]-sum3[i-1][j-1]+(ll)x*j;
		}
	}
	for(l=min(n,m);l>=3;--l){
		for(i=1;i<=n-l+1;++i)
			for(j=1;j<=m-l+1;++j){
				temp1=(sum1[i+l-1][j+l-1]-sum1[i-1][j+l-1]-sum1[i+l-1][j-1]+sum1[i-1][j-1]);
				temp1-=a1[i][j]+a1[i+l-1][j]+a1[i][j+l-1]+a1[i+l-1][j+l-1];
				
				temp2=(sum2[i+l-1][j+l-1]-sum2[i-1][j+l-1]-sum2[i+l-1][j-1]+sum2[i-1][j-1]);
				temp2-=a2[i][j]+a2[i+l-1][j]+a2[i][j+l-1]+a2[i+l-1][j+l-1];
				
				temp3=(sum3[i+l-1][j+l-1]-sum3[i-1][j+l-1]-sum3[i+l-1][j-1]+sum3[i-1][j-1]);
				temp3-=a3[i][j]+a3[i+l-1][j]+a3[i][j+l-1]+a3[i+l-1][j+l-1];
				if(l&1){
					xx=i+l/2;
					yy=j+l/2;
					if(temp2-temp1*xx==0 && temp3-temp1*yy==0){
						printf("%d\n",l);
						return;
					}
				}else {
					xx=i+l/2-1;
					yy=j+l/2-1;
					if(temp2*2-temp1*(xx+xx+1)==0 && temp3*2-temp1*(yy+yy+1)==0){
						printf("%d\n",l);
						return;
					}
				}
						
			}
	}
	printf("IMPOSSIBLE\n");
}
	

int main(){
	int t,i;
	scanf("%d",&t);
	for(i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}
} 
