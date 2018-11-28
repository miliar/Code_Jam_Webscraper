#include <cstdio>
#define MAXN 10

int n, m;
bool a[MAXN][MAXN];

int rez[MAXN][1<<MAXN];
int C[1<<MAXN];

bool can(int f, int t, int ROW){
	int X = t;
	bool x1[MAXN], x2[MAXN];
	for (int i = 0; i < m; i++){
		x1[i] = (f%2);
		x2[i] = (t%2);
		f /= 2;
		t /= 2;
	}
	for (int i = 0; i < m; i++) if (x2[i]){
		if (!a[ROW][i]) return false;
		if ((i!=0)&&(x1[i-1])) return false;
		if ((i!=0)&&(x2[i-1])) return false;
		if ((i!=m-1)&&(x1[i+1])) return false;
		if ((i!=m-1)&&(x2[i+1])) return false;
	}
	return true;
}

int getc(int i){
	if (i==0) return 0;
	if (i%2) return getc(i/2)+1; else return getc(i/2);
}

int main(){
	freopen("cheat.in", "rt", stdin);
	freopen("cheat.out", "wt", stdout);
	int T;
	for (int i = 0; i < (1<<MAXN); i++) C[i] = getc(i);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++){
		scanf("%d%d\n", &n, &m);
		for (int i = 0; i < n; i++){
			for (int j = 0; j < m; j++){
				char ch;
				scanf("%c", &ch);
				a[i][j] = (ch=='.');
			}
			scanf("\n");
		}
		for (int i = 0; i < MAXN; i++)
			for (int j = 0; j < (1<<MAXN); j++) rez[i][j] = 0;
		for (int i = 0; i < (1<<m); i++) if (can(0,i,0)) rez[0][i] = C[i];
		for (int j = 1; j < n; j++){
			for (int i = 0; i < (1<<m); i++)
				for (int p = 0; p < (1<<m); p++)
					if (can(p,i,j))
						rez[j][i] >?= rez[j-1][p]+C[i];
		}
		int ans = 0;
		for (int i = 0; i < n; i++) for (int j = 0; j < (1<<m); j++) ans >?= rez[i][j];
		printf("Case #%d: %d\n", t, ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
