#include<stdio.h>
#include<string.h>

char str[5000][16], tar[512];
int L, D, N;

bool pp[15][26];
bool match(char str[]) {
	for(int i=0;i<L;i++)
		if(!pp[i][str[i]-'a'])
			return false;
	return true;
}

int matchcount(char pat[]) {
	memset(pp, false, sizeof(pp));
	int p=0;
	for(int i=0;pat[i];) {
		if(pat[i]=='(')
			for(i++;pat[i]!=')';i++)
				pp[p][pat[i]-'a']=true;
		else
			pp[p][pat[i]-'a']=true;
		i++; p++;
	}
	int cnt=0;
	for(int i=0;i<D;i++) cnt+=match(str[i]);
	return cnt;
}

int main() {
	scanf("%d%d%d\n", &L, &D, &N);
	for(int i=0;i<D;i++) gets(str[i]);

	for(int i=1;i<=N;i++)
		printf("Case #%d: %d\n", i, matchcount(gets(tar)));
}