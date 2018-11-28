#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define N 11000
#define L 12
char word[N][L];
int hash[N][26];
int deep[N];
int cmpvalue;
int and = (1<<10) - 1;
int cmp(const void *a, const void *b){
	int ia = *(int *)a, ib = *(int *)b;
	if(hash[ia][cmpvalue] - hash[ib][cmpvalue])
		return hash[ia][cmpvalue] - hash[ib][cmpvalue];
	else
		return ia - ib;
}
int slove(int a[], int n, char *w, int d){
	int i, j;
	cmpvalue = (*w) - 'a';
	for(i=0; i<n; i++)
		if(hash[a[i]][cmpvalue] & and)
			break;
	if(i==n)
		return slove(a, n, w+1, d);
	qsort(a, n, sizeof(a[0]), cmp);
	i=0;
	while(i<n){
		j=i;
		while(j<n && hash[a[j]][cmpvalue]==hash[a[i]][cmpvalue])
			j++;
		if(j!=i+1){
			if(hash[a[i]][cmpvalue] & and){
				slove(&a[i], j-i, w+1, d);
			}
			else{
				slove(&a[i], j-i, w+1, d+1);
			}
			cmpvalue = (*w) - 'a';
		}
		else{
			if(hash[a[i]][cmpvalue] & and)
				deep[a[i]] = d;
			else
				deep[a[i]] = d+1;
		}
		i = j;
	}
	return 0;
}

int sslove(int a[], int n, char *w, int d){
	cmpvalue = 0;
	qsort(a, n, sizeof(a[0]), cmp);
	int i, j;
	i = 0;
	int ans = 0;
	while(i<n){
		j = i;
		while(j<n && (hash[a[i]][0]>>10) == (hash[a[j]][0]>>10))
			j ++;
		slove(&a[i], j-i, w, d);
		i = j;
	}
	for(i=0; i<n; i++)
		if(deep[i] > deep[ans])
			ans = i;
	return ans;
}
int main(){
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int a[N];
	char w[30];
	int test;
	int n, m, len;
	scanf("%d", &test);
	for(int t=1; t<=test; t++){
		scanf("%d %d", &n, &m);
		for(int i=0; i<n; i++)
			scanf("%s", word[i]);
		printf("Case #%d:", t);
		memset(hash, 0, sizeof(hash));
		for(int i=0; i<n; i++){
			len = strlen(word[i]);
			for(int j=0; j<26; j++)
				hash[i][j] = len<<10;
			for(int j=0; j<len; j++)
				hash[i][word[i][j]-'a'] |= 1<<j;
		}
		for(int i=0; i<m; i++){
			for(int j=0; j<n; j++)
				a[j] = j;
			memset(deep, 0xff, sizeof(deep));
			scanf("%s", w);
			printf(" %s", word[sslove(a, n, w, 0)]);
		}
		printf("\n");
	}
	return 0;
}