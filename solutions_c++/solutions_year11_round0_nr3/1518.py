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
    
    vector<long long> vals;
    
    fr(k,0,n) {
      long long x;
      cin >> x;
      vals.pb(x);
    }
    
    long long answer = -1;
    
    long long correct[2];
    long long wrong[2];
    
    fr(k,0,n) {
      correct[0] = correct[1] = 0;
      wrong[0] = wrong[1] = 0;
      fr(j,0,n) {
        int x = (k==j)?1:0;
        wrong[x] = wrong[x] ^ vals[j];
        correct[x] = correct[x] + vals[j];
      }
      if (wrong[0]==wrong[1])
        answer = max(answer,max(correct[0],correct[1]));
    }

    fr(k,0,n-1) {
      correct[0] = correct[1] = 0;
      wrong[0] = wrong[1] = 0;
      fr(j,0,n) {
        int x = (j<=k)?1:0;
        wrong[x] = wrong[x] ^ vals[j];
        correct[x] = correct[x] + vals[j];
      }
      if (wrong[0]==wrong[1])
        answer = max(answer,max(correct[0],correct[1]));
    }
    
    cout << "Case #" << i+1 << ": ";
    if (answer == -1) {
      cout << "NO";
    } else {
      cout << answer;
    }
    cout << endl;
  }
	return 0;
}
