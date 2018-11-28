#include <cstdio>
#include <cstring>
using namespace std;
const int maxl=15,maxd=5001;
char dic[maxd][maxl+1];
int l,d,n;
void init()
{
	scanf("%d%d%d",&l,&d,&n);
	for(int i=0;i<d;i++) scanf("%s",dic[i]);
}
int solve()
{
	static char s[10240];
	scanf("%s",s);
	static bool u[maxl][26];
	memset(u,0,sizeof(u));
	int i=0;
	for(char *p=s;*p;p++)
	{
		if(*p=='(')
		{
			while(*++p!=')') u[i][*p-'a']=true;
			i++;
		}
		else
		{
			u[i][*p-'a']=true;
			i++;
		}
	}
	int ans=0;
	for(int i=0;i<d;i++)
	{
		bool flag=true;
		for(int j=0;j<l;j++)
			if(!u[j][dic[i][j]-'a'])
			{
				//printf("out %d %d\n",i,j);
				flag=false;
				break;
			}
		if(flag) ans++;
	}
	return ans;
}
int main()
{
	init();
	for(int i=1;i<=n;i++)
		printf("Case #%d: %d\n",i,solve());
	return 0;
}
