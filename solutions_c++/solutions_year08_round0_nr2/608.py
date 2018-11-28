#include <iostream>
#include <queue>
#include <vector>
#include <cstdlib>

#define REP(i,n) for (int i=1,_n=(n);i<=_n;i++)

#define A 0
#define B 1

using namespace std;

const int maxn=1000+10; const int maxint=2100000000;

typedef struct _node
{
        int st;
        int et;
        _node () {}
        _node (int tt) {st=tt;}
}node;

struct comp
{
	bool operator () (const node &a, const node &b)
	{
         return a.st>b.st;
	}
};
priority_queue<node, vector <node>, comp> Heap[2];

node list[2][maxn];

int N[2];

int need[2];

int T;

int K;

inline int readTime()
{
       int h,m;
       scanf("%d:%d",&h,&m);
       return h*60+m;
}

inline void Init()
{
       scanf("%d",&T);
       int u,v;
       scanf("%d%d",&N[A],&N[B]);
       for (int i=0;i<2;i++)
       {
           REP(j,N[i])
           {
              u=readTime(); v=readTime();
              list[i][j].st=u; list[i][j].et=v;
           }
       }
       while (Heap[A].size()) Heap[A].pop();
       while (Heap[B].size()) Heap[B].pop();
}

inline int comp(const void *a,const void *b)
{
       node *aa=(node *)a; node *bb=(node *)b;
       if (aa->st<bb->st || (aa->st==bb->st && aa->et<bb->et)) return -1;
       return 1;
}

inline void work()
{
       for (int i=0;i<2;i++) qsort(list[i]+1,N[i],sizeof(node),comp);
       
       need[A]=need[B]=0;
       
       Heap[A].push(node(maxint)); Heap[B].push(node(maxint));
       list[A][N[A]+1].st=maxint; list[B][N[B]+1].st=maxint;
       
       int i[2];
       i[A]=1; i[B]=1;
       
       int nowT,now;
       int StTime;
       
       while (i[A]<=N[A] || i[B]<=N[B])
       {
             now=A;
             nowT=list[A][i[A]].st;
             if (list[B][i[B]].st<list[A][i[A]].st 
             || (list[B][i[B]].st==list[A][i[A]].st && list[B][i[B]].et<list[A][i[A]].et))
             {
                 now=B;
                 nowT=list[B][i[B]].st;
             }
             
             StTime=Heap[now].top().st;
             if (StTime<=nowT) Heap[now].pop();
             else need[now]++;
             Heap[now^1].push(node(list[now][i[now]].et+T));
             i[now]++;
       }
       printf("Case #%d: %d %d\n",K,need[A],need[B]);
}

int main()
{
    freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
    int t; scanf("%d",&t);
    for (K=1;K<=t;K++)
    {
        Init();
        work();
    }
    return 0;
}
