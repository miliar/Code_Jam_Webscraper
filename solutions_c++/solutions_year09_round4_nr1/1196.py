#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <algorithm>

using namespace std;

#define TAM 128
#define INF 0x3f3f3f3f

int n;
int ans;
int casado[TAM],foi[TAM],ultimo1[TAM];
char row[TAM][TAM];

void minmovimento(){
	int i,j;
	int v[TAM];
	int c;
	for(i=1;i<=n;i++) v[i] = casado[i];
    
    c=0;   
    for(i=2;i<=n;i++){
		j = i;
		while(j>=2 && v[j] < v[j-1]){
           swap(v[j],v[j-1]);
		   c++;
		   j--;
		}
	}     
	  
	ans = min(ans,c);
}

void solve(int k){
	int i;
	if(k == n + 1){
		minmovimento();
		return;
	}
	for(i=ultimo1[k];i<=n;i++)
		if(!foi[i]){
	   	   casado[k] = i;
		   foi[i] = 1;
		   solve(k+1);
		   foi[i] = 0;
		}
}

int main(){
	int t,nt;
	int i,j;
	scanf("%d",&nt);
	for(t=1;t<=nt;t++){
		scanf("%d",&n);
		for(i=1;i<=n;i++){
			scanf(" %s",row[i]);			
			ultimo1[i] = 0;
			for(j=0;j<n;j++) if(row[i][j] == '1') ultimo1[i] = j+1;
		}
		ans = INF;
		for(i=1;i<=n;i++){
			foi[i] = 0;
			casado[i] = -1;
		}
		solve(1);
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}