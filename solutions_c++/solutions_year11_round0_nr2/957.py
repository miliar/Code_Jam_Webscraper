#include <cstdio>
#include <vector>
using namespace std;

vector<char> V;
int cnt[128];
char C[128][128];
char O[128][128];
char Base[] = "QWERASDF";

void pop() {
    char x = V.back();
    cnt[x]--;
    V.pop_back();
}

void push(char ch) {
    if(V.empty()) {
	V.push_back(ch);
	cnt[ch]++;
	return;
    }
    char c = V.back();
    if(C[ch][c]) {
	pop();
	V.push_back(C[ch][c]);
	cnt[C[ch][c]]++;
	return;
    }
    for(int k = 0; k < 8; ++k) {
	if(cnt[Base[k]] && O[ch][Base[k]] == 1) {
	    for(char a = 'A'; a <= 'Z'; ++a) {
		cnt[a] = 0;
	    }
	    V.clear();
	    return;
	}
    }
    V.push_back(ch);
    cnt[ch]++;
}

void solve(int test) {
    printf("Case #%d: ", test);
    V.clear();
    for(char a = 'A'; a <= 'Z'; ++a) {
	cnt[a] = 0;
    }
    for(int i = 0; i < 8; ++i) {
	for(int j = 0; j < 8; ++j) {
	    C[Base[i]][Base[j]] = 0;
	    O[Base[i]][Base[j]] = 0;
	}
    }
    int comb;
    scanf("%d", &comb);
    char buf[111];
    for(int i = 0; i < comb; ++i) {
	scanf("%s", buf);
	C[buf[0]][buf[1]] = C[buf[1]][buf[0]] = buf[2];
    }
    int oppos;
    scanf("%d", &oppos);
    for(int i = 0; i < oppos; ++i) {
	scanf("%s", buf);
	O[buf[0]][buf[1]] = O[buf[1]][buf[0]] = 1;
    }
    int len;
    scanf("%d", &len);
    scanf("%s", buf);
    for(int i = 0; buf[i]; ++i) {
	push(buf[i]);
    }
    printf("[");
    for(int i = 0; i < V.size(); ++i) {
	if(i) printf(", ");
	printf("%c", V[i]);
    }
    printf("]\n");
}
    


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int i = 1; i <= t; ++i) {
	solve(i);
    }
    return 0;
}
