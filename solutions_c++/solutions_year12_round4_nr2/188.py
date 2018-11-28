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
#define X first
#define Y second
#define r first
#define ind second
typedef long long LL;
typedef __int128_t VL;

int W, L, N;
bool zamien;
pair<int, int> promienie[1123];
pair<int, int> wyn[1123];


int main(){
	int testy;
	scanf("%d", &testy);
	for(int t = 1; t <= testy; t++){
		printf("Case #%d: ", t);
		scanf("%d %d %d", &N, &W, &L);
		if(W < L)
			zamien = false;
		else{
			zamien = true;
			swap(W, L);
		}
		for(int i = 0; i < N; i++){
			scanf("%d", &promienie[i].r);
			promienie[i].ind = i;
		}
		sort(promienie, promienie+N);
		reverse(promienie, promienie+N);
		int grwys = promienie[0].r, grszer = 0, wysdawaj = 0;
		for(int i = 0; i < N; i++){
			if(grszer == 0){
				wyn[promienie[i].ind].Y = 0;
			}
			else{
				if(grszer+promienie[i].r <= W)
					wyn[promienie[i].ind].Y = grszer+promienie[i].r;
				else{
					wyn[promienie[i].ind].Y = 0;
					grwys = grwys + 2*promienie[i].r;
					wysdawaj = grwys-promienie[i].r;
				}
			}
			grszer = wyn[promienie[i].ind].Y+promienie[i].r;
				
			wyn[promienie[i].ind].X = wysdawaj;
				
			
		}
		
		if(zamien)
			for(int i = 0; i < N; i++)
				printf("%d %d ", wyn[i].X, wyn[i].Y);
		else
			for(int i = 0; i < N; i++)
				printf("%d %d ", wyn[i].Y, wyn[i].X);
		printf("\n");
	}
	return 0;
}
