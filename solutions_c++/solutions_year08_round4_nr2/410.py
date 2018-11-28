#include<algorithm>
#include<cstdlib>
#include<iostream>
#include<map>
#include<sstream>
#include<set>
#include<string>
#include<numeric>
#include<vector>
#include<cmath>

#define PB push_back
#define SZ(x) int((x).size())
#define ALL(a) (a).begin(),(a).end()
#define REP(i,n) for(int i=0;i<(n);i++)

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int,int> pt;
typedef pair<ll,pt> pp;

void tt() {
  int N,M,A;
  cin>>N>>M>>A;
  map<int,pt> m;
  REP(x,N+1)
    REP(y,M+1)
    m[A+x*y]=pt(x,y);
  REP(x,N+1)
    REP(y,M+1)
    {
      int a = x*y;
      if(m.count(a))
        {
          cout << "0 0 " << m[a].first << " " << y << " " << x << " " << m[a].second;
          return;
        }
    }
  cout<<"IMPOSSIBLE";
}

int main()
{
  int T;
  cin >> T;
  for(int t = 1 ; t <= T ; t++)
    {
      printf("Case #%d: ", t);
      tt();
      puts("");
    }
  return 0;
}
