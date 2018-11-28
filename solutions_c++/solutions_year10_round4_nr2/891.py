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
#include <fstream>
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
#define ll long long
#define INF 1000000000


int p;
int m[1200];
int w[1200];
int prices[15][1200];
bool used[15][1200];

void add(int pos) {
  int x = pos/2;
  int r = 0;
  while(!used[r+1][x/2]) {
    if (r==p-1) break;
    x = x/2;
    r++;
  }
  used[r][x] = true;
  int n = 1<<(r+1);
  int s = (pos/n)*n;
  fr(i,s,s+n) {
    w[i]++;
  }
}

int calc() {
  int n = 1<<p;
  int ans = 0;
  fr(i,0,n) {
    while ((p-w[i])>m[i]) {
      add(i);
      ans++;
    }
  }
  return ans;
}

int main() {
	int t;
	
	ifstream fin("b.in");
	ofstream fout("b.ans");
	
	fin >> t;
	
	fr(x,0,t) {
    fin >> p;
    int n = 1<<p;
    cl(m,0);
    cl(used,0);
    cl(w,0);
    fr(i,0,n) {
      fin >> m[i];
    }
    fr(k,0,p) {
      n=n/2;
      fr(i,0,n) {
        fin >> prices[k][i];
      }
    }
    int res = calc();
		cout << "Case #" << x+1 << ": " << res << endl;
		fout << "Case #" << x+1 << ": " << res << endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}
