/*
language: c++
author: Suvin
problem A
*/

#include<stdio.h>
#include<string.h>
#define MAXL 30
#define MAXD 5050

char word[MAXD][MAXL], pat[600];
bool flag[MAXL][26];

int main()
{
	int i, j, L, D, N, cnt, len, k;
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	scanf("%d %d %d", &L, &D, &N);
	for(i=0; i<D; i++)
		scanf("%s", word[i]);
	
	for(i=1; i<=N; i++){
		scanf("%s", pat);
		len = strlen(pat);
		
		memset(flag, false, sizeof(flag));
			
		for(j=k=0; j<len; j++){
			if(pat[j]=='('){
				j++;
				while(pat[j]!=')') {flag[k][pat[j]-'a'] = true; j++;}
				k++;
			}
			else 
				flag[k++][pat[j]-'a'] = true;
		}
		
		for(j=cnt=0; j<D; j++){
			for(k=0; k<L; k++)
				if(!flag[k][word[j][k]-'a']) break;
			if(k==L) cnt++;
		}
		printf("Case #%d: %d\n", i, cnt);
	}
	
	return 0;
}


