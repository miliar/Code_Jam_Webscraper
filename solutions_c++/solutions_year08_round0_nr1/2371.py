#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <list>
#include <stack>
#include <numeric>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <cstdio>
using namespace std;
#define debug(a) cout << #a
#define FO(it,a) for(__typeof(a)::iterator it=a.begin();it!=a.end();++it)
#define FZ(i,n) for(int i=0;i<n;++i)
#define FL(i,s,e) for(int i=s;i<e;++i)
#define CL(s,t) memset(s,t,sizeof(s))
#define sz size()
#define pb push_back
#define B begin()
#define E end()
#define all(a) a.B,a.E 
#define GI ({int t;scanf("%d\n",&t);t;})
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<vector<int> > vvi;
int main()
{	
	int t = GI;
	FZ(tt,t)
	{
		int s = GI;
		string str;
		vs search;char buf[10000];
		FZ(i,s) scanf("%[^\n]",buf),search.pb(buf),getchar();
		int q = GI;
//		if(tt==10) cout << s  << " " << q << endl;
		int now = s-1,cnt=0;
		set<string> flag;
		FZ(i,q)
		{
			scanf("%[^\n]",buf),str = buf,getchar();
			if(flag.find(str) == flag.end()) 
			{	if(now == 0)
				{	
//					if(tt == 10)
//					cout << " change " << i << endl;

					++cnt;
					now = s-1;
					flag = set<string> ();
				}
				flag.insert(str),now--;
			}
//			cout << str << endl;
		}
		cout << "Case #" << tt+1 << ": " << cnt << endl;
	}
	return 0;
}
