#include<stdio.h>
#include<string.h>

const int maxn=1000000;

int n, q;
char eng[1010][110], query[1010][110];
bool valid[1010][1010];
int s[1010][1010];

void input()
{
	char str[10];
	int i;
	
	gets(str);
	sscanf(str, "%d", &n);
	for(i=0; i<n; i++) gets(eng[i]);
	
	gets(str);
	sscanf(str, "%d", &q);
	for(i=0; i<q; i++) gets(query[i]);
}

int find(char str[])
{
	int i;
	for(i=0; i<n; i++)
		if(strcmp(str, eng[i])==0) return i;
}

int solve()
{
	int i, j, min1, min2, ret;
	
	if(q==0) return 0;
	
	memset(valid, 0, sizeof(valid));
	for(i=0; i<q; i++){
		j=find(query[i]);
		valid[i][j]=1;
	}
	
	for(i=0; i<q; i++)
		for(j=0; j<n; j++) s[i][j]=maxn;
		
	for(i=0; i<n; i++)
		if(!valid[0][i]) s[0][i]=0;
	min1=0;
	
	for(i=1; i<q; i++){
		min2=maxn;
		for(j=0; j<n; j++)
			if(!valid[i][j]){
				if(s[i-1][j]<s[i][j]) s[i][j]=s[i-1][j];
				if(min1+1<s[i][j]) s[i][j]=min1+1;
				if(s[i][j]<min2) min2=s[i][j];
			}
		min1=min2;
	}
	
	ret=maxn;
	for(i=0; i<n; i++)
		if(s[q-1][i]<ret) ret=s[q-1][i];
		
	return ret;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int cc, ct, ans;
	char str[10];
	
	gets(str);
	sscanf(str, "%d", &cc);
	for(ct=1; ct<=cc; ct++){
		input();
		ans=solve();
		printf("Case #%d: %d\n", ct, ans);
	}
	
	return 0;
}
