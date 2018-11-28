#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
using namespace std;

int ggler[101];
int point[]={
0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10
};
int spoint[]={
0,0,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10,0,0
};
int main(){
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; t++){
		//N:googleの数 S:驚くべきgooglerの数 p:p点以上の人を見つけたい。
		int N, S, p;
		int possible = 0;
		scanf("%d %d %d", &N, &S, &p);
		for(int i = 0; i < N; i++)
			scanf("%d", &ggler[i]);
		sort(ggler, ggler + N);
		int ans = 0;
		int pn = 0;
		for(int i = 0; i < N; i++){
			int total = ggler[i];
			if(p <= point[total]){
				//printf("%d <= point[%d]=%d\n",p,total,point[total]);
				ans++;
			}else{
				if(pn < S){
					if(point[total] < p && p <= spoint[total]){
						//printf("p <= spoint[%d]=%d\n",total,spoint[total]);
						pn++;
						ans++;
					}
				}
			}
		}
		printf("Case #%d: %d\n", t + 1, ans);
	}
	return 0;
}

