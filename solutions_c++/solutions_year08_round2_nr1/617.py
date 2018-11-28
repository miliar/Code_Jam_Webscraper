#include <cstdio>
#include <vector>

using namespace std;

int nt;
long long n,A,B,C,D,x0,y0,M;

struct point
{
	long long x,y;
};

vector <point> p;

bool isit(point a,point b,point c)
{
	if((a.x+b.x+c.x)%3==0&&(a.y+b.y+c.y)%3==0) return 1;
	return 0;
}

//bool isz(point a,point b,point c)
//{
//	if(a.x*(b.y-c.y)+b.x*(c.y-a.y)+c.x*(a.y-b.y)==0) return 0;
//	return 1;
//}

void read()
{
	scanf("%d %d %d %d %d %d %d %d",&n,&A,&B,&C,&D,&x0,&y0,&M);
	p.clear();
	point push;
	push.x=x0;
	push.y=y0;
	p.push_back(push);
	for(int i=1;i<n;i++)
	{
		push.x=(A*push.x+B)%M;
		push.y=(C*push.y+D)%M;
		p.push_back(push);
	}
}

void solve(int casen)
{
	int ans=0;
	int siz=p.size();
	for(int i=0;i<siz;i++)
		for(int j=i+1;j<siz;j++)
			for(int k=j+1;k<siz;k++)
				if(isit(p[i],p[j],p[k]))  ans++;
	printf("Case #%d: %d\n",casen,ans);
}

int main()
{
	scanf("%d",&nt);
	for(int i=0;i<nt;i++)
	{
		read();
		solve(i+1);
	}

    return 0;
}
