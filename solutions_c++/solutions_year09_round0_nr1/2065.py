#include "iostream"
#include "string"
#include "cstring"
#include "algorithm"
#define N 5001
#define M 20
#define K 501
using namespace std;
char word[N][M];
bool msg[K][M][30];
int l,d,n;
void init()
{
	int i,j,k;
	char s[M*30];
	bool flag;
	memset(msg,false,sizeof(msg));
	for(i=0;i<d;i++)
		scanf("%s",word[i]);
	for(i=0;i<n;i++)
	{
		scanf("%s",s);
		for(j=0,k=0,flag=false;s[j];j++)
		{
			if(s[j]=='(')
			{
				flag=true;
			}
			else if(s[j]==')')
			{
				k++;
				flag=false;
			}
			else
			{
				if(flag)
					msg[i][k][s[j]-'a']=true;
				else
					msg[i][k++][s[j]-'a']=true;
			}
		}
	}
}
bool check(int x,int y)
{
	int i;
	for(i=0;i<l;i++)
	{
		if(!msg[x][i][word[y][i]-'a'])
			return false;
	}
	return true;
}
void solve()
{
	int i,j,cnt;
	for(i=0;i<n;i++)
	{
		cnt=0;
		for(j=0;j<d;j++)
		{
			if(check(i,j))
				++cnt;
		}
		printf("Case #%d: %d\n",i+1,cnt);
	}
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d%d%d",&l,&d,&n);
	init();
	solve();
	return 0;
}