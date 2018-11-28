#include<stdio.h>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<memory>
#include<math.h>
#include<time.h>
#include<string.h>
#include<algorithm>

using namespace std;

typedef vector<int> vi; 
typedef vector<string> vs; 

#define min(i,j) ((i)<(j)?(i):(j))
#define max(i,j) ((i)>(j)?(i):(j))
#define abx(i) ((i)>0?(i):(-(i)))
#define eps 1e-9

int T,p;
int na,nb;

struct mm
{
	int s;
	int e;
	bool c;
	bool operator < ( const mm &z)
	{
		if(s!=z.s)return s<z.s;
		return e<z.e;
	}
}a[256];
bool flag[256];

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int ncase,icase=1;
	int i,j,k,t;
	int ansa,ansb;
	bool now;
	for(scanf("%d",&ncase);ncase--;)
	{
		scanf("%d%d%d",&T,&na,&nb);
		p=0;ansa=ansb=0;
		while(na--)
		{
			scanf("%d:%d%d:%d",&i,&j,&k,&t);
			a[p].s=i*60+j;a[p].c=true;
			a[p++].e=k*60+t+T;
		}
		while(nb--)
		{
			scanf("%d:%d%d:%d",&i,&j,&k,&t);
			a[p].s=i*60+j;a[p].c=false;
			a[p++].e=k*60+t+T;
		}
		sort(a,a+p);
		memset(flag,true,sizeof(flag));
		for(i=0;i<p;i++)
			if(flag[i])
			{
				if(a[i].c)ansa++;
				else ansb++;
				t=a[i].e;
				now=a[i].c;
				for(j=i+1;j<p;j++)
					if((a[j].c^now)&&flag[j]&&a[j].s>=t)
					{
						flag[j]=false;
						t=a[j].e;
						now=!now;
					}
			}
		printf("Case #%d: %d %d\n",icase++,ansa,ansb);
	}
	return 0;
}

