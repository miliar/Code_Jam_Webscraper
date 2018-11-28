#include <cstdio>
#include <algorithm>
#include <string>
#include <queue>
#include <iostream>
using namespace std;
int tc,n,r[50],AC,rx[50];
char a[50][50];
int main(){
	scanf("%d",&tc);
	for (int c=1;c<=tc;c++){
		for (int i=0;i<50;i++) r[i]=0,rx[i]=-1;
		AC=0;
		scanf("%d",&n);
		for (int i=0;i<n;i++){
			scanf("%s",a[i]);
			for (int j=0;j<n;j++)
				if (a[i][j]=='1') r[i]++,rx[i]=j+1;
		}
		for (int i=0;i<n-1;i++)
			if (rx[i]>i+1){
				int p=0,tmp[50],tx;
				for (int j=i+1;j<n&&!p;j++) if (rx[j]<=i+1) p=j;
				//for (int k=0;k<n;k++) tmp[k]=a[i][k]; tx=rx[i];
				for (int j=p;j>i;j--){
					for (int k=0;k<n;k++){
						char t=a[j][k];
						a[j][k]=a[j-1][k];
						a[j-1][k]=t;
					}
					int t=rx[j]; rx[j]=rx[j-1]; rx[j-1]=t;
					AC++;
				}
			}

		printf("Case #%d: %d\n",c,AC);
		
	}
	return 0;
}
