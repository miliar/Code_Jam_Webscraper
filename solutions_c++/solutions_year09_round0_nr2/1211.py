#include<cstdio>
#include<queue>
using namespace std;

int n,m,a[102][102],T;
char c='a',R[102][102];
queue <int> I,J;

void fill(int i,int j)
{
int mn=a[i][j],ir,jr;

if(i>1&&a[i-1][j]<mn)
	mn=a[i-1][j],ir=i-1,jr=j;

if(j>1&&a[i][j-1]<mn)
	mn=a[i][j-1],ir=i,jr=j-1;
	
if(j<m&&a[i][j+1]<mn)
	mn=a[i][j+1],ir=i,jr=j+1;
	
if(i<n&&a[i+1][j]<mn)
	mn=a[i+1][j],ir=i+1,jr=j;
	
if(a[i][j]==mn) 
	{
	R[i][j]=c++;
	return;
	}
	
if(!R[ir][jr])
	fill(ir,jr);
	
R[i][j]=R[ir][jr];
}

/*
void fill2(int is,int js,char c)
{
I.push(is);
J.push(js);
R[is][js]=c;

while(!I.empty())
	{
	int i=I.front(),j=J.front();
	I.pop();
	J.pop();
	
	if(i>1&&!R[i-1][j]&&ok(i-1,j,i,j))
		{
		R[i-1][j]=c;
		I.push(i-1);
		J.push(j);
		}
		
	if(j>1&&!R[i][j-1]&&ok(i,j-1,i,j))
		{
		R[i][j-1]=c;
		I.push(i);
		J.push(j-1);
		}
		
	if(i<n&&!R[i+1][j]&&ok(i+1,j,i,j))
		{
		R[i+1][j]=c;
		I.push(i+1);
		J.push(j);
		}
		
	if(j<m&&!R[i][j+1]&&ok(i,j+1,i,j))
		{
		R[i+1][j]=c;
		I.push(i+1);
		J.push(j);
		}
	}
}*/

void go()
{
for(int i=1;i<=n;i++)
	for(int j=1;j<=m;j++)
		if(!R[i][j])
			fill(i,j);
}

void af(int t)
{
printf("Case #%d:\n",t);

for(int i=1;i<=n;i++)
	{
	printf("%c",R[i][1]);
	for(int j=2;j<=m;j++)
		printf(" %c",R[i][j]);
		
	printf("\n");
	}
}

void rd()
{
scanf("%d",&T);

for(int t=1;t<=T;t++)
	{
	scanf("%d%d",&n,&m);
	
	for(int i=1;i<=n;i++)
		for(int j=1;j<=m;j++)
			scanf("%d",&a[i][j]),R[i][j]=0;
	
	c='a';
	go();
	af(t);
	}
}

int main()
{
freopen("input","r",stdin);
freopen("output","w",stdout);

rd();

return 0;
}
