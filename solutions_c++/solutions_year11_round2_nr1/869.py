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
    int n;
    cin >> n;
    string g[200];
    fr(k,0,n) {
      cin >> g[k];
    }
    long long wpt[200];
    long long wpb[200];
    fr(k,0,n) {
      int total = 0;
      int wins = 0;
      fr(j,0,n) {
        if (g[k][j]=='.') continue;
        if (g[k][j]=='1') {
          wins++;
        }
        total++;
      }
      wpt[k] = wins;
      wpb[k] = total;
    }
    float owpt[200];
    long long owpb[200];
    fr(k,0,n) {
      float allWps = 0;
      int cnt = 0;
      fr(a,0,n) {
        if (g[a][k]=='.') continue;
        int total = 0;
        int wins = 0;
        fr(b,0,n) {
          if (g[a][b]=='.') continue;
          if (b==k) continue;
          if (g[a][b]=='1') wins++;
          total++;
        }
        allWps += (float)wins/(float)total;
        cnt++;
      }
      owpt[k] = allWps;
      owpb[k] = cnt;
    }
    float oowpt[200];
    long long oowpb[200];
    fr(k,0,n) {
      int cnt = 0;
      float all = 0;
      fr(j,0,n) {
        if (g[k][j]=='.') continue;
        all += owpt[j]/(float)owpb[j];
        cnt++;
      }
      oowpt[k] = all;
      oowpb[k] = cnt;
    }
    
    cout << "Case #" << i+1 << ": " << endl;
    fr(k,0,n) {
      float rpi = wpt[k]/(4*(float)wpb[k]) + owpt[k]/(2*(float)owpb[k]) + oowpt[k]/((float)oowpb[k]*4);
      cout << setprecision(12) << rpi << endl;
    }
  }
	return 0;
}
