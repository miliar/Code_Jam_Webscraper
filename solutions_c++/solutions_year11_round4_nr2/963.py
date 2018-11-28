#include<cstdio>
#include<cstring>
#include<algorithm>
#define MAX_R 500
#define MAX_C 500
#define EPS (1e-10)
using namespace std;
int R, C, D;
char w[MAX_R][MAX_C];
bool check(int si, int sj, int size){
	double a, b;
	a = b = 0.0;
	for(int i=0;i<size;++i){
		for(int j=0;j<size;++j){
			double di, dj;
			if(size%2 == 0){
				if(i < size/2){
					di = i - (size/2 - 0.5);
				}
				else{
					di = i - (size/2 - 0.5);
				}
				if(j < size/2){
					dj = j - (size/2 - 0.5);
				}
				else{
					dj = j - (size/2 - 0.5);
				}
			}
			else{
				di = i - size/2;
				dj = j - size/2;
			}
			if(i == 0 && j == 0 || i == 0 && j == size-1
					|| i == size-1 && j == 0 || i == size-1 && j == size-1){
			}
			else{
				a += (D + w[si+i][sj+j] - '0') * di;
				b += (D + w[si+i][sj+j] - '0') * dj;
			}
		}
	}
	return -EPS < a && a < EPS && -EPS < b && b < EPS;
}
int solve(){
	int res = -1;
	for(int i=0;i<R;++i){
		for(int j=0;j<C;++j){
			for(int k=3; i+k <= R && j+k <=C; ++k){
				bool b = check(i, j, k);
				if(b){
					res = max(res, k);
				}
			}
		}
	}
	return res;
}
int main(){
	int T;
	scanf("%d", &T);
	for(int a=1;a<=T;++a){
		int res;
		scanf("%d%d%d", &R, &C, &D);
		for(int i=0;i<R;++i){
			scanf("%s", w[i]);
		}
		res = solve();
		if(res >= 3){
			printf("Case #%d: %d\n", a, res);
		}
		else{
			printf("Case #%d: IMPOSSIBLE\n", a);
		}
	}
	return 0;
}
