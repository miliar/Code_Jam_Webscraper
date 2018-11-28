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

char ss[1000];

int main()
{
  int T;
  cin >> T;
  for(int t = 1 ; t <= T ; t++)
    {
      printf("Case #%d: ", t);
      int k;
      string s;
      cin>>k>>s;      
      int perm[5]={0,1,2,3,4};
      int mini=s.size()+2;
      do {
        int t=1;
        for(int i = 0 ; i < s.size() ; i += k)
          for(int j = 0 ; j < k ; j++)
            ss[i + j] = s[i + perm[j]];
        for(int i = 1 ; i < s.size() ; i++)
          t+=ss[i] != ss[i-1];
        mini=min(t,mini);
      } while(next_permutation(perm, perm + k));
      
      cout<<mini;
      puts("");
    }

  return 0;
}
