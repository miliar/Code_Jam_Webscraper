#include <iostream>
#include <algorithm>
using namespace std;

const int fx[5]={0,1,0,0,-1};
const int fy[5]={0,0,1,-1,0};

int cs;
int n,m,tot;
int a[501][501];
int map[501][501];
struct point
{
	int x,y;
}data[20001],dl[20001];

void init()
{
	cin>>n>>m;
	tot=0;
	int i,j,k=1;
	for (i=1;i<=n;i++)
		for (j=1;j<=m;j++) 
		{
			cin>>a[i][j];
			data[k].x=i;
			data[k].y=j;
			k++;
		}
	memset(map,0,sizeof(map));
}

int cmp(const void * p1,const void * p2)
{
	const point * a1,* a2;
	a1=(const point * ) p1;
	a2=(const point * ) p2;
	return a[a2->x][a2->y]-a[a1->x][a1->y];
}

bool out(point & p)
{
	if (p.x<=0 || p.x>n || p.y<=0 || p.y>m) return true;
	return false;
}

void chl(point & loc)
{
	point p,q,u;
	int top=1;
	dl[top]=loc;
	int i,h;
	while (true)
	{
		p=dl[top];
		h=a[p.x][p.y]-1;
		u.x=0;
		u.y=0;
		for(i=1;i<=4;i++)
		{
			q.x=p.x+fx[i];
			q.y=p.y+fy[i];
			if (!out(q) && (a[q.x][q.y]<=h))
			{
				h=a[q.x][q.y];
				u=q;
			}
		}
		if (u.x==0 && u.y==0) break;
		top++;
		dl[top]=u;
	}
	p=dl[top];
	if (map[p.x][p.y]==0)
	{
		tot++;
		map[p.x][p.y]=tot;
	}
	h=map[p.x][p.y];
	for (i=1;i<top;i++)
	{
		p=dl[i];
		map[p.x][p.y]=h;
	}
}

void make()
{
	int i,j;
	for (i=1;i<=n*m;i++)
	{
		if(map[data[i].x][data[i].y]==0)
			chl(data[i]);
	}
	char c='a';
	char jl[30];
	memset(jl,0,sizeof(jl));
	for (i=1;i<=n;i++)
	{
		for (j=1;j<=m;j++)
		{
			if (jl[map[i][j]]==0)
			{
				jl[map[i][j]]=c;
				c++;
			}
			cout<<jl[map[i][j]]<<' ';
		}
		cout<<endl;
	}
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>cs;
	int i;
	for(i=1;i<=cs;i++)
	{
		init();
		qsort(data+1,n*m,sizeof(point),cmp);
		cout<<"Case #"<<i<<":"<<endl;
		make();
	}

	return  0;
}