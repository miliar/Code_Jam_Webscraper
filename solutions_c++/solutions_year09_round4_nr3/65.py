
#include <iostream>
#include <cstring>
#include <queue>
#include <deque>
#include <vector>
#include <cstdio>
#include <stack>
#include <cmath>
#include <map>
#include <algorithm>
using namespace std;

typedef pair<int,int> pii;
#define f first
#define s second

const int szmax=2*100+2;


struct st{
int pos;
int val;
int pre;
int maxflw;
bool operator < (const st &a) const{
return val>a.val;
}
};

pair<int,int> mincostflow(int sz, vector<int> *next, int cost[][szmax], int cap[][szmax], int sta, int end, int maxval){
int ret=0;
int retflow=0;

int pot[sz]; //potential
for(int i=0;i<sz;i++)pot[i]=0xaaaaaaaa;
pot[sta]=0;
for(int i=0;i<sz;i++){
	for(int k=0;k<sz;k++)for(int t=0;t<sz;t++)if(cap[k][t]){
		pot[t]=min(pot[t],pot[k]+cost[k][t]);
	}
}

#define getcost(a,b) (cost[a][b]+pot[a]-pot[b])

while(1){
priority_queue<st> q;
int dist[sz];memset(dist,0,sizeof(dist)); //for potential calc

int prev[sz];memset(prev,-1,sizeof(prev));
q.push((st){sta,0,-2,maxval-retflow});

int flw;
while(q.size()){
st now=q.top();
q.pop();
int pos=now.pos;
int val=now.val;
int pre=now.pre;
int maxflw=now.maxflw;

if(maxflw==0)break;

if(prev[pos]!=-1)continue;
prev[pos]=pre;
dist[pos]=val;

if(pos==end)flw=maxflw;

for(int i=0;i<next[pos].size();i++){
int go=next[pos][i];
if(cap[pos][go]<=0)continue;
if(prev[go]!=-1)continue;

//assert(0<=getcost(pos,go));
q.push((st){go,val+getcost(pos,go),pos,min(maxflw,cap[pos][go])});
}
}
if(prev[end]==-1)break;

int pos=end;
while(prev[pos]!=-2){
cap[prev[pos]][pos]-=flw;
cap[pos][prev[pos]]+=flw;
pos=prev[pos];
}
ret+=flw*(dist[end]+pot[end]-pot[sta]);
retflow+=flw;

//recalc pot
for(int i=0;i<sz;i++)pot[i]+=dist[i];
int minpot=1000*1000*1000;
for(int i=0;i<sz;i++)minpot=min(minpot,pot[i]);
for(int i=0;i<sz;i++)pot[i]-=minpot; //offset adjust (not to overflow)
}
return make_pair(ret,retflow);
}

int main(){
	int nn;scanf("%d",&nn);
	while(nn--){
		int n,m;scanf("%d%d",&n,&m);
		vector<int> v[n];
		for(int i=0;i<n;i++){
			v[i].resize(m);
			for(int k=0;k<m;k++)scanf("%d",&v[i][k]);
		}
		sort(v,v+n);

		int ans=-1;

		for(int x=1;x<=n;x++){
			int sz=2*n+2;
			int sta=sz-2;
			int end=sz-1;
			int cap[sz][szmax];memset(cap,0,sizeof(cap));
			int cost[sz][szmax];
			
	vector<int> next[sz];

#define add(from,to,capa,costt) {\
	next[from].push_back(to);\
	next[to].push_back(from);\
	cap[from][to]=(capa);\
	cost[from][to]=(costt);\
	cost[to][from]=-(costt);\
	}

		for(int i=0;i<n;i++)add(sta,i,1,0);
		for(int i=0;i<n;i++)add(n+i,end,1,0);
		for(int i=0;i<n;i++)add(i,n+i,1,0);

		for(int i=0;i<n;i++)for(int k=0;k<n;k++)if(i!=k){
			int ng=0;
			for(int t=0;t<m && ng==0;t++)if(v[k][t]<=v[i][t])ng=1;

			if(ng==0)add(n+i,k,1,-1);
		}
		
#if 0
		for(int i=0;i<sz;i++)for(int k=0;k<sz;k++)if(cap[i][k]){
			cout<<i<<"->"<<k<<" cap"<<cap[i][k]<<" cost"<<cost[i][k]<<endl;
		}
#endif

			pair<int,int> ret=mincostflow(sz,next,cost,cap,sta,end,x);
			int retval=ret.first;
			int retflw=ret.second;
			//cout<<"x"<<x<<" retval"<<retval<<" retflw"<<retflw<<endl;
			int cnt=retflw-retval;
			if(cnt==n){ans=x;break;}
		}

		static int npr=1;
		printf("Case #%d: %d\n",npr++,ans);
	}
}
