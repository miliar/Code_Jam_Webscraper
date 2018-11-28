#include <iostream>
#include <string.h>
#include <stdio.h>
using namespace std;

const int SZ = 750000;
char arr[20][26];
char t[10000];
int num[20];
int next[SZ][26], tot;
int cnt[SZ];
int L, D, N, ans;

void insert(char * words) 
{
	int cur = 0;
	for(int pos = 0; words[pos]; pos++){
		int dt = words[pos] - 'a';
		if(next[cur][dt] == -1){
			next[cur][dt] = ++tot;
		}
		cur = next[cur][dt];
	}
	cnt[cur]++;
}

void dfs(int cur, int i, int deep)
{
	if(deep == L){
		ans += cnt[cur];
		return ;
	}
	for(int j = 0; j < num[i]; j++){
		int dt = arr[i][j] - 'a';
		if(next[cur][dt] != -1){
			dfs(next[cur][dt], i + 1, deep + 1);
		}
	}
}

int main()
{
	char words[20];
	memset(next, -1, sizeof(next));
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d%d%d", &L, &D, &N);
	while(D--){
		scanf("%s", words);
		insert(words);
	}
	for(int i = 1; i <= N; i++){
		int k = 0, pos = 0;
		scanf("%s", t);
		while(t[pos]){
			if(t[pos] == '('){
				num[k] = 0, pos++;
				while(t[pos] != ')'){
					arr[k][num[k]++] = t[pos++];
				}
				pos++, k++;
			}
			else {
				num[k] = 1;
				arr[k++][0] = t[pos++];
			}
		}
		ans = 0;
		dfs(0, 0, 0);
		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}



		

		




