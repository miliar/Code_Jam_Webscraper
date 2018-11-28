//A.cpp
//_are89
#include <functional>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <map>
#include <set>

using namespace std;

#define sz(a) int((a).size())
#define pb push_back
#define mp make_pair
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i=(c).begin(); i!=(c).end();i++)
#define present(c,x)  ( (c).find(x) !=(c).end())
#define cpresent(c,x) (find(all(c),x)!= (c).end() )
#define minEI(x)  min_element(x.begin(),x.end())-(x).begin()
#define maxEI(x)  max_element(x.begin(),x.end())-(x).begin()

#define UNS(v)     sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define acuSum(x)  accumulate(x.begin(),x.end(),0)
#define acuMul(x)  accumulate(x.begin(),x.end(),1, multiplies<int>()); 
#define bits(x)     __builtin_popcount( x )

template<class F, class T> T convert(F input, int width = 0, int prec = -1) {
	stringstream A;
	T res;
	if (prec > -1)
		A << fixed << setprecision(prec);
	A << setw(width) << setfill('0') << input;
	A >> res;
	return res;
}

vector<string> split(string s) {
	stringstream A(s);
	vector<string> res;
	string t;
	while (A >> t)
		res.push_back(t);
	return res;
}
bool chk(vector<string> v) {
	for (int i = 0; i < sz(v); i++)
		for (int j = 0; j < sz(v[i]); j++) {
			if (v[i][j] == '#')
				return false;
		}
	return true;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "rt", stdin);
	freopen("output_A_L.txt", "wt", stdout);
#endif
	int tests;
	cin >> tests;
	for (int tc = 1; tc <= tests; tc++) {
		int r;
		int c;
		cin >> r >> c;
		vector<string> v;
		for (int i = 0; i < r; i++) {
			string s;
			cin >> s;
			v.pb(s);
		}
		for (int i = 0; i < sz(v) - 1; i++) {
			for (int j = 0; j < sz(v[i]); j++) {
				if (v[i][j] == '#' && v[i][j + 1] == '#' && v[i + 1][j] == '#'&& v[i + 1][j + 1] == '#')
				{
					v[i][j]= '/';
					v[i][j+1]='\\';
				    v[i+1][j]='\\';
				    v[i+1][j+1]='/';
			}
		}
	}
		if(!chk(v))cout<<"Case #"<<tc<<":"<<endl<<"Impossible"<<endl;
		else
		{cout<<"Case #"<<tc<<":"<<endl;
			for(int i=0;i<sz(v);i++)
			{
				for(int j=0;j<sz(v[i]);j++)
				{
					cout<<v[i][j];
				}
				cout<<endl;
			}
		}

}

return 0;
}

