#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <ctime>
using namespace std;
static const double EPS = 1e-9;
typedef long long ll;
typedef long long LL;
typedef pair<int,int>            PI;
typedef map<PI, int> MPI;
typedef vector<int>	VI;
typedef vector<PI>	VPI;
typedef vector< vector<int> >	VII;
typedef unsigned int UINT32;
typedef unsigned short UINT16;
typedef unsigned char UINT8;
#define ALL(c) (c).begin(), (c).end()
#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define FOR(i, s, n) for (int i = (s); i < (int)(n); i++)
#define PB(a)  push_back(a)
#define MP(a,b)  make_pair(a,b)
#define MEMZ(a) memset(a,0,sizeof(a))
#define ITER(c) __typeof((c).begin())
#define PRESENT(c, e) ((c).find((e)) != (c).end())
#define CPRESENT(c, e) (find(all(c), (e)) != (c).end())
#define TR(c, i) for (ITER(c) i = (c).begin(); i != (c).end(); ++i)

#define INF INT_MAX

#define MOD 1000000009

int flag[1001];

//gcc用の__gcdを使ったもの
inline long long lcm( long long m, long long n )
{
	return ((m / __gcd(m, n)) * n); // lcm = m * n / gcd(m,n)
}//l

//素数計算
//エラトステネスの篩

#define MAX_PRIME  2000000 //★適当
int isPrime[MAX_PRIME];
void CalcPrime(int N)
{
  int i;
  for(i=0;i<=N;i++)isPrime[i] = 0;
  for(i=3;i<=N;i+=2)isPrime[i] = 1;
  if(N<2)return;
  isPrime[2] = 1;
  for(i=3;(i*i)<=N;i+=2)
  {
    if(isPrime[i])
    {
      int j;
      int step = i*2; /* i*i + 奇数個のiは偶数なので、すでにisPrimeは0になっている */
      for(j= i*i;j<=N;j+=step)isPrime[j] = 0;
    }
  }
  return;
}


int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int N;
    cin>>N;
    if(N==1)
    {
      cout<<"Case #"<<t<<": "<<0<<endl;
      continue;
    }
    int cp=0;
    CalcPrime(N);
    for(int i = 1;i<=N;i++)
    {
      cp+=isPrime[i];
    }
#ifdef DEBUG
cout<<cp<<endl;
#endif
    MEMZ(flag);
    for(int i = 2;i<=N;i++)
    {
      for(int j= i+1;j<=N;j++)
      {
        int num = lcm(i,j);
        if(num<=N && num!=i && num!=j)
        {
          flag[num]=1;
#ifdef DEBUG
cout<<"num="<<num<<endl;
#endif
        }
      }
    }
    
    int ret = 0;
    for(int i = 1;i<=N;i++)
    {
      if(flag[i]==0)ret++;
    }
#ifdef DEBUG
cout<<ret<<endl;
#endif
    ret -= cp;
    cout<<"Case #"<<t<<": "<<ret<<endl;
  }
  return 0;
}

