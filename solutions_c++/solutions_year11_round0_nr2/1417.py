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
    int n,c,d;
    map<string,char> combine;
    bool oppose[500][500];
    cl(oppose,0);
    
    cin >> c;
    fr(k,0,c) {
      string s;
      cin >> s;
      combine[s.substr(0,2)] = s[2];
      combine[s.substr(1,1)+s.substr(0,1)] = s[2];
    }

    cin >> d;
    fr(k,0,d) {
      string s;
      cin >> s;
      oppose[s[0]][s[1]] = true;
      oppose[s[1]][s[0]] = true;
    }

    cin >> n;
    string list;
    string commands;
    cin >> commands;

    fr(k,0,n) {
      char c = commands[k];
      if (list.size()==0) {
        list.pb(c);
        continue;
      }
      string temp;
      temp.pb(list[list.size()-1]);
      temp.pb(c);
      
      bool combined = false;
      if (combine.find(temp)!=combine.end()) {
        c = combine[temp];
        combined = true;
      }
      
      bool ok = true;
      fr2(j,list) {
        if (oppose[list[j]][c]) {
          ok = false;
          break;
        }
      }
      
      if (ok) {
        if (combined) {
          list[list.size()-1] = c;
        } else {
          list.pb(c);
        }
      } else {
        list = "";
      }
      
    }
    
    string answer = "";
    fr2(k,list) {
      answer = answer + " " + list[k] + ",";
    }
    if (answer.size()<2)
      answer = "  ";
    answer[0] = '[';
    answer[answer.size()-1] = ']';
    
    cout << "Case #" << i+1 << ": " << answer << endl;
  }
	return 0;
}
