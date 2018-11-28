#include <cstdio>
#include <cstring>
#include <cassert>

using namespace std;

int table[100][100];

int W[100];
int L[100];
int WA[100][100];

double WP[100];
double OWP[100];
double OOWP[100];


int main(){
	int tc, tcN;
	scanf("%d", &tcN);
	for(tc=0; tc<tcN; ++tc){
		memset(W, 0, sizeof(W));
		memset(L, 0, sizeof(L));
		memset(WA, 0, sizeof(WA));
		memset(WP, 0, sizeof(WP));
		memset(OWP, 0, sizeof(OWP));
		memset(OOWP, 0, sizeof(OOWP));
		char buffer[1024];
		int N;
		scanf("%d", &N);
		gets(buffer);
		for(int i=0; i<N; ++i){
			gets(buffer);
			for(int j=0; j<N; ++j){
				if(buffer[j] == '1'){
					++W[i];
					++L[j];
					++WA[i][j];
				}
			}
		}
		for(int i=0; i<N; ++i){
			WP[i] = (double)W[i]/(W[i] + L[i]);
			for(int j=0; j<N; ++j){
				if(j==i)
					continue;
				if(!WA[i][j] && !WA[j][i])
					continue;
				int wj = W[j];
				int lj = L[j];
				if(WA[i][j])
					--lj;
				if(WA[j][i])
					--wj;
				OWP[i] += (double)wj/(lj + wj);
			}
			OWP[i] /= W[i] + L[i];
		}
		printf("Case #%d:\n", tc+1);
		for(int i=0; i<N; ++i){
			for(int j=0; j<N; ++j){
				if(j==i)
					continue;
				if(!WA[i][j] && !WA[j][i])
					continue;
				OOWP[i] += OWP[j];
			}
			OOWP[i] /= W[i] + L[i];
			//printf("%lf %lf %lf\n", WP[i], OWP[i], OOWP[i]);
			printf("%.20lf\n", 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
		}

	}
}
