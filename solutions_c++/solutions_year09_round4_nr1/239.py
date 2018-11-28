#include<iostream>
using namespace std;

long t,n;
char z[50][50];
long q[50];

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	long h,i,j,k,l,w;
	scanf("%ld",&t);
	for(h=1;h<=t;h++){
		scanf("%ld",&n);
			for(i=1;i<=n;i++)
			scanf("%s",z[i]);
		for(i=1;i<=n;i++){
			for(j=n-1;j>=0;j--){
				if(z[i][j]=='1')break;
			}
			q[i]=n-j-1;
		}
		k=0;
		for(i=1;i<=n;i++)
			if(q[i]<n-i)
				for(j=i+1;j<=n;j++)
					if(q[j]>=n-i){
						for(w=j;w>i;w--){
							l=q[w];q[w]=q[w-1];q[w-1]=l;k++;
						}
						break;
					}
		printf("Case #%ld: %ld\n",h,k);
	}
	return 0;
}