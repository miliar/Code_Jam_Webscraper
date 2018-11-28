#include <iostream>
#include <cstring>
using namespace std;

int cs,l;
char a[10001];
char f[]="welcome to code jam";
int v[1000][1000];

void init()
{
	gets(a);
	while (a[0]==0) gets(a);
	l=strlen(a);
	memset(v,-1,sizeof(v));
}
int tongji(char * a,char * b,int x,int y)
{
	if (v[x][y]!=-1) return v[x][y];
	if (b[0]==0) 
	{
		v[x][y]=1;
		return 1;
	}
	int i,j;
	j=0;
	for (i=0;a[i]!=0;i++)
	{
		if (a[i]==b[0]) j+=tongji(a+i+1,b+1,x+i+1,y+1);
	}
	j=j%10000;
	v[x][y]=j;
	return j;
}
void make()
{
	int t=tongji(a,f,0,0);
	if (t<1000)
	{
		cout<<0;
		if (t<100)
		{
			cout<<0;
			if (t<10) cout<<0;
		}
	}
	cout<<t<<endl;
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>cs;
	int i;
	for (i=1;i<=cs;i++)
	{
		init();
		cout<<"Case #"<<i<<": ";
		make();
	}
	return 0;
}