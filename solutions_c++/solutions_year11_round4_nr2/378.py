#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
using namespace std;

int t,r,c,d;
char w[100][100];

int main(){
	int h,i,j,k,l,m;
	int a,b,s,ans;
	scanf("%d",&t);
	for(h=1;h<=t;h++){
		scanf("%d%d%d",&r,&c,&d);
		for(i=0;i<r;i++)
			scanf("%s",w[i]);
		ans=0;
		for(i=0;i<r;i++){
			for(j=0;j<c;j++){
				for(k=2;i+k<r && j+k<c;k++){
					a=b=s=0;
					for(l=i;l<=i+k;l++){
						for(m=j;m<=j+k;m++){
							if((l==i || l==i+k) && (m==j || m==j+k))continue;
							a+=(d+w[l][m]-'0')*l;
							b+=(d+w[l][m]-'0')*m;
							s+=d+w[l][m]-'0';
						}
					}
					if(2*a==s*(2*i+k) && 2*b==s*(2*j+k) && ans<k)
						ans=k;
				}
			}
		}
		printf("Case #%d: ",h);
		if(ans==0)printf("IMPOSSIBLE\n");
		else printf("%d\n",ans+1);
	}
	return 0;
}
