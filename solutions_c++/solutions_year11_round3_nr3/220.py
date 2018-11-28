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
#include <cstring>

using namespace std;

string itoa(int val) {stringstream ss;ss << val;return ss.str();}
typedef vector<int> vi;
vi parseInt(string s) {stringstream ss(s);vi ans;while (!ss.eof()) {int temp; ss >> temp; ans.push_back(temp); } return ans;}
#define COPY(x,y) y.resize(x.size());copy(x.begin(),x.end(),y.begin())
#define pb push_back
#define SWAP(t,x,y) t temp=x;x=y;y=temp;
#define fr(i,s,e) for (int i = int(s); i < int(e); i++)
#define fr2(i,c) for (unsigned int i = 0; i < (c).size(); i++)
#define cl(a,val) memset(a,val,sizeof(a)); 

int main(int argc,char* argv[]) {
  int t;
  cin >> t;
  fr(i,0,t) {
    int n,l,h;
    cin >> n >> l >> h;
    vector<int> f;
    fr(k,0,n) {
      int x;
      cin >> x;
      f.pb(x);
    }
    int ans = -1;
    fr(k,l,h+1) {
      bool ok = true;
      fr2(j,f) {
        if (f[j]>k) {
          if (f[j]%k!=0) {
            ok = false; break;
          }
        } else {
          if (k%f[j]!=0) {
            ok = false; break;
          }
        }
      }
      if (ok) {
        ans = k; break;
      }
    }
    cout << "Case #" << i+1 << ": ";
    if (ans==-1) {
      cout << "NO" << endl;
    } else {
      cout << ans << endl;
    }
  }
	return 0;
}
