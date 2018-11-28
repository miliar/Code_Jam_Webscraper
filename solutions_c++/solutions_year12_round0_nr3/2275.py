#include <cstdio>
#include <vector>
#include <algorithm>

#define FOR(i,a,b) for (int i=(a); i<(b); i++)
#define SZ(x) ((int)(x).size())
#define ALL(v) (v).begin() , (v).end()
#define CLR(v) memset(v, 0, sizeof(v));

#define MAX 2000001
#define MEX 935101

using namespace std;

int rec[MAX];
bool used[MEX];
int tens[] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};
vector<int> bros[MEX];

int main() {
	int left, right, d, z, t=1;
	
	FOR(i,1,MAX) {
		for(d=0; i/tens[d]; d++);
//		printf("%d has %d digits\n", i, d);
		
		if (rec[i]) continue;
		bros[t].resize(0);
		bros[t].push_back(i);
		rec[i] = t++;
		
		FOR(j,1,d) {
			left = i/tens[j];
			right = i%tens[j];
			z = left+tens[d-j]*right;
			
			if (right/tens[j-1] && z < MAX && !rec[z]) {
				bros[rec[i]].push_back(z);
				rec[z] = rec[i];
			}
		}
	}
	
//	printf("t = %d\n", t);

	int n, A, B, res;
	scanf("%d", &n);

	FOR(i,0,n) {
		scanf("%d %d", &A, &B);
		res = 0;
		//puts("TEST\n");
		memset(used, 0, sizeof(used));
		FOR(j,A,B+1) {
			if (used[rec[j]]) continue;
			t = 0;
			FOR(k,0,SZ(bros[rec[j]])) {
				if (A <= bros[rec[j]][k] && bros[rec[j]][k] <= B) {
					//printf("%d ", bros[rec[j]][k]);	
					t++;
				}
			}
	//		puts("");
			
			res += t*(t-1)/2;
			used[rec[j]] = true;
		}
		printf("Case #%d: %d\n", i+1, res);
	}
	
/*	
	FOR(i,0,t) {
		FOR(j,0,SZ(bros[i]))
			printf("%d ", bros[i][j]);
		puts("");
	}
	printf("t = %d\n", t);
*/
	return 0;
}