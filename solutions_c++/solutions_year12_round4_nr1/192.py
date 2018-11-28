#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<deque>
#include<cstring>
#include<string>
#include<cmath>
#include<ctime>
#include<cstdlib>
using namespace std;
#define D first
#define I second
typedef long long LL;
typedef __int128_t VL;

int N;
pair<int, int> liny[10123];
int maxI[10123];

int main(){
	int testy;
	scanf("%d", &testy);
	for(int t = 1; t <= testy; t++){
		scanf("%d", &N);
		for(int i = 0; i < N; i++)
			scanf("%d %d", &liny[i].D, &liny[i].I);
		scanf("%d\n", &liny[N].D);
		liny[N].I = 1000123000;
		fill(maxI, maxI+N+1, -1);
		maxI[0] = liny[0].D;
		for(int i = 0; i < N; i++){
			liny[i].I = min(liny[i].I, maxI[i]);
			for(int j = i; j <= N; j++){
				if(liny[i].I >= liny[j].D-liny[i].D)
					maxI[j] = max(maxI[j], min(liny[j].I, liny[j].D-liny[i].D));
				else
					break;
			}
		
		}
		
	
		if(maxI[N] >= 0)
			printf("Case #%d: YES\n", t);
		else
			printf("Case #%d: NO\n", t);
	}
	return 0;
}
