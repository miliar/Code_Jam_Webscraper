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
  int T;
  cin >> T;
  fr(i,0,T) {
    long long l,t,n,c;
    cin >> l >> t >> n >> c;
    vector<long long> a;
    fr(k,0,c) {
      long long x;
      cin >> x;
      a.pb(x);
    }
    
    long long time = 0;
    vector<long long> save;
    fr(k,0,n) {
      long long dist = a[k%c];
      if (t<=time) {
        save.pb(dist);
      } else if (t<time+dist*2) {
        save.pb(dist*2 - ((t-time) + (dist-(t-time)/2)));
      }
      time += dist*2;
    }
    
    sort(save.begin(),save.end());
    reverse(save.begin(),save.end());
    fr(k,0,l)
      time -= save[k];
    
    cout << "Case #" << i+1 << ": " << time << endl;
  }
	return 0;
}
