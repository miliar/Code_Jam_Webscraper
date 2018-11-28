//DEDICATED TO EMMA WATSON, THE BRITISH *SUNSHINE*
#include <vector>
#include <list>
#include <map>
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
//#include <fstream>

#define eps 1e-11
#define INF 1000000000
#define PI 3.141592653589793238462
#define EU 2.71828182845904523536
#define sz(a) (int)a.size()
#define pb(a) push_back(a)
#define mset(a,hodnota) memset(a,hodnota,sizeof(a))
#define wh(a) a.begin(),a.end()
#define REP(i,n) for(__typeof(n) i=0;i<(n);++i)
#define REPS(i,n) for(int(i)=0;i<int(n.size());++i)
#define FOR(i,a,b) for(__typeof(b) i=(a);i<=(b);++i)
#define FORD(i,a,b) for(__typeof(a) i=(a);i>=(b);--i)
#define FORE(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define SQR(a) ((a)*(a))
#define pii pair<int,int>
#define mp(a,b) make_pair(a,b)
#define fi first
#define se second
typedef long long ll;
using namespace std;
int N,L,D;
struct mystr
{
  char S[20];
};
int M[5005][20];
char buf[505];
int P[20];
int main( )
{
  scanf("%d %d %d",&L,&D,&N);
  REP(i,D)
  {
    scanf("%s",buf);
    REP(j,L)
      M[i][j]=1<<int(buf[j]-'a');
  }
  REP(i,N)
  {
    scanf("%s",buf);
    int dlz=strlen(buf),ind=0;
    REP(j,dlz)
      if (buf[j]=='(')
      {
        int k=j+1;
        P[ind]=0;
        while(buf[k]!=')')
        {
          P[ind]|=1<<int(buf[k]-'a');
          k++;        
        }
        j=k;
        ind++;
      }else
      {
        P[ind]=1<<int(buf[j]-'a');
        ind++;      
      } 
    int ans=0;   
    REP(j,D)
    {   
      int ok=1;
      REP(k,L)
        if ((M[j][k]&P[k])==0)
        {
          ok=0;break;
        }
      ans+=ok;
    }
    printf("Case #%d: %d\n",i+1,ans);  
  }



  
  return 0;
}
