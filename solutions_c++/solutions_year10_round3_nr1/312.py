#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
const int N=40000;
struct TPoint
{
	int x,y;
}a[N];
int c[N];
int cmp(TPoint a, TPoint b)
{
	return a.x>b.x;
}

void insert(int x){
        int p;
        p=x;
        while(p<N){
                c[p]+=1;
                p+= p&(-p);
        }
}

int get(int x){
        int p,ans;
        p=x;
        ans=0;
        while(p>0){
                ans+=c[p];
                p-= p&(-p);
        }
        return ans;
}


int main()
{
	int i,t;
	int n,tc;
	freopen("A-large.in","r",stdin);
	freopen("out1.txt","w",stdout);
	scanf("%d",&tc);
	for(t=1;t<=tc;t++)
	{
		memset(c,0,sizeof(c));
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d%d",&a[i].x,&a[i].y);
		}
		sort(a,a+n,cmp);
		int sum = 0;
		for (i=0;i<n;i++)
		{
			sum+=get(a[i].y);
			insert(a[i].y);
		}
		printf("Case #%d: %d\n", t, sum);
	}
	return 0;
}
