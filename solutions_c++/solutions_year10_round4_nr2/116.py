#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>

using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)

//int n,m;
int f[1<<11][12];
int a[1<<11];
int b[1<<11];


int n,m,N;

int main(){
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,k,test,cases=0;
	scanf("%d",&test);
	while (test){
		test--;
		cases++;
		
		scanf("%d",&n);
		N=(1<<n);
		for (i=N;i<N*2;i++){
			scanf("%d",&a[i]);
			for (j=0;j<=a[i];j++) 
				f[i][j]=0;
			for (j=a[i]+1;j<12;j++) 	
				f[i][j]=-1;
		}
		j=N;
		for (i=n-1;i>=0;i--){
			for (k=j/2;k<j;k++) scanf("%d",&b[k]);
			j/=2;
		}
		for (i=N-1;i>0;i--){
			f[i][11]=-1;
			for (j=10;j>=0;j--){
				f[i][j]=-1;
				
				if (f[i][j+1]!=-1) f[i][j]=f[i][j+1];
				if (f[i*2][j]!=-1 && f[i*2+1][j]!=-1) 
					if (f[i][j]==-1||f[i][j]>b[i]+f[i*2][j]+f[i*2+1][j]) 
						f[i][j]=f[i*2][j]+f[i*2+1][j]+b[i];
				
						
				if (f[i*2][j+1]!=-1 && f[i*2+1][j+1]!=-1) 
					if (f[i][j]==-1||f[i][j]>f[i*2][j+1]+f[i*2+1][j+1]) 
						f[i][j]=f[i*2][j+1]+f[i*2+1][j+1];
			}
		}
		int ans=-1;
		for (i=0;i<12;i++){
			if (f[1][i]==-1) continue;
			if (ans==-1||ans>f[1][i]) ans=f[1][i];
		}
		printf("Case #%d: %d\n",cases,ans);
	}
	return 0;
}
