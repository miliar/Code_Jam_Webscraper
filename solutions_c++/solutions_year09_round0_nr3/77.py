#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define MAXN 550
#define WSIZE 19
#define MOD 10000

char welc[] = "-welcome to code jam";

int n;
char input[MAXN];

int resp[MAXN][1+WSIZE];

void printpadded(int resp){
	int k = MOD/10;
	while(resp < k){
		printf("0");
		k /= 10;	
	}
	
	if(k != 0){
		printf("%d",resp);
	}	
}

int main(){
	
	int t,lp;
	int i,j;
	scanf(" %d ",&t);
	
	for(lp=1;lp<=t;lp++){
		gets(&input[1]);
		n = strlen(&input[1]);
		for(i=0;i<=n;i++){
			for(j=0;j<=WSIZE;j++){
				resp[i][j] = 0;	
			}	
		}
		
		resp[0][0] = 1;
		
		for(i=1;i<=n;i++){
			for(j=0;j<=WSIZE;j++){
				resp[i][j] = resp[i-1][j];
				if(j > 0){
					if(input[i] == welc[j]){
						resp[i][j] += resp[i-1][j-1];
						if(resp[i][j] >= MOD) resp[i][j] -= MOD;	
					}
				}
			}	
		}
		
		/*
		for(i=0;i<=n;i++){
			for(j=0;j<=WSIZE;j++){
				printf("%d ",resp[i][j]);		
			}
			printf("\n");
		}
		*/
		
		printf("Case #%d: ",lp);
		printpadded(resp[n][WSIZE]);
		printf("\n");
			
	}
		
	return 0;
	
}
