#include <cstdio>
#include <cstring>

using namespace std;

int price[128][26];
int matrix[128][128];
int match[128];
int bio[128];
int N, K;

void load()
{
	scanf("%d%d", &N, &K);

	for (int i = 0; i < N; ++i){
		for (int k = 0; k < K; ++k){
			scanf("%d", &price[i][k]);
		}
	}
}

void generate_matrix(){
	memset(matrix, 0, sizeof matrix);
	for (int i = 0; i < N; ++i){
		for (int j = 0; j < i; ++j){
			int veza = 1;
			for (int k = 1; k < K && veza; ++k){
				if ( ! ((price[i][0] < price[j][0] && price[i][k] < price[j][k]) || (price[i][0] > price[j][0] && price[i][k] > price[j][k])) ){
					veza = 0;
				}
			}
			if (price[i][0] < price[j][0]) matrix[i][j] = veza;
			else matrix[j][i] = veza;
		}
	}
}

int probaj(int s)
{
	for (int i = 0; i < N; ++i){
		if (!bio[i] && matrix[s][i]){
			bio[i] = 1;
			if (match[i] == -1 || probaj(match[i])){
				match[i] = s;
				return 1;
			}
		}
	}

	return 0;
}

int matching()
{
	int sol = 0;
	memset(match, -1, sizeof match);

	for (int i = 0; i < N; ++i){
		memset(bio, 0, sizeof bio);

		if (probaj(i)) ++sol;
	}
	
	return sol;
}

int main()
{
	int T;
	scanf("%d", &T);

	for (int tt = 1; tt <= T; ++tt){
		load();
		generate_matrix();
		
		int mat = matching();

		printf("Case #%d: %d\n", tt, N-mat);
	}
	return 0;
}
