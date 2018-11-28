//Jakub Kędzierski
// SZABLON BY UW:
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
 
using namespace std;
 
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define VAR(V,init) __typeof(init) V=(init)
#define FOREACH(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define INFTY 100000000
#define MAX int('z')-int('a')
#define FI first
#define SE second
 
typedef vector<int> VI;
typedef list<int> LI;
typedef priority_queue<int> PQI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;
template <class T>
inline int size(const T&a) { return a.size()-1; }
typedef vector<string> VS;
 
ll nwd(ll a,ll b) { return !b?a:nwd(b,a%b); }
inline int CEIL(int a,int b) { return a%b?a/b+1:a/b; }
 
VS parse(string s)
{
  string a;
  VS wyn;
  REP(i,s.size())
    if (s[i]!=' ') a+=s[i];
    else if (!a.empty()) { wyn.PB(a); a=""; }
  if (!a.empty()) wyn.PB(a);
  return wyn;
}
 
VS parse(string s,char ch)
{
  string a;
  VS wyn;
  REP(i,s.size())
    if (s[i]!=ch) a+=s[i];
    else if (!a.empty()) { wyn.PB(a); a=""; }
  if (!a.empty()) wyn.PB(a);
  return wyn;
}
 
int toi(char ch) { return int(ch)-int('0'); }
 
void tolower(string &s) { REP(i,s.size()) s[i]=tolower(s[i]); }
 
int chg(char ch) { return int(ch)-int('a'); }
// KONIEC SZABLONU UW

int main()
{
  int T;
  scanf("%d",&T);
  long long int N,D,G;
  for(int i=1;i<=T;i++)
	  {
		  bool da=false;
		  scanf("%lld%lld%lld",&N,&D,&G);
		 if(N<100){
			  for(int j=1;j<=N;j++)
				if(!((D*j)%100))
					da=true;}
		  else
			  da=true;
		  if(da){if((G==100)&&(D<100))
					da=false;
				 else if((G==0)&&(D!=0))
					da=false;
				}
		  if(da)
			  printf("Case #%d: Possible\n",i);
		  else
			  printf("Case #%d: Broken\n",i);
		}
  return 0;
}

