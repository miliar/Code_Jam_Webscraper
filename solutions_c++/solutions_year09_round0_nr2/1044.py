/*
PROB: problemB
CONT: google code jam qualification 2009
KEYW: graph, connected components
*/

#include <iostream>
#include <queue>

using namespace std;

// ------------- union find -------------
int prev[1000002],rank[1000002];

int find(int p)
{
 if(prev[p]!=-1) return prev[p]=find(prev[p]);
 return p;
}

void merge(int p,int q)
{
 int pp=find(p); int pq=find(q);

 if(rank[pp]>rank[pq]) prev[pq]=pp;
 else prev[pp]=pq;
 
 if(rank[pp]==rank[pq]) rank[pq]++;    
} 
// -------------            -------------

int n,m,compNum;
int alt[101][101],comp[101][101];
char table[101][101];
queue<int> q;
           
int dx[]={-1, 0, 0,+1};
int dy[]={ 0,-1,+1, 0};

void init()
{
 // init union find
 memset(rank,0,sizeof(rank));
 memset(prev,-1,sizeof(prev));
 
 // init comp
 memset(comp,-1,sizeof(comp)); compNum=1;
 memset(table,'-',sizeof(table));
 
 int i,j;
 scanf("%d %d",&n,&m);
 for(i=1;i<=n;i++)
   for(j=1;j<=m;j++)
       scanf("%d",&alt[i][j]);    
}

bool isIn(int i,int j)
{ return i>=1 && i<=n && j>=1 && j<=m; }

void bfs(int u)
{
 q=queue<int> ();
 int tmpr,tmpc;
 int nextr,nextc;
 int i,minn,dir;
 
 q.push(u);
 comp[u/101][u%101]=compNum;
 
 while(!q.empty())
 {
  tmpr=(q.front())/101; tmpc=(q.front())%101; q.pop();    
    
  minn=INT_MAX; dir=-1;
  for(i=0;i<4;i++)
    {
     nextr=tmpr+dx[i];
     nextc=tmpc+dy[i];
     if(!isIn(nextr,nextc)) continue;
     if(alt[nextr][nextc]<alt[tmpr][tmpc] && alt[nextr][nextc]<minn) { minn=alt[nextr][nextc]; dir=i; }             
    }
  
  if(dir==-1) continue;
    
  nextr=tmpr+dx[dir];
  nextc=tmpc+dy[dir];
  
  if(comp[nextr][nextc]==-1) { comp[nextr][nextc]=compNum; q.push(nextr*101+nextc); }
  else { merge(compNum,comp[nextr][nextc]); }
 }  
 
 compNum++;    
}

void fill(int u,char letter)
{
 q=queue<int> ();
 int tmpr,tmpc;
 int nextr,nextc,i;    
 
 table[u/101][u%101]=letter;
 q.push(u);
 
 while(!q.empty())
 {
  tmpr=(q.front())/101; tmpc=(q.front())%101; q.pop();    
  
  for(i=0;i<4;i++)
    {
     nextr=tmpr+dx[i]; nextc=tmpc+dy[i];
     if(isIn(nextr,nextc) && table[nextr][nextc]=='-' && comp[tmpr][tmpc]==comp[nextr][nextc]) { table[nextr][nextc]=letter; q.push(nextr*101+nextc); } 
    }              
 } 
}

void solve()
{
 init();
 
 int i,j;
 for(i=1;i<=n;i++)
    for(j=1;j<=m;j++)
         if(comp[i][j]==-1) bfs(i*101+j);    
  
 for(i=1;i<=n;i++)
   for(j=1;j<=m;j++)
       comp[i][j]=find(comp[i][j]);
 
 char letter='a';
 for(i=1;i<=n;i++)
   for(j=1;j<=m;j++)
       if(table[i][j]=='-') { fill(i*101+j,letter); letter++; }
}

int main()
{
 int tests;
 scanf("%d",&tests);
 
 for(int p=1;p<=tests;p++)
   {
    solve();
    printf("Case #%d:\n",p);
    for(int i=1;i<=n;printf("\n"),i++)
      for(int j=1;j<=m;j++)
          printf("%c ",table[i][j]);
   }
 
 //system("pause");
 return 0;   
}
