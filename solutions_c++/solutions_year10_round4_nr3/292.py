#include <set>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int Test,N,n[2];
pair<int,int> P[2][1000055];
set< pair<int,int> > myset[2];

inline bool Check1(int k,int x,int y)
{
	int xxx=myset[k].count(make_pair(x,y-1));
	if (xxx==1) return true;
	int yyy=myset[k].count(make_pair(x-1,y));
	if (yyy==1) return true;
	return false;
}

inline bool Check2(int k,int x,int y)
{
	int xxx=myset[k].count(make_pair(x,y-1));
	if (xxx==0) return false;
	int yyy=myset[k].count(make_pair(x-1,y));
	if (yyy==0) return false;
	return true;
}

inline void Add(int k,int x,int y)
{
	pair<int,int> p=make_pair(x,y);
	if (myset[k].count(p)>0) return;
	P[k][n[k]++]=p;
	myset[k].insert(p);
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d",&Test);
	for (int Case=1;Case<=Test;Case++) {
		scanf("%d",&N);
		myset[0].clear();
		myset[1].clear();
		n[0]=n[1]=0;
		for (int i=0;i<N;i++) {
			int x1,y1,x2,y2;
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for (int x=x1;x<=x2;x++)
			for (int y=y1;y<=y2;y++)
				Add(0,x,y);
		}
		int Ans=0;
		for (int u=0,v=1;n[u];u^=1,v^=1) {
			n[v]=0;++Ans;
			myset[v].clear();
			for (int i=0;i<n[u];i++) {
				int x=P[u][i].first,y=P[u][i].second;
				if (Check1(u,x,y)) Add(v,x,y);
				if (Check2(u,x,y+1)) Add(v,x,y+1);
			}
//			printf("%d\n",n[v]);
		}
		printf("Case #%d: %d\n",Case,Ans);
	}
	return 0;
}
