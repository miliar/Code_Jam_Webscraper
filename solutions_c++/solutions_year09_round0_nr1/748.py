#include <cstdio>
#include <cstring>
using namespace std;
int L,D,N,M;
int F[75001][26];
char str[1000];

bool let(char s)
{
	if(s>='a' && s<='z') return 1;
	return 0;
}

void add_to_bor(int s,int i)
{
	if(i>=L) return;
	int k=str[i]-'a';
	if(F[s][k]==-1)
	{
		F[s][k]=M;
		M++;
	}
	add_to_bor(F[s][k],i+1);
}

int solve(int s,int i,int c)
{
	if(c>=L) 
		return 1;
	int k;
	if(let(str[i]))
	{
		k=str[i]-'a';
		if(F[s][k]>=0)
			return solve(F[s][k],i+1,c+1);
		return 0;
	}
	i++;
	int res=0,st=i,ft;
	while(str[i]!=')') i++;
	ft=i+1;
	i=st;
	while(str[i]!=')')
	{
		k=str[i]-'a';
		if(F[s][k]>=0)
			res+=solve(F[s][k],ft,c+1);
		i++;
	}
	return res;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,K=0;
	scanf("%d%d%d",&L,&D,&N);
	for(i=0;i<75001;i++) 
		for(j=0;j<26;j++)
			F[i][j]=-1;
	M=1;
	for(i=0;i<D;i++)
	{
		scanf("%s",str);
		add_to_bor(0,0);
	}
	for(i=0;i<N;i++)
	{
		scanf("%s",str);
		printf("Case #%d: %d\n",i+1,solve(0,0,0));
	}
	return 0;
}