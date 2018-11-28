#include<vector>
#include<list>
#include<iostream>
#include<cstring>
using namespace std;
int t,casenum,n,k,i,j,l;
int price[150][30];
int ans;
const int infinity=0x3FFFFFFF;
const int maxsize=10000;
class maxflow
{
public:
    struct graph
    {
        int f,c,link;
        graph *next;
        graph *opposite;
        bool positive;
    };
    vector<graph*> g;
    vector<graph*> first;
    list<int> queue;
    int dist[maxsize];
    bool h[maxsize];
    int size;
    void init(int nodenum)
    {
        size=nodenum;
        g.clear();
        for (int i=0;i<=size;i++) g.push_back(NULL);
    }
    void addedge(int x,int y,int c)
    {
        graph *p=new graph;
        p->link=y;
        p->f=0;
        p->c=c;
        p->next=g[x];
        p->positive=true;
        g[x]=p;
        p=new graph;
        p->link=x;
        p->f=0;
        p->c=c;
        p->next=g[y];
        p->positive=false;
        g[y]=p;
        g[x]->opposite=g[y];
        g[y]->opposite=g[x];
    }
    void spfa()
    {
        for (int i=1;i<=size;i++) dist[i]=infinity;
        for (int i=1;i<=size;i++) h[i]=false;
        dist[0]=0;
        h[0]=true;
        queue.clear();
        queue.push_back(0);
        while (!queue.empty())
        {
            graph *p=g[queue.front()];
            while (p)
            {
                if ((p->positive)&&(p->f<p->c)||(!p->positive)&&(p->f>0))
                if (dist[queue.front()]+1<dist[p->link])
                {
                    dist[p->link]=dist[queue.front()]+1;
                    if (!h[p->link])
                    {
                        h[p->link]=true;
                        queue.push_back(p->link);
                    }
                 }
                 p=p->next;
            }
            h[queue.front()]=false;
            queue.pop_front();
        }
    }
    int dinic(int cur,int flow)
    {
        if (cur==size) return flow;
        graph *p=first[cur];
        int delta=0;
        while (p)
        {
            if (dist[cur]+1==dist[p->link])
                if ((p->positive)&&(p->f<p->c)||(!p->positive)&&(p->f>0))
                {
                    int r;
                    if (p->positive)
                    {
                        r=dinic(p->link,min(flow-delta,p->c-p->f));
                        p->f+=r;
                        p->opposite->f+=r;
                    }
                    else
                    {
                        r=dinic(p->link,min(flow-delta,p->f));
                        p->f-=r;
                        p->opposite->f-=r;
                    }
                    delta+=r;
                    if (delta==flow) break;
                }
            p=p->next;
       }
       first[cur]=p;
       return delta;
    }
};
maxflow index;
int main()
{

	freopen("problem.in","r",stdin);
	freopen("problem.out","w",stdout);
	cin>>t;
	for	(casenum=1;casenum<=t;casenum++)
	{
		cin>>n>>k;
		index.init(2*n+1);
		for (i=1;i<=n;i++)
			for (j=1;j<=k;j++)
				cin>>price[i][j];
		ans=n;
		for (i=1;i<=n;i++)
			index.addedge(0,i,1);
		for (i=n+1;i<=2*n;i++)
			index.addedge(i,2*n+1,1);
		for (i=1;i<=n;i++)
			for (j=1;j<=n;j++)
			{
				bool flag=true;
				for (l=1;l<=k;l++)
					if (price[i][l]<=price[j][l])
					{
						flag=false;
						break;
					}
				if (flag) index.addedge(i,j+n,infinity);
			}
		while (1)
		{
			index.spfa();
			if (index.dist[index.size]==infinity) break;
			index.first=index.g;
			ans-=index.dinic(0,infinity);
		}
		cout<<"Case #"<<casenum<<": "<<ans<<endl;
	}
}
