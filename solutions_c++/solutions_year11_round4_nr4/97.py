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
const double eps=1e-11;
ll gcd(ll a,ll b){return b==0?a:gcd(b,a%b);};
bool prime(ll a)
{
	if(a==2)
		return true;
	if(a%2==0)
		return false;
	for(ll i=3;i*i<=a;i+=2)
		if(a%i==0)
			return false;
	return true;
}
stack<int> path;
int D[400];
vii m;
bool see[400];
int dfs(int a)
{
	if(a==0)
	{
		mset(see,0);
		int res=0;
		stack<int> p2;
		while(!path.empty())
		{
			int top=path.top();
			path.pop();
			for(int i=0;i<m[top].size();++i)
				if(!see[m[top][i]])
				{
					res++;
					see[m[top][i]]=true;
				}
			p2.push(top);
		}
		while(!p2.empty())
		{
			int top=p2.top();
			p2.pop();
			path.push(top);
			if(see[top])
			{
				res--;
				see[top]=false;
			}
		}
		return res;
	}
	int g=D[a]-1;
	int res=0;
	for(int i=0;i<m[a].size();++i)
	{
		if(D[m[a][i]]==g)
		{
			path.push(m[a][i]);
			res=max(res,dfs(m[a][i]));
			path.pop();
		}
	}
	return res;
}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	
	int testcase;
	scanf("%d ",&testcase);
	rep(caseID,testcase)
	{
		int p,w;
		scanf("%d %d ",&p,&w);
		mset(D,0);
		m=vii(p,vi(0));
		path=stack<int>();
		rep(i,w)
		{
			int a,b;
			scanf("%d,%d ",&a,&b);
			m[a].push_back(b);
			m[b].push_back(a);
		}
		priority_queue<pair<int,int > > q;
		q.push(pair<int,int >(0,0));
		
		int last[400];
		rep(i,400)
			D[i]=inf;
		D[0]=0;
		
		while(!q.empty())
		{
			pii top=q.top();
			q.pop();
			int s=top.first;
			if(top.second<=D[top.first])
			{
				for(vi::const_iterator it=m[s].begin();it!=m[s].end();++it){
						
						int cost=D[s] + 1;
                        int v2 = *it;
                        if(D[v2] > cost) {
                              // update distance if possible
                              D[v2] = cost;
                              // add the vertex to queue
                              q.push(pair<int,int >(v2,D[v2]));
                        }
                  }

			}
		}
		int res=inf;
		for(int i=0;i<m[1].size();++i)
		{
			if(res>D[m[1][i]])
				res=D[m[1][i]];
		}
		printf("Case #%d: %d %d\n",caseID+1,res,dfs(1));
	}
	
	return 0;
}

