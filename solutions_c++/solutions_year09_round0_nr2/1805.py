#include <iostream>
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define MAX 110
using namespace std;

int T,a,b,l;
int m[MAX][MAX];
char w[MAX][MAX];

void fun(int i, int j){
	//printf("obliczam %d %d\n",i,j);
	int mini;
	mini=m[i][j];
	if(i!=0&&mini>m[i-1][j]) mini=m[i-1][j];
	if(i!=(a-1)&&mini>m[i+1][j]) mini=m[i+1][j];
	if(j!=0&&mini>m[i][j-1]) mini=m[i][j-1];
	if(j!=(b-1)&&mini>m[i][j+1]) mini=m[i][j+1];				
	if(mini<m[i][j]){
		if(i!=0&&mini==m[i-1][j]){
			if(w[i-1][j]=='A') fun(i-1,j);
			w[i][j]=w[i-1][j];
		}
		else if(j!=0&&mini==m[i][j-1]){ 
			if(w[i][j-1]=='A') fun(i,j-1);
 			w[i][j]=w[i][j-1];
		}
		else if(j!=(b-1)&&mini==m[i][j+1]){
			if(w[i][j+1]=='A') fun(i,j+1);
			w[i][j]=w[i][j+1];
		}
		else if(i!=(a-1)&&mini==m[i+1][j]){
			if(w[i+1][j]=='A') fun(i+1,j);
			w[i][j]=w[i+1][j];
		}
	}else{
		if(w[i][j]=='A') w[i][j]='a'+l;
		l++;
	}
}

int main(){
	scanf("%d",&T);
	REP(z,T){		
		scanf("%d %d",&a,&b);
		REP(i,a) REP(j,b) { w[i][j]='A'; scanf("%d",&m[i][j]); }
		l=0;
		printf("Case #%d:\n",z+1);
		REP(i,a){ 
			REP(j,b){
				if(w[i][j]=='A') fun(i,j);
				printf("%c ",w[i][j]);
			}
			printf("\n");
		}
	}
	return 0;
}

