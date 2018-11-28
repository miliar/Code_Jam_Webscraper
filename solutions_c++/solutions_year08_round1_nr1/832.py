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
#include <cstdio>
#include <sstream>
using namespace std;
#define FO(it,a) for(__typeof(a)::iterator it=a.begin();it!=a.end();++it)
#define FZ(i,n) for(int i=0;i<n;++i)
#define FL(i,s,e) for(int i=s;i<e;++i)
#define CLR(s,t) memset(s,t,sizeof(s))
#define sz size()
#define pb push_back

int main()
{
  int T, n;
  cin >> T;
  FZ(i,T) {
    cin >> n;
    vector<int> a(n), b(n);
    FZ(k,n) cin >> a[k];
    FZ(k,n) cin >> b[k];
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    int cnt = 0;
    FZ(k,n) {
      if (a[0] * b[ b.size()-1 ] < a[ a.size()-1 ] * b[0]){
        cnt += a[0] * b[ b.size()-1 ];
        a.erase(a.begin());
        b.erase(b.begin()+b.size()-1);
      }else{
        cnt += b[0] * a[ a.size()-1 ];
        b.erase(b.begin());
        a.erase(a.begin()+a.size()-1);
      }
    }
    cout << "Case #" << i+1 << ": " << cnt << endl;
  }
}
