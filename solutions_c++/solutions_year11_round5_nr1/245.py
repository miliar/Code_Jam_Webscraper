// zero.lin`s google_codejam.cpp 
//
#include "google_codejam\stdafx.h"
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vii;
typedef pair<int,int> pii;
typedef long long ll;

#define rep(i,n) for(int i=0;i<n;++i)
#define all(n) n.begin(),n.end()
#define sz(o) (int)(o.size())
#define mset(o,v) memset(o,v,sizeof(o))
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define mk(first,second) make_pair(first,second)
#define present(container, element) (container.find(element) != container.end()) 
#define cpresent(container, element) (find(all(container),element) != container.end())

const int inf=1<<30;
const double eps=1e-6;
ll gcd(ll a,ll b){return b==0?a:gcd(b,a%b);};

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	
	int testcase;
	scanf("%d ",&testcase);
	rep(caseID,testcase)
	{
		int w,u,l,g;
		scanf("%d %d %d %d",&w,&l,&u,&g);
		vector<double> low(w+1,0),up(w+1,0);
		int lastx=-1;
		int lasty=-1;
		rep(i,l)
		{
			int x,y;
			scanf("%d %d",&x,&y);
			if(lastx!=-1)
			{
				for(int j=lastx;j<=x;++j)
				{
					low[j]=lasty+1.0*(y-lasty)*(j-lastx)/(x-lastx);
				}
			}
			lastx=x;
			lasty=y;
		}
		lastx=-1;
		rep(i,u)
		{
			int x,y;
			scanf("%d %d",&x,&y);
			if(lastx!=-1)
			{
				for(int j=lastx;j<=x;++j)
				{
					up[j]=lasty+1.0*(y-lasty)*(j-lastx)/(x-lastx);
				}
			}
			lastx=x;
			lasty=y;
		}
		double sum=0;
		for(int i=0;i<w;++i)
		{
			sum+=((up[i]-low[i])+(up[i+1]-low[i+1]));
		}
		printf("Case #%d:\n",caseID+1);
		double ea=sum/g;
		int now=0;
		double left=ea;
		for(int i=0;i<g-1;++i)
		{
			while(left>(up[now]-low[now])+(up[now+1]-low[now+1]))
			{
				left-=(up[now]-low[now])+(up[now+1]-low[now+1]);
				now++;
			}
			double s=(up[now]-low[now])+(up[now+1]-low[now+1]);
			double d1=(up[now]-low[now]);
			double d2=(up[now+1]-low[now+1]);
			double a=d2-d1;
			double b=d1*2;
			double c=-left;
			double d;
			if(abs(a)<eps)
				d=-c/b;
			else
				d=(-b+sqrt(b*b-4*a*c))/(2*a);
			printf("%f\n",now+d);
			left=ea+left;
			//now++;
		}
	}
	
	return 0;
}

