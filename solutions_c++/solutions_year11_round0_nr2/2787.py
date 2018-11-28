#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int a[255][255],am[255][255];
char mp[255][255];
char A[105];
int N, n_case=0;
int check(char ch){
	switch(ch){
		case 'Q':
		case 'W':
		case 'E':
		case 'R':
		case 'A':
		case 'S':
		case 'D':
		case 'F': return 1;
		default: return 0;	
	}
}
int search(int top){
	
}
char stack[105];
int cnt;
int canin(int cnt, char ch){
	if(cnt == 0) return 1;
	if(am[stack[cnt]][ch]) return 0;
	for(int i = cnt; i >= 1; i--){
		if(a[stack[i]][ch]) return 0;	
	}
	return 1;
}
void solve(){
	cnt = 0;
	stack[++cnt] = A[0];
	for(int i = 1; i < N; i++){
		if(canin(cnt, A[i])){
			stack[++cnt] = A[i];
		} else {
			if(cnt >= 1 && am[stack[cnt]][A[i]]){
				cnt--;
				stack[++cnt] = mp[stack[cnt]][A[i]];
			} else if(cnt>=1){
				int np = cnt;
				for(; np >= 1; np--){
					if(a[stack[np]][A[i]]) break;
				}
				if(np >= 1) cnt = 0;
			}
		}
	}
	//printf("cnt = %d\n", cnt);
	printf("Case #%d: [",++n_case);
	for(int i = 1; i<= cnt; i++){
		if(i != 1) printf(", ");
		printf("%c", stack[i]);	
	}
	printf("]\n");
}
void input(){
	memset(a, 0, sizeof(a));
	memset(mp, 0, sizeof(mp));
	memset(am, 0, sizeof(am));
	int n;
	scanf("%d", &n);
	char str[20];
	for(int i = 0; i < n; i++){	
		scanf("%s", str);//printf("%s ", str);
		mp[str[0]][str[1]] = str[2];
		mp[str[1]][str[0]] = str[2];
		am[str[0]][str[1]] = 1;
		am[str[1]][str[0]] = 1;
	}
	//printf("\n");
	scanf("%d", &n);
	for(int i = 0; i < n; i++){
		scanf("%s", str);//printf("%s ", str);
		a[str[0]][str[1]] = 1;
		a[str[1]][str[0]] = 1;
	}
	//printf("\n");
	scanf("%d", &N);
	scanf("%s", A);
}
int main(){
	//freopen("test.in", "r", stdin);
	//freopen("test.out", "w", stdout);
	//freopen("B-small-attempt1.in", "r", stdin);
	//freopen("B-small-attempt1.out", "w", stdout);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int C;
	scanf("%d", &C);
	for(int i = 1; i <= C; i++){
		input();
		solve();
		//return 0;
	}
}
