#include<iostream>
#include<algorithm>
using namespace std;
const int MAX=60;

int N,K;
char s[MAX][MAX],t[MAX][MAX];
void change()
{
	int i,j;
	for(i=1;i<=N;i++)
	{
		for(j=1;j<=N;j++) t[j][N-i+1]=s[i][j];
	}

	for(j=1;j<=N;j++)
	{
		for(i=N;i>=1;i--)
		{
			if(t[i][j]!='.')
			{
				int k=i+1;
				while(k<=N&&t[k][j]=='.')
				{
					char ch=t[k][j];
					t[k][j]=t[k-1][j];
					t[k-1][j]=ch;
					k++;
				}
			}
		}
	}
}
bool gs1(int x,int y,char ch)
{
	if(y+K-1>N) return 0;
	int j,cnt=1;
	for(j=y+1;j<=N&&t[x][j]==ch;j++) cnt++;

	return cnt>=K;
}
bool gs2(int x,int y,char ch)
{
	if(x+K-1>N) return 0;
	int i,cnt=1;
	for(i=x+1;i<=N&&t[i][y]==ch;i++) cnt++;
	return cnt>=K;
}
bool gs3(int x,int y,char ch)
{
	if(x+K-1>N||y+K-1>N) return 0;
	int i,j,cnt=1;
	for(i=x+1,j=y+1;i<=N&&j<=N&&t[i][j]==ch;i++,j++) cnt++;
	
	return cnt>=K;
}
bool gs4(int x,int y,char ch)
{
	if(x+K-1>N||y<K) return 0;
	int i,j,cnt=1;
	for(i=x+1,j=y-1;i<=N&&j<=N&&t[i][j]==ch;i++,j--) cnt++;
	
	return cnt>=K;
}
bool ok(char ch)
{
	int i,j;
	for(i=1;i<=N;i++)
	{
		for(j=1;j<=N;j++)
		{
			if(t[i][j]==ch)
			{
				if(gs1(i,j,ch)||gs2(i,j,ch)||gs3(i,j,ch)||gs4(i,j,ch)) return 1;
			}
		}
	}
	return 0;
}
int main()
{
	freopen("F:\\A-small-attempt1.in","r",stdin);
	freopen("F:\\A-small-attempt1.out","w",stdout);
	int i,j,T;scanf("%d",&T);
	int CN=0;
	while(T--)
	{
		scanf("%d%d",&N,&K);
		for(i=1;i<=N;i++) scanf("%s",s[i]+1);
		change();
		bool f1=ok('B');
		bool f2=ok('R');
		printf("Case #%d: ",++CN);
		if(f1&&f2) puts("Both");
		else if(f1) puts("Blue");
		else if(f2) puts("Red");
		else puts("Neither");
	}
	//system("pause");
	return 0;
}
