#include <cstdio>
#include <cstring>
using namespace std;

const int maxn = 6000;
const int maxm = 30;
const int maxl = 20;

struct Node{
	int len;
	char c[maxm];
	char& operator[]( const int index) { return c[index]; }
};

Node pattern[maxl];
char dict[maxn][maxl];
int cases, L, D, N;

int get_num(){
	int i, j, k, ans = 0;
	bool match;
	for(i = 0; i < D; i++){
		for(j = 0; j < L; j++){
			match = false;
			for(k = 0; k < pattern[j].len; k++){
				if(dict[i][j] == pattern[j][k]){
					match  = true;
					break;
				}
			}
			if(!match) break;
		}
		if(j == L) ans++;
	}
	return ans;
}

void read_in_pattern(){
	int i, j, k;
	char c;
	for(i = 0; i < L; i++){
		pattern[i].len = 0;
		c = getchar();
		if(c == '('){
			while(true){
				c = getchar();
				if(c == ')') break;
				pattern[i][pattern[i].len++] = c;
			}
		}
		else{
			pattern[i].len = 1;
			pattern[i][0] = c;
		}
	}
	c = getchar();
}

int main(){
	int i, j, k;
	scanf("%d%d%d", &L, &D, &N);
	for(i = 0; i < D; i++){
		scanf("%s", &(dict[i]));
	}
	scanf("\n");
	for(i = 1; i <= N; i++){
		read_in_pattern();
		k = get_num();
		printf("Case #%d: %d\n", i, k);
	}
}
