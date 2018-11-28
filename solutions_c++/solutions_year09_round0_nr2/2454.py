#include <stdio.h>
#include <string.h>
const int size = 110;
const int Inf = 1000000000;
int parent[size];
int rank[size];
int w,h;
int buf[12][12];
bool state[12][12];
char ch[size];
char ans[12][12];
void makeSet(int i)
{
	parent[i] = i;
	rank[i] = 0;
	ch[i] = '-';
}
int findSet(int i)
{
	if(i != parent[i])
	{
		parent[i] = findSet(parent[i]);
	}
	return parent[i];
}
void link(int i,int j)
{
	if(i == j)
		return;
	if(rank[i] > rank[j])
		parent[j] = i;
	else
	{
		if(rank[i] == rank[j])
			rank[j]++;
		parent[i] = j;
	}
}
void unionSet(int i,int j)
{
	link(findSet(i),findSet(j));
}
inline int getIndex(int i,int j)
{
	return i*w+j;
}
inline bool check(int i,int j)
{
	if(i>=0 
		&& i<=h-1
		&& j>=0
		&& j<=w-1)
		return true;
	return false;
}
void search(int i,int j)
{
	int tmpi,tmpj;
	int min = Inf;
	if(check(i-1,j) && buf[i][j] > buf[i-1][j] && buf[i-1][j] <min)
	{
		min = buf[i-1][j];
		tmpi = i-1;
		tmpj = j;
	}
	if(check(i,j-1) && buf[i][j] > buf[i][j-1] && buf[i][j-1] <min)
	{
		min = buf[i][j-1];
		tmpi = i;
		tmpj = j-1;		
	}
	if(check(i,j+1) && buf[i][j] > buf[i][j+1] && buf[i][j+1] <min)
	{
		min = buf[i][j+1];
		tmpi = i;
		tmpj = j+1;
	}
	if(check(i+1,j) && buf[i][j] > buf[i+1][j] && buf[i+1][j] <min)
	{
		min = buf[i+1][j];
		tmpi = i+1;
		tmpj = j;
	}
	if(min!=Inf)
	{
		unionSet(getIndex(i,j),getIndex(tmpi,tmpj));
		if(state[tmpi][tmpj] == false)
		{
			state[tmpi][tmpj] = true;
			search(tmpi,tmpj);
		}
	}
}
int main()
{
	int n,i,j,k;
	char now;
	freopen("out.txt","w",stdout);
	scanf("%d",&n);
	for(int count=1;count<=n;count++)
	{
		scanf("%d%d",&h,&w);
		for(i=0;i<h*w;i++)
		{
			makeSet(i);
		}
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				state[i][j]=false;
				ans[i][j] = '-';
				scanf("%d",&buf[i][j]);
			}
		}
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				if(state[i][j] == false)
					search(i,j);
			}
		}
		now = 'a';
		for(i=0;i<h;i++)
		{
			for(j=0;j<w;j++)
			{
				k= findSet(getIndex(i,j));
				if(ch[k] == '-')
				{
					ch[k] = now++;					
				}
				ans[i][j] = ch[k];
			}
		}
		printf("Case #%d:\n",count);
		for(i=0;i<h;i++)
		{			
			printf("%c",ans[i][0]);
			for(j=1;j<w;j++)
			{
				printf(" %c",ans[i][j]);
			}
			printf("\n");
		}





	}
	return 0;
}