#include<iostream>
#include<map>
#include<math.h>
#include<vector>
#include<string>
#include<string.h>
#include<queue>
#include<algorithm>
#include<sstream>
#define all(X) (X).begin(),(X).end()
#define mem(X) memset(X,0,sizeof(X))
#define debug_v(v) for(int db=0;db<(v).size();db++)cout<<v[db]<<','<<;cout<<endl;
#define pqpush(pq,x,cmp) (pq).push_back(x);push_heap((pq).begin(),(pq).end(),cmp);
#define pqpop(pq,cmp) pop_heap((pq).begin(),(pq).end(),cmp);(pq).pop_back();
#define PB(x) push_back(x)
using namespace std;
typedef long long ll;
typedef vector<int>::iterator iv;
typedef map<string,int>::iterator msii;
typedef map<int,int>::iterator miii;
typedef map<int,bool>::iterator mibi;
typedef map<string,bool>::iterator msbi;
typedef map<string,int> msi;
typedef map<int,int> mii;
typedef map<int,bool> mib;
typedef map<string,bool> msb;
typedef vector<int> vi;
typedef vector<string> vs;
#define ESP 0.1

double rrm[1000],xm[1000],ym[1000],rm[1000],tx,ty;
int t,n,h1,h2,cc,h3,h4,m1[1000],w,l;
bool ans;

bool cmp(int fh1,int fh2){return rrm[fh1]>rrm[fh2];}

int nn;

bool chk(double x,double y,double r)
{
	for(int fh1=0;fh1<nn;fh1++)
	{
		if((xm[fh1]-x)*(xm[fh1]-x)+(ym[fh1]-y)*(ym[fh1]-y)+ESP<(rm[fh1]+r)*(rm[fh1]+r))return 0;
	}
	return 1;
}

int ttm[1000];

double pw(double aa){return aa*aa;}

void add(double x,double y,double r)
{
	xm[nn]=x;
	ym[nn]=y;
	rm[nn++]=r;
}

int main(){
	freopen("B-small-attempt3.in","r",stdin);
	freopen("B-small-attempt3.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d %d%d",&n,&w,&l);
		
		for(h1=0;h1<n;h1++)
		{
			scanf("%lf",&rrm[h1]);
			m1[h1]=h1;
		}
		
		sort(m1,m1+n,cmp);
		
		nn=0;
		
		double xx=0.01;
		
		add(0.01,0.01,rrm[m1[0]]);
		ttm[m1[0]]=0;
		/*
		for(h1=1;h1<n;h1++)
		{
			if((xx+=sqrt(pw(rrm[m1[h1]]+rrm[m1[h1-1]])-pw(rrm[m1[h1]]-rrm[m1[h1-1]]))+ESP)<=w)
			{
				add(xx,rrm[m1[h1]]+0.01,rrm[m1[h1]]);
				ttm[m1[h1]]=nn-1;
			}
			else break;
		}
		
		xx=0;

		for(;h1<n;h1++)
		{
			if((xx+=sqrt(pw(rrm[m1[h1]]+rrm[m1[h1-1]])-pw(rrm[m1[h1]]-rrm[m1[h1-1]]))+ESP)<=l)
			{
				add(rrm[m1[h1]]+0.01,xx,rrm[m1[h1]]);
				ttm[m1[h1]]=nn-1;
			}
			else break;
		}*/
		
		for(h1=1;h1<n;h1++)
		{
			do
			{
				tx=(double)w*(rand()%30000)/30000;
				ty=(double)l*(rand()%30000)/30000;
			}while(!chk(tx,ty,rrm[m1[h1]]));
			add(tx,ty,rrm[m1[h1]]);
			ttm[m1[h1]]=nn-1;
		}
		
		printf("Case #%d:",++cc);
		for(h1=0;h1<n;h1++)
		{
			printf(" %.6lf %.6lf",xm[ttm[h1]],ym[ttm[h1]]);
		}
		printf("\n");
	}
}
