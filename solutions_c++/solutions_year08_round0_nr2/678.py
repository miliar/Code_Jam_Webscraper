#include<cstdio>
#include<algorithm>
#include<queue>
#include<set>
using namespace std;
int n,t;
int cnt[2];
int na,nb;
int main()
{
	int l,i;
	int u,v,x,y;
	char st;
	//freopen ("B-large.in.txt", "r", stdin);
	//freopen ("output.txt", "w", stdout);
	scanf("%d",&n);
	for(l=1;l<=n;++l)
	{
		multiset<int> set[2];
		priority_queue<pair<int, pair<int,int> > > q;		
		cnt[0] = cnt[1] = 0;
		set[0].insert(-1);
		set[1].insert(-1);
		scanf("%d%d%d",&t,&na,&nb);
		for(i=0;i<na;++i){
			scanf("%d:%d %d:%d",&u,&v,&x,&y);
			q.push(make_pair(- (u*60+v),make_pair(x*60+y,0)));
		}
		for(i=0;i<nb;++i){
			scanf("%d:%d %d:%d",&u,&v,&x,&y);
			q.push(make_pair(- (u*60+v),make_pair(x*60+y,1)));
		}		
		while(!q.empty())
		{
			u = -q.top().first;	v=q.top().second.first;
			st=q.top().second.second;	q.pop();
			multiset<int>::iterator it = -- set[st].upper_bound (u);
			int train = *it;
			//printf ("%d/%d\t%d/%d\n",u/60,u%60,train/60,train%60);
			if (train == -1)
				++ cnt[st];
			else
				set[st].erase (it);				
			set[1 - st].insert (v + t);
		}
		printf("Case #%d: %d %d\n", l, cnt[0], cnt[1]);
	}
}
