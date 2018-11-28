// Google code jam TrainTable
#include <cstdio>
#include <algorithm>
using namespace std;


int a[128][2], b[128][2];
int na, nb;
int K;

struct nod { int x, grup,in;};

nod x[1000];
int nx;

struct cmp{
	bool operator()(const nod &a,const nod &b)const
	{
		if(a.x<b.x)return 1;
		if(a.x==b.x && a.in>b.in) return 1;
		return 0;
	}
};


void read()
{
	scanf("%d\n",&K);
	scanf("%d %d\n", &na, &nb);
	int i,p,q;
	
	for(i=1;i<=na;++i)
	{
		scanf("%d:%d ", &p, &q);
		a[i][0]=p*60+q;
		scanf("%d:%d\n", &p, &q);
		a[i][1]=p*60+q;
	}
	for(i=1;i<=nb;++i)
	{
		scanf("%d:%d ", &p, &q);
		b[i][0]=p*60+q;
		scanf("%d:%d\n", &p, &q);
		b[i][1]=p*60+q;
	}	
}


void doit(int caz)
{
	int i, j,k,left,right,ok;
	
	for(i=0;i<=na;++i)
		for(j=0;j<=nb;++j)
		{
		
			ok=1;
			left=i;
			right=j;
			
			for(k=1;k<=nx;++k)
			{
				if(x[k].grup==1)
				{
					if(x[k].in==1) --left;
					if(x[k].in==2) ++right;
				}
				else
				{
					if(x[k].in==1) --right;
					if(x[k].in==2) ++left;
				}
				
				//if(i==0 && j==2) printf("x[k].x :%d x[k].grup: %d x[k].in: %d: (%d %d)\n",x[k].x, x[k].grup, x[k].in,left,right); 
				if(left<0 || right<0) {ok=0;break;}
			}		
			
			if(ok) { printf("Case #%d: %d %d\n",caz, i,j);return;};
			
			
		}
	
	
	
	
}


void solve(int caz)
{
	int i, j;

	nx=0;
	for(i=1;i<=na;++i)
	{
		
		x[++nx].x=a[i][0];
		x[nx].grup=1;
		x[nx].in=1;
		x[++nx].x=a[i][1]+K;
		x[nx].grup=1;
		x[nx].in=2;
	}
	
	for(i=1;i<=nb;++i)
	{
		x[++nx].x=b[i][0];
		x[nx].grup=2;
		x[nx].in=1;
		x[++nx].x=b[i][1]+K;
		x[nx].grup=2;
		x[nx].in=2;
	}
	

	sort(x+1,x+nx+1,cmp());
	
	doit(caz);
	
	
}

int main()
{
	int T;
	freopen("train.in","r",stdin);
	freopen("train.out","w",stdout);
	scanf("%d\n", &T);
	
	for(int i=1;i<=T;++i)
	{
		read();
		solve(i);
	}
	return 0;
}
