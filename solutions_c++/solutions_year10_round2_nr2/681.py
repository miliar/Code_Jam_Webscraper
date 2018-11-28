#include <vector>
#include <list>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
using namespace std;
#define dump(x) cerr <<  __LINE__ << " : "<< #x << "  =  " << (x) <<endl;
#define CL(a,x) memset(a,x,sizeof(a))
#define Pb push_back
#define Mp(A,B) make_pair(A,B)
#define SZ(v) ((int)(v).size())
#define LEN(X) ((int)X.length())
//遍历 
#define BEND(v) v.begin(),v.end()
#define FR(i,a,b) for(int i=(a);i<(b);++i)//[a,b)
#define FOR(i,n) FR(i,0,n)//[0,n)
#define FORALL(i,v) FOR(i,(int)v.size())//[0,v.size()) 
#define FORSZ(i,a,v) FR(i,a,SZ(v))//[a,v.size())
#define FRE(i,a,b) for(int i=(a);i<=(b);++i)//[a,b]
#define FORE(i,n) FRE(i,1,n)//[1,n]
#define FOREACH(i,v) for(typeof(v.end())i=v.begin();i!=v.end();++i)
//反向遍历  
#define RF(i,a,b) for(int i=(a)-1;i>=(b);--i)//[b,a)
#define ROF(i,n) RF(i,n,0)//[0,n)
#define RFE(i,a,b) for(int i=(a);i>=(b);--i)//[b,a]
#define ROFE(i,n) RFE(i,1,0)//[1,n]
#define ROFALL(i,v) ROF(i,(int)v.size())//[0,v.size()) 
#define ROFSZ(i,a,v) RF(i,SZ(v),a)//[a,v.size())
#define ROFEACH(i,v) for(typeof(v.rend())i=v.rbegin();i!=v.rend();++i)
const double Pi=acos(-1.0);
const double eps=1e-11;
typedef pair<int,int> pi;
template <class T> void out(T A[],int n){for (int i=0;i<n;i++) cout<<A[i]<<" ";cout<<endl;}
template <class T> void out (vector<T> A,int n=-1){if(n==-1) n=A.size();for (int i=0;i<n;i++) cout<<A[i]<<" ";cout<<endl;}
int toInt(string s){istringstream sin(s);int t; sin>>t; return t;}
string toString (int v){ostringstream sout;sout<<v; return sout.str();}
#define printg case_number++, printf("Case #%d: ",case_number), printf
#define gout case_number++, printf("Case #%d: ",case_number), cout

using namespace std;

int my_pos[50];
int v[50];
int lefttime[50];
int canreach[50];

int main()
{
    freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int tcase,ncase,n,k,b,t,i,j,h,ans;
	scanf("%d",&ncase);
	for(tcase=1;tcase<=ncase;tcase++)
	{
		printf("Case #%d: ",tcase);
		scanf("%d%d%d%d",&n,&k,&b,&t);
		for(i=0;i<n;i++)
		{
			scanf("%d",&my_pos[i]);
		}
		j=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",&v[i]);
			if((b-my_pos[i])<=v[i]*t)
			{
				j++;
				canreach[i]=1;
			}
			else
			{
				canreach[i]=0;
			}
		}
		if(j<k)
		{
			printf("IMPOSSIBLE\n");
			continue;
		}
		ans=0;
		for(i=n-1;i>=0&&k>0;i--)
		{
			if(canreach[i]==1)
			{
				k--;
				h=0;
				for(j=i+1;j<n;j++)
					if(canreach[j]==0)
						ans++;
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}
