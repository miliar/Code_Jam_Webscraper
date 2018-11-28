#include <stdio.h>
#include <algorithm>
using namespace std;

#define INF 1023456789

main(){
	int datasuu;
	scanf("%d ",&datasuu);
	for(int t=1;t<=datasuu;t++){
		printf("Case #%d: ",t);
		
		int n;
		scanf("%d",&n);
		int c[1100];
		for(int i=0;i<n;i++)scanf("%d",&c[i]);
		int x=0;
		for(int i=0;i<n;i++)x^=c[i];
		if(x!=0)printf("NO\n");
		else{
			int mini=INF,sum=0;
			for(int i=0;i<n;i++){
				mini=min(mini,c[i]);
				sum+=c[i];
			}
			printf("%d\n",sum-mini);
		}
	}
}