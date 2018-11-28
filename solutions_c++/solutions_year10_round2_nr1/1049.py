#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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


using namespace std;

#define INF 999999
#define pb push_back
#define sz(x) ((int)((x).size()))
#define all(x) (x).begin(),(x).end()
#define db double
#define ll long long
#define rep(i,n) for (int (i)=0; (i)<(n); ++(i))
#define forn(i,a,n) for (int (i)=(a); (i)<(n); ++(i))
#define VI vector<int>
#define VB vector<bool>
string s;
#define Tr data *
#define PSD pair<string,Tr>
#define VPSD vector<PSD >
struct data{
	VPSD uk;
};
Tr root;
void init(Tr p = root){
	rep(i,sz(p->uk))
		init(p->uk[i].second);
	delete p;
}
string sub;
int ans;
void add(bool Mode,Tr p = root){
	sub.clear();
	int pos = 0;
	int n = sz(s);
	while (pos < n && s[pos] != '/')
		++pos;
	if (pos == 0)
		return;
	sub = s.substr(0,pos);
	if (pos != n)
		s.erase(0,pos+1);
	else
		s.erase(0,pos);
	rep(i,sz(p->uk))
		if (p->uk[i].first == sub){
			add(Mode,p->uk[i].second);
			return;
		}
	Tr x = new data;
	p->uk.push_back(PSD(sub,x));
	if (Mode)
		++ans;
	add(Mode,x);
}
int main(){
	freopen("input.txt","rt",stdin); freopen("output.txt","wt",stdout);
	int T;
	cin >> T;
	root = new(data);
	rep(qwer,T){
		init();
		root = new(data);
		int n,m;
		ans = 0;
		cin >> n >> m;
		rep(i,n){
			cin >> s;
			s = s.erase(0,1);
			add(false);
		}
		rep(i,m){
			cin >> s;
			s = s.erase(0,1);
			add(true);
		}
		printf("Case #%d: %d\n",qwer+1,ans);
	}
	return 0;
}