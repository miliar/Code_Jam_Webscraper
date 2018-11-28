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
    int r,c;
    cin >> r >> c;
    vector<string> g;
    fr(k,0,r) {
      string s;
      cin >> s;
      g.pb(s);
    }
    bool ok = true;
    fr(k,0,r) {
      fr(j,0,c) {
        if (g[k][j]=='#') {
          if ((k==r-1) || (j==c-1)) {
            ok = false;
            break;
          }
          if (g[k][j+1]!='#'
              || g[k+1][j]!='#'
              || g[k+1][j+1]!='#') 
          {
            ok = false;
            break;
          }
          g[k][j]='/';
          g[k+1][j+1]='/';
          g[k+1][j]='\\';
          g[k][j+1]='\\';
        }
      }
      if (!ok) break;
    }
    cout << "Case #" << i+1 << ": " << endl;
    if (!ok) {
      cout << "Impossible" << endl;
    } else {
      fr(k,0,r)
        cout << g[k] << endl;
    }
  }
	return 0;
}
