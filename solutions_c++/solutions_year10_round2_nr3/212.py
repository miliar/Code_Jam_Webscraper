#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <boost/foreach.hpp>

using namespace std;

static const int MOD = 100003;
int modmup(int a, int b, int m )
{
    if(a>m)
        a=a%m;
    if(b>m)
        b=b%m;
    int ret = 0;
    if(a<b)
        swap(a,b);
    while(b)
    {
        while(a<m)
        {
            if(b&1)
                ret += a;
            a<<=1;
            b>>=1;
        }
        a-=m;
        while(ret>=m)
            ret-=m;
        if(a<b)
            swap(a,b);
    }
    return ret;
};

int binomial[501*501];
#define cnk(n, k) binomial[(n)*501+k]

int result[501*501];
#define res(n, c) result[(n)*501+c]
int init()
{
  memset(binomial, 0, 501*501*sizeof(int));
  cnk(0, 0) = 1;
  for (int n=1; n<501; ++n)
  {
    cnk(n, 0) = 1;
    for (int k=1; k<=n; ++k)
    {
      cnk(n, k) = (cnk(n-1, k) + cnk(n-1, k-1)) % MOD;
    }
  }
  for (int i=0; i<501*501; ++i)
    result[i] = -1;
}

// winning sequences with n of size c
int computecache(int n, int c)
{
  //cerr << "inres " << n <<" " << c<<" " << res(n, c) <<endl;
  if (n==1 && c==0) return 1;
  if (n<c || c<=0)
    return 0;
  if (res(n, c)!=-1)
    return res(n, c);
  int r = 0;
  r += computecache(c, c-1);
  for (int d=2; c-d>0 && n-c-1>0; ++d)
  {
    // result(c, c-d)* C(d, n-c-d)
    //cerr << "add " << computecache(c, c-d) <<" " << (d-1) <<" " << (n-c-1) <<" " <<   cnk(d-1, n-c-1) << endl;
    r+= modmup(computecache(c, c-d), cnk(d-1, n-c-1), MOD);
  }
  //cerr << "res " << n <<" " << c<<" " << r <<endl;
  res(n, c) = r;
  return r;
}

std::string getLine()
{
  char line[4096];
  cin.getline(line, 4096);
  return line;
}



int main()
{
  int T;
  cin >> T;
  init();
  for (int t=0; t<T; ++t)
  {
    int N;
    cin >>N;
    int r = 0;
    for (int i=1; i<=N; ++i)
      r = (r + computecache(N, i))% MOD;
    cout << "Case #" << (t+1) <<": " << (r-1) << endl;
  }
}
