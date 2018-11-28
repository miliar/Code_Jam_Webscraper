#include<cstdio>
#include<memory>

char f_name[100];
int t;
int a[200][200];
char dec[200][200];
char c;
int n,m;
int d[4][2]={-1,0,0,-1,0,1,1,0};

bool out_of_range(int i,int j)
{
	return (i<0||j<0||i>=n||j>=m);
}

char find(int i,int j)
{
	int MIN=a[i][j];
	int MINk=-1;
	if(dec[i][j]) return dec[i][j];
	for(int k=0;k<4;k++)
	{
		if(out_of_range(i+d[k][0],j+d[k][1])) continue;
		if(MIN>a[i+d[k][0]][j+d[k][1]])
		{
			MIN=a[i+d[k][0]][j+d[k][1]];
			MINk=k;
		}
	}
	if(MINk==-1)
	{
		dec[i][j]=c++;
		return dec[i][j];
	}
	else
	{
		dec[i][j]=find(i+d[MINk][0],j+d[MINk][1]);
		return dec[i][j];
	}
}

void input()
{
	scanf("%d%d",&n,&m);
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			scanf("%d",&a[i][j]);
		}
	}
	c='a';
	memset(dec,0,sizeof(dec));
}

void process()
{
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			if(dec[i][j]==0)
			{
				find(i,j);
			}
		}
	}
}

void output()
{
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			printf("%c ",dec[i][j]);
		}
		printf("\n");
	}
}

int main()
{
	gets(f_name);
	freopen(f_name,"r",stdin);
	scanf("%d",&t);
	freopen("output.txt","w",stdout);
	for(int i=0;i<t;i++)
	{
		input();
		process();
		printf("Case #%d:\n",i+1);
		output();
	}
}