#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
using namespace std;

const int MAXN = 256;
const int INF = 1012345678;

map <char, vector <char> > mm;
int n, k, indegree[MAXN], outdegree[MAXN];
bool mat[MAXN][MAXN];
char token[1024];

void init() {
	for (char ch = 'a'; ch <= 'z'; ch++) {
		mm[ch].push_back(ch);
	}
	mm['o'].push_back('0');
	mm['i'].push_back('1');
	mm['e'].push_back('3');
	mm['a'].push_back('4');
	mm['s'].push_back('5');
	mm['t'].push_back('7');
	mm['b'].push_back('8');
	mm['g'].push_back('9');
}

int main() {
	init();
	int taskNumber;
	scanf("%d", &taskNumber);
	for (int taskIdx = 0; taskIdx < taskNumber; taskIdx++) {
		scanf("%d%s", &k, token);
		n = strlen(token);
		memset(mat, 0, sizeof(mat));
		for (int i = 1; i < n; i++) {
			for (vector <char>::const_iterator it = mm[token[i - 1]].begin(); it != mm[token[i - 1]].end(); it++) {
				for (vector <char>::const_iterator jt = mm[token[i]].begin(); jt != mm[token[i]].end(); jt++) {
					mat[*it][*jt] = true;
				}
			}
		}
		int res1 = 1;
		memset(indegree, 0, sizeof(indegree));
		memset(outdegree, 0, sizeof(outdegree));
		for (int i = 0; i < MAXN; i++) {
			for (int j = 0; j < MAXN; j++) {
				res1 += mat[i][j];
				outdegree[i] += mat[i][j];
				indegree[i] += mat[j][i];
			}
		}
		int res2 = 0;
		for (int i = 0; i < MAXN; i++) {
			res2 += abs(indegree[i] - outdegree[i]);
		}
if (res2 & 1) puts("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
		res2 >>= 1;
		for (int i = 0; i < MAXN; i++) {
			if (indegree[i] + outdegree[i] == 0) continue;
			for (int j = 0; j < MAXN; j++) {
				if (i == j || indegree[j] + outdegree[j] == 0) continue;
				int sum = 0;
				for (int k = 0; k < MAXN; k++) {
					if (i == k) {
						sum += abs(1 - outdegree[k] + indegree[k]);
					} else if (j == k) {
						sum += abs(1 - indegree[k] + outdegree[k]);
					} else {
						sum += abs(indegree[k] - outdegree[k]);
					}
				}
if (sum & 1) puts("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
				res2 = min(res2, sum >> 1);
			}
		}
		printf("Case #%d: %d\n", taskIdx + 1, res1 + res2);
	}
	return 0;
}
