#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>

int n,a[1500],b[1500];

int main(){
	int zz,zzn,i,ans,j;
	for(zzn=1,scanf("%d",&zz);zzn<=zz;zzn++){
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%d%d",a+i,b+i);
		
		for(ans=i=0;i<n;i++){
			for(j=0;j<i;j++){
				if((a[i]<a[j]&&b[i]>b[j])||
					(a[i]>a[j]&&b[i]<b[j]))ans++;
			}
		}
		
		printf("Case #%d: %d\n",zzn,ans);
	}
	system("pause");
	return 0;
}
