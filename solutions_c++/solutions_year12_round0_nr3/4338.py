#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <set>

#define REP(a,b) for (int a = 0; a < b; a++)
#define FORU(a,b,c) for (int a = b; a <= c; a++)

#define RESET(a,b) memset(a,b,sizeof a)

using namespace std;

int nkasus,n,a,b;
int tot;

int apa(int i ,int j){
	int yo  = 0;
	int dig = 1;
	int dop = i;
	while (dop > 0){
		dop /= 10;
		dig *= 10;
	}	
	dig /= 10;
		
	int jo = i;
	dop = i;
	while (dop > 0){
		jo = (jo%10)*dig + (jo/10);
		dop /= 10;
		
		if (jo == j){
			yo = 1;
			break;	
		}
	}
	return 	yo;
}

int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	
	scanf("%d", &nkasus);
	REP(jt,nkasus){
		scanf("%d%d", &a,&b);
		
		tot = 0;
		FORU(i,a,b-1){
			FORU(j,i+1,b){
				//apakah a,b?
				
				tot += apa(i,j);
			}
		}
		
		
		printf("Case #%d: %d\n", jt+1, tot);
	}
	
	return 0;
}
