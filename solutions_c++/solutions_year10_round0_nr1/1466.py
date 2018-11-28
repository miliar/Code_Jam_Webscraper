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

int main() {
	int t;
	
	ifstream fin("a.in");
	ofstream fout("a.ans");
	
	fin >> t;
	
	fr(i,0,t) {
    int n,k;
    fin >> n >> k;
    string res = "OFF";
    int x = (1<<n)-1;
    if (k%(x+1)==x) {
      res = "ON";
    }
		cout << "Case #" << i+1 << ": " << res << endl;
		fout << "Case #" << i+1 << ": " << res << endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}
