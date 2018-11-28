#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;
const int MAXS=110;
const int MAXQ=1100;
const int MAXLEN=110;
const int MO=1293747;
const int oo=2000000000;
int id[MO];
int s,q;
int b[MAXQ];
char str[MAXLEN];
int cnt;
int getID()
{
	gets(str);
	char* pt=str;
	int h=0;
	while(*pt)
	{
		h=(h*128+*pt)%MO;
		pt++;
	}
	if(!id[h])id[h]=++cnt;
	return id[h];
}
void init()
{
	memset(id,0,sizeof(id));
	cnt=0;
	scanf("%d",&s);gets(str);
	for(int i=1;i<=s;i++)getID();
	scanf("%d",&q);gets(str);
	for(int i=1;i<=q;i++)
		b[i]=getID();
}
int f[MAXQ][MAXS];
inline int min(int a,int b){return a<b?a:b;};
void work()
{
	int mn=0;
	for(int i=1;i<=q;i++)
	{
		int mn2=oo;
		for(int j=1;j<=s;j++)
		{
			if(j==b[i])
			{
				f[i][j]=oo;
				continue;
			}
			if(i==1)f[i][j]=0;
			else
			{
				f[i][j]=min(f[i-1][j],mn+1);
			}
			if(f[i][j]<mn2)mn2=f[i][j];
		}
		mn=mn2;
	}
	printf("%d\n",mn);
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int cases;
	scanf("%d",&cases);gets(str);
	int t=0;
	while(cases--)
	{
		t++;
		printf("Case #%d: ",t);
		init();
		work();
	}
}
