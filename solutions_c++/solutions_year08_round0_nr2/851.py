#include <vector>
#include <sstream>
#include <set>
#include <map>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <queue>
#include <sstream>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;i++)
#define FO(i,j,n) for(int i=j;i<n;i++)
#define FOX(i,x) for(int i=0;i<x.size();i++)
#define VI vector<int>
#define VB vector<bool>
#define VVI vector<vector <int> >
#define VS vector<string>
#define S(x) sort(x.begin(),x.end());
#define R(x) reverse(x.begin(),x.end());
#define PII pair<int,int>
#define X first
#define Y second
#define PB push_back
#define MP make_pair

typedef long long ll;
typedef long double ld;

int adj[500][500];

int T,na,nb;

int maxflow(int source,int sink)
{
 int ret=0;
 while(1)
 {
  queue <int> bfs;
  int N=2*(na+nb)+2;
  int parent[500];
  memset(parent,-1,sizeof(parent));
  bfs.push(source);
  parent[source]=-1;
  bool done=false;
  while(!bfs.empty() && !done)
  {
   int u=bfs.front();
   bfs.pop();
   for(int j=0;j<N;j++)
           if(adj[u][j]!=0 && parent[j]==-1 && j!=source)
           {
            parent[j]=u;
            bfs.push(j);
            if(j==sink)
            {
             done=true;
             break;
            }
           }
  }
  if(!done)
           break;
  ret++;
  int t=sink;
  while(parent[t]!=-1)
  {
   adj[parent[t]][t]--;
   adj[t][parent[t]]++;
   t=parent[t];
  }
 }
 return ret;
}

string ta[110][2],tb[110][2];

bool good(string a, string b)
{
  int ha,ma,hb,mb;
  sscanf(a.c_str(),"%d:%d",&ha,&ma);
  sscanf(b.c_str(),"%d:%d",&hb,&mb);
  //  cout<<"In good:"<<endl;
  //  cout<<a<<" "<<ha<<" "<<ma<<endl;
  //  cout<<b<<" "<<hb<<" "<<mb<<endl;
  ma+=T;
  ha+=(ma/60);
  ma%=60;
  bool ret=ha<hb or ( ha==hb and ma<=mb);
  //  cout<<"Ans : "<<ret<<endl;
  return ret;
}

int main()
{
  int t;
  cin>>t;
  int cnt=1;
  while(t--)
    {
      cin>>T;
      cin>>na>>nb;
      FOR(i,na)
	cin>>ta[i][0]>>ta[i][1];
      FOR(i,nb)
	cin>>tb[i][0]>>tb[i][1];
      int source=2*(na+nb),sink=2*(na+nb)+1;
      memset(adj,0,sizeof(adj));
      FOR(i,na)
	FOR(j,nb)
	{
	  if(good(ta[i][1],tb[j][0]))
	    adj[i][na+nb+na+j]=1;
	  if(good(tb[j][1],ta[i][0]))
	    adj[na+j][na+nb+i]=1;
	}
      FOR(i,na+nb)
	adj[source][i]=1,adj[na+nb+i][sink]=1;
      int ans=maxflow(source,sink);
      int ac=0,bc=0;
      FOR(i,na)
	if(adj[na+nb+i][sink]==1)
	  ac++;
      FOR(i,nb)
	if(adj[na+nb+na+i][sink]==1)
	  bc++;
      assert(ac+bc==(na+nb-ans));
      printf("Case #%d: %d %d\n",cnt++,ac,bc);
    }
  return 0;
}

