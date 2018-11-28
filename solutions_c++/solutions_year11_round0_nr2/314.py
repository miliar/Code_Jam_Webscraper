#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std; 

const int maxn = 200;

int oppo[maxn][maxn];
int comb[maxn][maxn];
int targ[maxn][maxn];
int cid; 

int iList[maxn];
int oList[maxn];

int T; 
int N; 
int top;

inline int ctoint(char c){
	return (int)(c -'A');
}

inline char inttoc(int a){
	return (char) (a + 'A');
}

void input(){
	int combN, oppoN; 
	scanf("%ld", &combN);
	for (int i = 0; i < combN; i++) {
		char ca, cb, cc;
		int a, b, c; 
		scanf(" %c%c%c", &ca, &cb, &cc);
		//printf("%c%c%c", ca, cb, cc); 
		a = ctoint(ca); b = ctoint(cb); c = ctoint(cc); 
		comb[a][b] = comb[b][a] = cid; 
		targ[a][b] = targ[b][a] = c; 
	}
	//printf(" fistpartover");
	scanf("%ld", &oppoN);
	for (int i = 0; i < oppoN; i++) {
		char ca, cb;
		int a, b; 
		scanf(" %c%c", &ca, &cb);
		//printf("%c%c", ca, cb); 
		a = ctoint(ca); b = ctoint(cb); 
		oppo[a][b] = oppo[b][a] = cid; 
	}
	//printf(" secondpartover");
	scanf("%ld", &N); 
	for(int i = 0; i < N; i++) {
		char c; 
		scanf(" %c", &c);
		//printf("%c", c); 
		iList[i] = ctoint(c);
	}
	//printf(" thirdpartover");
}

void work(){
	top = 0; 
	for (int i = 0; i < N; i++) {
		int cur = iList[i]; 
		if (top == 0) {
			oList[top++] = cur; 
			continue; 
		}
		int prev = oList[top - 1]; 
		if (comb[cur][prev] == cid){
			oList[top - 1] = targ[cur][prev];
			continue; 
		}
		for (int j = 0; j < top; j++) {
			prev = oList[j];
			if (oppo[prev][cur] == cid){
				top = 0;
				break; 
			}
		}
		if (top != 0) oList[top++] = cur; 
	}
}

void output(){
	printf("Case #%ld: [", cid);
	for (int i = 0; i < top-1; i++) {
		printf("%c, ", inttoc(oList[i]));
	}
	if (top > 0) printf("%c", inttoc(oList[top - 1]));
	printf("]\n");
}

int main(){
	//freopen("E:\\Algorithms\\GoogleJam\\GoogleJam\\input\\B-large.in", "r", stdin);
	//freopen("E:\\Algorithms\\GoogleJam\\GoogleJam\\input\\B-large.out", "w", stdout);
	scanf("%ld", &T); 
	memset(oppo, 255, sizeof(oppo)); 
	memset(comb, 255, sizeof(comb));
	for (cid = 1; cid <= T; cid++){
		input();
		work(); 
		output();
	}
	//fclose(stdout);
}