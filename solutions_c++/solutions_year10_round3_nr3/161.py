#include<stdio.h>
#include<string.h>

int my[1000];
int set[1000][1000];
int n,m;
int ans=0;

void get(char s[],int x)
{
	int i;
	int k;
	for(i=0;i<m;i++)
	{
		if(s[i]>='0'&&s[i]<='9')
		{
			k=s[i]-'0';
		}
		else if(s[i]=='A')
		{
			k=10;
		}
		else if(s[i]=='B')
		{
			k=11;
		}
		else if(s[i]=='C')
		{
			k=12;
		}
		else if(s[i]=='D')
		{
			k=13;
		}
		else if(s[i]=='E')
		{
			k=14;
		}
		else if(s[i]=='F')
		{
			k=15;
		}
		int pp=8;
		for(int j=0;j<4;j++)
		{
			set[x][4*i+j]=k/pp;
			k%=pp;
			pp/=2;
		}
	}
	return ;
}

bool check(int w,int x,int y,int z)
{
	int i,j;
	if(w>1)
	{
		for(i=x;i<x+w;i++)
		{
			for(j=y;j<=z;j++)
			{
				if(set[i][j]==-1)
				{
					return false;
				}
				if(i>x&&set[i-1][j]!=-1)
				{
					if((set[i][j]^set[i-1][j])==0)
					{
						return false;
					}
				}
				if(j>y&&set[i][j-1]!=-1)
				{
					if((set[i][j]^set[i][j-1])==0)
					{
						return false;
					}
				}
				if(i<x+w-1&&set[i+1][j]!=-1)
				{
					if((set[i][j]^set[i+1][j])==0)
					{
						return false;
					}
				}
				if(j<z&&set[i][j+1]!=-1)
				{
					if((set[i][j]^set[i][j+1])==0)
					{
						return false;
					}

				}
			}
		}
		for(i=x;i<x+w;i++)
		{
			for(j=y;j<=z;j++)
			{
				set[i][j]=-1;
			}
		}
	}
	else
	{
		if(set[x][y]==-1)
		{
			return false;
		}
		set[x][y]=-1;
	}
	return true;
}

void search()
{
	int i,j,p,k;
	int len=n<m?n:m;
	for(k=len;k>=1;k--)
	{
		for(i=0;i<n;i++)
		{
			if(i+k-1<n)
			{
				for(j=0;j<m;j++)
				{
					p=j+k-1;
					if(p<m)
					{
						if(check(k,i,j,p))
						{
							my[k]++;
						}
					}
				}
			}
		}
		if(my[k])
		{
			ans++;
		}
	}
	return ;
}
				

int main(void)
{
	int tt;
	int yy=0;
	freopen("C-small-attempt1 (1).in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&tt);
	while(tt--)
	{
		yy++;
		char s[1000];
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
		{
			scanf("%s",s);
			get(s,i);
		}
		memset(my,0,sizeof(my));
		ans=0;
		search();
		int i=n<m?n:m;
		printf("Case #%d: %d\n",yy,ans);
		for(;i>=1;i--)
		{
			if(my[i]>0)
			{
				printf("%d %d\n",i,my[i]);
			}
		}
	}
	return 0;
}