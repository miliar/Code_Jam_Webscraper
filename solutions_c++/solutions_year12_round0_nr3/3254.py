#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <sstream>

using namespace std;

#define pb push_back
#define mp make_pair
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define REP(i,j,k) for(int i=j;i<(int)(k);++i)
#define foreach(i,c) for(__typeof(c.begin()) i=c.begin();i!=c.end();++i)
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef long long ll;
const int INF = 99999999;
const double EPS = 1e-9;

int n,a,b;
bool res[2000001];


int main()
{
	cin >> n;
	rep(i,n){
		rep(j,2000001) res[j]=false;
		int ans = 0;
		vector<pii> v;
		cin >> a >> b;
		REP(j,a,b+1)if(!res[j]){
			res[j]=true;
			stringstream ss;
			string s;
			ss << j;
			ss >> s;
			rep(k,s.size()-1){
				string s1;
				rep(l,s.size()-1) s1+=s[l+1];
				s1+=s[0];
				s=s1;
				stringstream si;
				int in;
				si << s;
				si >> in;
				if(!res[in]&&a<=in&&in<=b&&j<in) v.pb(pii(j,in));
			}
		}
		sort(all(v));
		if(v.size()!=0) ans++;
		rep(j,v.size()-1)if(v[j]!=v[j+1]) ans++;
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}
