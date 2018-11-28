#include <stdio.h>
#include <cstring>
#include <set>
#include <iostream>
#include <algorithm>

using namespace std;

int testnum, n, k;
bool can[128][128];
int dat[128][32];
int m1[128], m2[128];

const int MAXN = 128;
#define _clr(x) memset(x, 0xff, sizeof(int) * MAXN)
int hungary(int m, int n, const bool mat[][MAXN], int * match1, int * match2) {
	int s[MAXN + 1], t[MAXN], p, q, ret = 0, i, j, k;
	_clr(match1);
	_clr(match2);
	for (i = 0; i < m; ret += (match1[i++] >= 0)) {
		_clr(t);
		for (s[p = q = 0] = i; p <= q && match1[i] < 0; p++) {
			k = s[p];
			for (j = 0; j < n && match1[i] < 0; j++) {
				if (mat[k][j] && t[j] < 0) {
					s[++q] = match2[j];
					t[j] = k;
					if (s[q] < 0) {
						for (p = j; p >= 0; j = p) {
							match2[j] = k = t[j];
							p = match1[k];
							match1[k] = j;
						}
					}
				}
			}
		}
	}
	return ret;
}

bool inter(int a, int b){
	if(dat[a][0] == dat[b][0]) return true;
	for(int i = 1;i < k;i++){
		if((dat[a][i - 1] <= dat[b][i - 1] && dat[a][i] >= dat[b][i]) || 
				(dat[a][i - 1] >= dat[b][i - 1] && dat[a][i] <= dat[b][i]))
		return true;
		if(dat[a][i] == dat[b][i]) return true;
	}
	return false;
}

bool used[128];

int find(){
	for(int i = 0;i < n;i++)
	if(!used[i])
	return i;
	return -1;
}

int main(){
	scanf("%d", &testnum);
	for(int test = 1;test <= testnum;test++){
		scanf("%d%d", &n, &k);
		for(int i = 0;i < n;i++){
			for(int j = 0;j < k;j++){
				scanf("%d", &dat[i][j]);
			}
		}
		memset(can, false, sizeof(can));
		bool flag;
		for(int i = 0;i < n;i++){
			for(int j = 0;j < n;j++){
				flag = true;
				for(int l = 0;l < k;l++)
					if(dat[i][l] >= dat[j][l]){
						flag = false;
						break;
					}
				can[i][j] = flag;
			}
		}
		/*for(int i = 0;i < n;i++){
			for(int j = i + 1;j < n;j++){
				can[i][j] = can[j][i] = !inter(i, j);
			}
			can[i][i] = false;
		}
		int ret = 0;
		memset(used, false, sizeof(used));
		set <int> se;
		set <int> :: iterator it;
		bool suc;
		int tmp;
		while((tmp = find()) >= 0){
			se.clear();
			se.insert(tmp);
			used[tmp] = true;
			for(int i = tmp + 1;i < n;i++) if(!used[i]){
				suc = true;
				for(it = se.begin();it != se.end();it++){
					if(!can[i][*it]){
						suc = false;
						break;
					}
				}
				if(suc){
					se.insert(i);
					used[i] = true;
				}
			}
			ret++;
		}*/
		int ret = hungary(n, n, can, m1, m2);
		printf("Case #%d: %d\n", test, n - ret);
	}
	return 0;
}
