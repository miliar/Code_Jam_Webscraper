#include<cstdio>
#include<cstring>
using namespace std;

int T;
char x[501],a[20]={"welcome to code jam"};
int r[20][501],R;

void go()
{
int N=strlen(x);
int i,j,S=0;

for(i=0;i<N;i++)
	{
	r[0][i]=0;
	if(x[i]=='w')
		r[0][i]=1;
	}

for(i=1;i<=18;i++)
	{
	for(j=0;j<N;j++)
		r[i][j]=0;
	
	for(j=0;j<N;j++)
		{
		if(x[j]==a[i])
			r[i][j]=S;
		
		S=(S+r[i-1][j])%10000;
		}
	S=0;
	}

R=0;
for(int k=0;k<N;k++)
	R=(R+r[18][k])%10000;
}

void rd()
{
scanf("%d ",&T);
for(int i=1;i<=T;i++)
	{
	gets(x);
	
	go();
	printf("Case #%d: ",i);
	
	int r1=R,q=0;
	while(r1/=10)
		q++;
		
	while(q++<3)
		printf("0");
		
	printf("%d\n",R);
	}
}

int main()
{
freopen("input","r",stdin);
freopen("output","w",stdout);

rd();

return 0;
}
