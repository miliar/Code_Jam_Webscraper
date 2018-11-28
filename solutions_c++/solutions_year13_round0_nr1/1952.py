#include<iostream>
#include<cmath>
#include<set>
#include<vector>
#include<list>
#include<map>
#include<algorithm>
#include<stdio.h>
#include<string.h>
#include<stack>
#include<queue>
#include<climits>
#include <string>
#include <sstream>

typedef unsigned long long int ULONG;
typedef long long int LONG;
typedef unsigned int UINT;

using namespace std;
#define FOR(i,a,b) for(int i=a;i<b;++i)

#ifndef ONLINE_JUDGE
#include <time.h>
#endif

#include<stdio.h>
#include<iostream>
#include<math.h>

const int S=4;
int N;

int X[2][S],XD[2],O[2][S],OD[2],D[2][S];
char B[S+1][S+1];





int main(){
	freopen("input.in","r",stdin);
#ifndef _DEBUG 
	freopen ("output.txt","w",stdout);
#endif
	clock_t start = clock();

	
	int T;
	scanf("%d",&T);	
	FOR(tT,0,T){
		FOR(i,0,S){
			scanf("%s",B[i]);
			X[0][i]=X[1][i]=0;
			O[0][i]=O[1][i]=0;
			D[0][i]=D[1][i]=0;
		}
		XD[0]=XD[1]=0;
		OD[0]=OD[1]=0;
		FOR(i,0,S){
			FOR(j,0,S){
				if(B[i][j]=='.'){
					D[0][j]++;
					D[1][i]++;
				}else{
					if(B[i][j]=='X' || B[i][j]=='T'){
						X[0][j]++;
						X[1][i]++;
						if(i==j)XD[0]++;
						if(i==(S-j-1))XD[1]++;
					}
					if(B[i][j]=='O' || B[i][j]=='T'){
						O[0][j]++;
						O[1][i]++;
						if(i==j)OD[0]++;
						if(i==(S-j-1))OD[1]++;
					}
				}
				
			}
		}
		printf("Case #%d: ",tT+1);
		if(XD[0]==S || XD[1]==S){
			printf("X won");
				goto E;
		}
		if(OD[0]==S || OD[1]==S){
			printf("O won");
				goto E;
		}
		FOR(i,0,S){
			if(X[0][i]==4 || X[1][i]==4){
				printf("X won");
				goto E;
			}
			if(O[0][i]==4 || O[1][i]==4){
				printf("O won");
				goto E;
			}
		}
		int i;
		for(i=0;i<S;i++){
			if(D[0][i]!=0 || D[1][i]!=0)
				break;
		}
		if(i!=S)printf("Game has not completed");
		else printf("Draw");
		E:
		printf("\n");
	}

#ifdef _DEBUG 	
	printf("Time elapsed: %f\n", ((double)clock() - start) / CLOCKS_PER_SEC);
#endif
	return 0;
}






