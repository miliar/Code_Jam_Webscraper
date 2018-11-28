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

bool cant[500][500];
int dp[500][500];
int w,h;

int calc(int r,int c) {
	if (dp[r][c]!=-1)
		return dp[r][c];
	if (r>w || c>h)
		return 0;
	if (cant[r][c])
		return 0;
	if (r==w && c==h) {
		return 1;
	}
	int ans = calc(r+2,c+1) + calc(r+1,c+2);
	dp[r][c] = ans%10007;
	return dp[r][c];
}

int main() {
	int t;
	
	ifstream fin("d.in");
	ofstream fout("d.ans");
	
	fin >> t;
	
	fr(i,0,t) {
		int R,r,c;
		cl(cant,0); cl(dp,-1);
		fin >> w >> h >> R;
		fr(k,0,R) {
			fin >> r >> c;
			cant[r][c] = true;
		}
		cout << "Case #" << i+1 << ": " << calc(1,1) << endl;
		fout << "Case #" << i+1 << ": " << calc(1,1) << endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}
