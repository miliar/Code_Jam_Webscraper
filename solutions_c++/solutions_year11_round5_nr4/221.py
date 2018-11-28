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
		char num[130];
		scanf("%s",num);
		int n=0;
		rep(i,130)
		{
			n=i;
			if(num[i]==0)
				break;
		}
		int q=0;
		rep(i,n)
			if(num[i]=='?')
				q++;
		rep(i,1<<q)
		{
			ll now=0;
			int p=0;
			rep(j,n)
			{
				if(num[j]=='?')
				{
					now=(now<<1)+(((1<<p)&i)?1:0);
					p++;
				}
				else
					now=(now<<1)+(num[j]-'0');
			}
			ll s=(ll)sqrt((double)now);
			if(s*s==now || (s+1)*(s+1)==now)
			{
				printf("Case #%d: ",caseID+1);
				p=0;
				rep(j,n)
				{
					if(num[j]=='?')
					{
						printf("%d",(((1<<p)&i)?1:0));
						p++;
					}
					else
						printf("%d",num[j]-'0');
				}
				printf("\n");
				break;
			}
		}
		
			
		
		
	}
	
	return 0;
}

