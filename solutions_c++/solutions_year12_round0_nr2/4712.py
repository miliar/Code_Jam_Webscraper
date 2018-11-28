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
		int n,s,p;
		scanf("%d %d %d ",&n,&s,&p);
		int use=0;
		int res=0;
		for(int i=0;i<n;++i)
		{
			int d;
			scanf("%d ",&d);
			if(d>=p*3-4 && d>=p)
			{
				if((d-p)/2<=p-2)
				{
					if(use>=s)
						continue;
					use++;
				}
				res++;
			}
		}
		printf("Case #%d: %d\n",caseID+1,res);
		
	}
	
	return 0;
}

