#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

#define MAXN 130
#define MOD 10007

int m,n;
int resp[MAXN][MAXN];
bool mrk[MAXN][MAXN];

int main(){
	
	int i,j,k;
	int a,b;
	int t,lp;
	
	scanf("%d",&t);
	
	for(lp=1;lp<=t;lp++){
		scanf("%d %d %d",&m,&n,&k);
		for(i=0;i<m+10;i++){
			for(j=0;j<n+10;j++){
				resp[i][j] = 0;
				mrk[i][j] = false;
			}
		}
		for(i=0;i<k;i++){
			scanf("%d %d",&a,&b);
			mrk[a-1][b-1] = true;
		}
		
		resp[0][0] = 1;
		for(i=0;i<m-1;i++){
			for(j=0;j<n-1;j++){
				a = i+1;
				b = j+2;
				if(!mrk[a][b]) resp[a][b] = (resp[a][b]+resp[i][j]) % MOD;
				a = i+2;
				b = j+1;
				if(!mrk[a][b]) resp[a][b] = (resp[a][b]+resp[i][j]) % MOD;
			}
		}
		
		printf("Case #%d: %d\n",lp,resp[m-1][n-1]);
		
	}
	
	return 0;
	
}