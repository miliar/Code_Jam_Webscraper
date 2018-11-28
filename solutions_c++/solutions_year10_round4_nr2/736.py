#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <map>

int T, P, pp, cost;
int val[2000];

void get(){
	int c=getchar();
	while(c=='\n')c=getchar();
	while(c!='\n')c=getchar();
	return;
}

int dc(int l, int r, int lv){
	
	if(l+1 == r){
		int min = val[l]<val[r] ? val[l] : val[r];
	//	printf("dc %d %d : %d min %d\n", l, r, lv, min);
		if(min + lv < P)cost++;
		return min;
	}
	int min, a, b;
	a = dc(l, (l+r)/2, lv+1);
	b = dc((l+r)/2+1, r, lv+1);
	min = a<b ? a : b;
//	printf("dc %d %d : %d min %d\n", l, r, lv, min);
	if(min + lv < P)cost++;
	return min;
}

int main(){
	scanf("%d", &T);
	for(int cc=1; cc<=T; cc++){
		cost = 0;
		scanf("%d", &P);
		pp= 1<<P;
		for(int i=0; i<pp; i++)
			scanf("%d", &val[i]);
		for(int i=0; i<P; i++)
			get();
		dc(0, pp-1, 0);
		printf("Case #%d: %d\n", cc, cost);
	}
}
