#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
bool cmp(char s1[], char s2[]){
	return (strcmp(s1, s2) < 0);
}
char tmp[17];
void Swap(char s1[], char s2[]){
	strcpy(tmp, s1);
	strcpy(s1, s2);
	strcpy(s2, tmp);
}
int L, D, N;
char Word[5010][17];
char List[17][5010][17];
char st[1000], tp[17];
int ans;
void init(){
	scanf("%d%d%d", &L, &D, &N);
	for (int i = 0; i < D; i++) 
		scanf("%s", Word[i]);
	for (int i = 0; i < D; i++)
	for (int j = i+1; j< D; j++)
	if (strcmp(Word[i], Word[j]) > 0) 
		Swap(Word[i], Word[j]);
	for (int j = 0; j < L; j++)
	for (int i = 0; i < D; i++){
		strcpy(List[j][i], Word[i]);
		List[j][i][j+1] = '\0';	
	}
}
bool Find(int x){
	int flag, m, l = 0, r = D-1;
	while (l < r) {
		m = ((l + r) >> 1);
		flag = strcmp(List[x][m], tp);
		if (flag == 0) return true;
		if (flag < 0) l = m + 1;
		else r = m - 1;
	}
	return (strcmp(List[x][r], tp) == 0);
}
void dfs(int dep, int p){
	if (dep == L) {
		ans ++;
		return ;
	}
	int p0, p1;
	p0 = p;
	p1 = p+1;
	if (st[p++] == '('){ 
		p0 = p;
		while (st[p] != ')' && st[p] != '\0') p++;
		p1 = p;
		p++; 
	}
	
	for (int i = p0; i < p1; i++) {
		tp[dep] = st[i];
		tp[dep+1] = '\0';
		if (Find(dep))
			dfs(dep + 1, p);
	}
}
void solve(){
	tp[L] = '\0';
	for (int i = 1; i <= N; i++) {
		ans = 0;
		tp[0] = '\0';
		scanf("%s", st);
		dfs(0, 0);
		printf("Case #%d: %d\n", i, ans);
	}
	
}
int main(){
//	freopen("A-large.in","r", stdin);
	//freopen("A-large.out","w", stdout);
	init();
	solve();
//	while (1);
	return 0;
}
