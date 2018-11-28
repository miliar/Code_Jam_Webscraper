#include <iostream>
#include <algorithm>
#include <hash_map>

static const int MAX = 101;
static const int LEN = 110;
static const int QUE = 1002;

static const int MANY = 999999;

using namespace std;

char names[MAX][LEN];
int query[MAX];

int main(){
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int N;
	cin >> N;
	for (int po = 0; po < N; po++){
		int S;
		scanf("%d\n",&S);
		for (int i = 0; i < S; i++){
			gets(names[i]);
		}
		int Q;
		scanf("%d\n",&Q);
		for (int i = 0; i < Q; i++){
			char buf[LEN];
			gets(buf);
			for (int j = 0; j < S; j++){
				if (!strcmp(buf, names[j])){
					query[i] = j;
					break;
				}
			}
		}
		if (!Q){
			cout << "Case #" << po+1 << ": " << 0 << "\n";
			continue;
		}
		int res[QUE][MAX];
		memset(res, -1, QUE*MAX*sizeof(int));
		for (int i = 0; i < S; i++){
			if (i == query[0]) continue;
			res[0][i] = 0;
		}
		for (int i = 1; i < Q; i++){
			for (int j = 0; j < S; j++){
				if (j == query[i]) continue;
				int min = MANY;
				for (int k = 0; k < S; k++){
					if (k == query[i-1]) continue;
					if (k == j){
						if (min > res[i-1][k]){
							min = res[i-1][k];
						}
					} else {
						if (min > res[i-1][k] + 1){
							min = res[i-1][k] + 1;
						}
					}
				}
				res[i][j] = min;
			}
		}
		int min = MANY;
		for (int i = 0; i < S; i++){
			if (i == query[Q-1]) continue;
			if (res[Q-1][i] < min){
				min = res[Q-1][i];
			}
		}
		cout << "Case #" << po+1 << ": " << min << "\n";
	}
	return 0;
}