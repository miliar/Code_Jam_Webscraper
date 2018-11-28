#include<cstdio>
#include<string.h>
#define max(a,b) (a>b?a:b)
using namespace std;

int T,n;
char x[100],v[1000];
unsigned long long y;

void baza(int a,int b)
{
y=0;
unsigned long long bz=1;
for(int i=n-1;i>=0;i--)
	{
	y+=(x[i]-'0')*bz;
	bz*=a;
	}
}

void go()
{
for(int i=0;i<=300;i++)
	v[i]=0;
char nx='1';

v[int(x[0])]=x[0]='1';

for(int i=1;i<n;i++)
	if(v[int(x[i])])
		x[i]=v[int(x[i])];
	else
		{
		if(nx=='1') v[int(x[i])]=x[i]='0';
		else v[int(x[i])]=x[i]=nx;
		nx++;
		}
		
baza(max(2,nx-'0'),10);
}

void rd()
{
scanf("%d",&T);

for(int i=1;i<=T;i++)
	{
	scanf("%s",x);
	n=strlen(x);
	
	go();
	printf("Case #%d: %lld\n",i,y);	
	}
}

int main()
{
freopen("input","r",stdin);
freopen("output","w",stdout);

rd();

return 0;
}
