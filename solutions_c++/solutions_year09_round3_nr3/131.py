#include<iostream>
using namespace std;

long n;
long p,q;
bool t[10001];
long z[101];
long ans[101][101];

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	long h,i,j,k;
	scanf("%ld",&n);
	for(h=1;h<=n;h++){
		scanf("%ld%ld",&p,&q);
		z[0]=0;
		for(i=1;i<=q;i++)
			scanf("%ld",&z[i]);
		z[q+1]=p+1;
		for(i=1;i<=q;i++)
			ans[i][i]=z[i+1]-z[i-1]-2;
		for(i=1;i<=q;i++)
			for(j=1;i+j<=q;j++){
				ans[j][i+j]=100000000;
				for(k=j;k<=i+j;k++)
					if(ans[j][k-1]+ans[k+1][i+j]+(z[i+j+1]-z[j-1]-2)<ans[j][i+j])
						ans[j][i+j]=ans[j][k-1]+ans[k+1][i+j]+(z[i+j+1]-z[j-1]-2);
			}
		printf("Case #%ld: %ld\n",h,ans[1][q]);
	}
	return 0;
}