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
    int c,d;
    cin >> c >> d;
    vector<double> pos;
    fr(k,0,c) {
      int p,x;
      cin >> p >> x;
      fr(j,0,x)
        pos.pb(p);
    }
    c = pos.size();
    double time = 0;
    double diff = 0.00001;
    //cout << diff << endl;
    while(true) {
      vector<double> p;
      COPY(pos,p);
      p[0] -= time;
      bool ok = true;
      fr(k,1,c) {
        float xx = p[k-1]+d;
        if (abs(xx-p[k])<=time) {
          p[k] = xx;
        } else {
          if (xx <= p[k]) {
            p[k] -= time;
          } else {
            p[k] += time;
          }
        }
        if (abs(p[k-1]-p[k])<d) {
          ok = false;
          break;
        }
      }
      if (ok) {
      //  fr(k,0,c)
      //    cout << p[k] << endl;
      //  cout << endl;
      }
      if (ok) break;
      time += diff;
      // cout << time << endl;
    }
    cout << "Case #" << i+1 << ": " << time << endl;
  }
	return 0;
}
