#include <map>
#include <set>
#include <math.h>
#include <deque>
#include <stack>
#include <queue>
#include <vector>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <memory.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()
#define rep(i,s,m) for(int i=s;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define PI = (2.0 * acos(0.0));
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)

vector<set<string> > v;
void tokenize(string s) {
	s = s.substr(1);
	string temp = "";
	//cout<<"S"<<s<<endl;
	set<string> st;
	int i = 0;
	int ind = s.find("/");
	while (ind != -1) {
	//	cout<<s.substr(0,ind)<<endl;
		if (((int) v.size()) <= i)
			v.push_back(st);//v.push_back(s);
		temp+="/"+s.substr(0, ind);
		//cout<<temp<<endl;
		v[i].insert(temp);
		s = s.substr(ind + 1);
		i++;
		ind = s.find("/");
	}
	temp+="/"+s.substr(0, ind);
	if (((int) v.size()) <= i)
		v.push_back(st);//v.push_back(s);
	v[i].insert(temp);
}
int main() {

	freopen("A.in", "rt", stdin);
	freopen("A.out", "wt", stdout);
	int t = 0, n, m, T;
	string path = "";
	cin >> T;
	while (t++ < T) {
		v.clear();
		int cnt1 = 0 , cnt2 = 0;
		cin >> n >> m;
		for (int i = 0; i < n; i++) {
			cin >> path;
			tokenize(path);
		}
		for (int i = 0; i <(int) v.size(); i++)
			cnt1 += v[i].size();
		//cout<<cnt1<<endl;
		for (int i = 0; i < m; i++) {
					cin >> path;
					tokenize(path);
				}
		for (int i = 0; i <(int) v.size(); i++)
					cnt2 += v[i].size();
		//cout<<cnt2<<endl;
		printf("Case #%d: %d\n", t, cnt2-cnt1);
	}
	//  system("pause");
	return 0;
}
