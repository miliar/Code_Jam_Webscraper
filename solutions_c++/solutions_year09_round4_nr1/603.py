#include <algorithm>
#include <stdio.h>
#include <string.h>
using namespace std;

int x[50];
char s[50][50];

int main()
{
	int i,j,n,k,T,t,ret;
	
	freopen("in","r",stdin);
	freopen("out","w",stdout);
		
	scanf("%d",&T);
	
	for(t=0;t<T;t++) {
		scanf("%d",&n);
		
		for(i=0;i<n;i++)
			scanf("%s",s[i]);
			
		memset(x,0,sizeof(x));	
		ret=0;
		
		for(i=0;i<n;i++)
			for(j=0;j<n;j++)
				if(s[i][j]=='1') x[i]=j;	
				
		for(i=0;i<n;i++) {
			for(j=i;j<n;j++) {
				if(x[j]<=i) {k=j; break;}
			}
			
			for(j=k;j>i;j--) {
				ret++; swap(x[j],x[j-1]);}
		}
		
		printf("Case #%d: %d\n",t+1,ret);
	}
}
