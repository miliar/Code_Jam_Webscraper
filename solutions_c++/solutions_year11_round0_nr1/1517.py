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
    int seconds[2];
    int pos[2];
    cin >> n;
    pos[0] = pos[1] = 1;
    seconds[0] = seconds[1] = 0;
    fr(k,0,n) {
      string s;
      int x;
      cin >> s >> x;
      int index = (s=="O"?0:1);
      int posdiff = abs(pos[index]-x);
      int secdiff = max(posdiff - (max(seconds[0],seconds[1]) - seconds[index]),0) + 1;
      seconds[index] = max(seconds[0],seconds[1]) + secdiff;
      pos[index] = x;
    }
    cout << "Case #" << i+1 << ": " << max(seconds[0],seconds[1]) << endl;
  }
	return 0;
}
