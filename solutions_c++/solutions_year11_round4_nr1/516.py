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

int A[1000001];

int main(void)
{
  int T,t;
  cin>>T;
  for(t=1;t<=T;t++)
  {
    int X,S,R,tim,N;
    cin>>X>>S>>R>>tim>>N;
    double res = 0.0;
    double time = tim;
    MEMZ(A);

    REP(i,N)
    {
      int B,E,w;
      cin>>B>>E>>w;
#ifdef DEBUG
cout<<B<<","<<E<<","<<w<<endl;
#endif
      for(int j = B; j< E;j++)
      {
        A[j] = w;
      }
    }
#ifdef DEBUG
REP(i,X)
cout<<A[i]<<",";
cout<<endl;
#endif
    sort(A,A+X);
#ifdef DEBUG
REP(i,X)
cout<<A[i]<<",";
cout<<endl;
#endif
    int pos = 0;
    while(pos<X)
    {
      int * next = upper_bound(&A[pos], &A[X],A[pos]);
      ll diff = next - &A[pos];
#ifdef DEBUG
cout<<pos<<","<<pos + diff<<endl;
#endif
      double runlength = time * (A[pos] + R);
      if(runlength>=diff-EPS)
      {
        double rtime = (double)diff / (A[pos] + R);
        res += rtime;
        time -= rtime;
      }
      else if(runlength >0+EPS)
      {
        double rest = diff - runlength;
        res += (double)runlength / (A[pos] + R);
        res += (double)rest / (A[pos] + S);
        time = 0;
      }
      else
      {
        res += (double)diff / (A[pos] + S);
        time = 0;
      }
      pos += diff;
    }
    cout.precision(20);
    cout<<"Case #"<<t<<": "<<res<<endl;
  }
  return 0;
}

