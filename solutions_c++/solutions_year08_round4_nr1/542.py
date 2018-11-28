#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <utility>
#include <algorithm>
#include <fstream>

using namespace std;

string itoa(int val) {stringstream ss;ss << val;return ss.str();}
typedef vector<int> vi;
typedef pair<int,int> pi;
vi parseInt(string s) {stringstream ss(s);vi ans;while (!ss.eof()) {int temp; ss >> temp; ans.push_back(temp); } return ans;}
#define COPY(x,y) y.resize(x.size());copy(x.begin(),x.end(),y.begin())
#define pb push_back
#define SWAP(t,x,y) t temp=x;x=y;y=temp;
#define ll long long

int m,v,n;
vi types;
bool ch[10000];
bool values[10000];
int dp[20000][5];

#define INF 555555

int calc(int,bool);

int or_calc(int node,bool val1,bool val2) {
	int a = calc(node*2+1,val1);
	int b = calc(node*2+2,val2);
	//if (node==3) {
	//	cout << val1 << " " << val2 << " " << a << " " << b << endl;
	//}
	if (a!=-1 && b!=-1) {
		return a+b;
	}
	return -1;
}

int calc(int node,bool value) {
	if (dp[node][value]!=-10) {
		return dp[node][value];
	}
	int best = INF;
	if (node<n) {
		if (types[node]==0) {
			// OR gate
			if (value==false) {
				int a = or_calc(node,false,false);
				if (a!=-1 && a<best) {
					best = a;
				}
			} else {
				int a = or_calc(node,true,false);
				if (a!=-1 && a<best) {
					best = a;
				}
				a = or_calc(node,false,true);
				if (a!=-1 && a<best) {
					best = a;
				}
				a = or_calc(node,true,true);
				if (a!=-1 && a<best) {
					best = a;
				}
			}
			if (ch[node]) {
				ch[node] = false;
				types[node] = 1;
				int a = calc(node,value);
				if (a!=-1 && (a+1)<best) {
					best = a + 1;
				}
				types[node] = 0;
				ch[node] = true;
			}
		} else {
			// AND Gate
			if (value==true) {
				int a = or_calc(node,true,true);
				if (a!=-1 && a<best) {
					best = a;
				}
			} else {
				int a = or_calc(node,true,false);
				if (a!=-1 && a<best) {
					best = a;
				}
				a = or_calc(node,false,true);
				if (a!=-1 && a<best) {
					best = a;
				}
				a = or_calc(node,false,false);
				if (a!=-1 && a<best) {
					best = a;
				}
			}
			if (ch[node]) {
				ch[node] = false;
				types[node] = 0;
				int a = calc(node,value);
				if (a!=-1 && (a+1)<best) {
					best = a + 1;
				}
				types[node] = 1;
				ch[node] = true;
			}
		}
	} else {
		if (values[node]==value) {
			return 0;
		} else {
			return -1;
		}
	}
	//cout << node << " " << value << " " << best << endl;
	if (best==INF) {
		dp[node][value] = -1;
		return -1;
	}
	dp[node][value] = best;
	return best;
}

int main() {
	int testcases;
	cin >> testcases;
	for(int i=1;i<=testcases;i++) {
		cin >> m >> v;
		n = (m-1)/2;
		types.clear();
		memset(dp,-10,sizeof(dp));
		for(int k=0;k<n;k++) {
			int g,c;
			cin >> g >> c;
			types.pb(g);
			if (c==1) {
				ch[k] = true;
			} else {
				ch[k] = false;
			}
		}
		for(int j=0;j<m;j++) {
			dp[j][0] = -10;
			dp[j][1] = -10;
			dp[j][2] = -10;
		}
		for(int k=n;k<m;k++) {
			int c;
			cin >> c;
			if (c==1) {
				values[k] = true;
			} else {
				values[k] = false;
			}
		}
		int ans = calc(0,v);
		cout << "Case #" << i << ": ";
		if (ans==-1) {
			cout << "IMPOSSIBLE";
		} else {
			cout << ans;
		}
		cout << endl;
	}
	return 0;
}
