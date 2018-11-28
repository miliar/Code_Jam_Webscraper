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
#include <fstream>

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
#define ll long long
#define INF 1000000000

int R,K,N;
vector<int> groups;
int dp[2000];
int dp2[2000];

long long calc() {
  int pos = 0;
  long long money = 0;
  fr(i,0,R) {
    int cur = 0;
    int spos = pos;
    if (dp[pos]==-1) {
      while((groups[pos]+cur)<=K) {
        cur += groups[pos];
        pos++;
        pos = pos%N;
        if (pos==spos) break;
      }
      dp[spos] = pos;
      dp2[spos] = cur;
    } else {
      pos = dp[spos];
      cur = dp2[spos];
    }
    money += cur;
  }
  return money;
}

int main() {
	int t;
	
	ifstream fin("c.in");
	ofstream fout("c.ans");
	
	fin >> t;
	
	fr(i,0,t) {
    groups.clear();
    cl(dp,-1);
    cl(dp2,0);
    fin >> R >> K >> N;
    fr(k,0,N) {
      int x;
      fin >> x;
      groups.pb(x);
    }
    long long ans = calc();
		cout << "Case #" << i+1 << ": " << ans << endl;
		fout << "Case #" << i+1 << ": " << ans << endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}
