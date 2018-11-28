#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <ctime>
#include <cmath>
#include <memory>
#include <cstring>
#include <utility>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
using namespace std;

typedef long long int LL;
typedef long double LD;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<string> VS;
typedef set<int> SI;
typedef map<int,int> MII;
typedef pair<int,int> II;
typedef vector<II> VII;
typedef vector<VII> VVII;
typedef vector<LL> VL;
typedef vector<VL> VLL;
typedef set<LL> SL;
typedef map<LL,LL> MLL;
typedef pair<LL,LL> LLL;
typedef vector<LD> VD;
typedef vector<VD> VVD;

template<typename T>
inline T sqr(const T &a){return a*a;}

string itoa(int a) {
	string res;
	while (a>0) {
		res+=a%10+'0';
		a/=10;
	}
	reverse(res.begin(),res.end());
	return res;
}

int testcounter=0;
ofstream ouf;

template <typename T>
void print(T s) {
	testcounter++;
	cout << "Case #" << testcounter << ": " << s << endl;
	ouf << "Case #" << testcounter << ": " << s << endl;
}

void precalc() {
}

void solve() {
	VVI reac(26,VI(26,-1));
	VVI opp(26,VI(26,0));
	VI st;
	int n;
	cin >> n;
	for (int i=0;i<n;i++) {
		string s;
		cin >> s;
		s[0]-='A';
		s[1]-='A';
		s[2]-='A';
		reac[s[0]][s[1]]=s[2];
		reac[s[1]][s[0]]=s[2];
	}
	cin >> n;
	for (int i=0;i<n;i++) {
		string s;
		cin >> s;
		s[0]-='A';
		s[1]-='A';
		opp[s[0]][s[1]]=1;
		opp[s[1]][s[0]]=1;
	}
	cin >> n;
	string s;
	cin >> s;
	for (int i=0;i<n;i++) {
		s[i]-='A';
		st.push_back(s[i]);
		if (st.size()>=2 && reac[st[st.size()-1]][st[st.size()-2]]!=-1) {
			char add=reac[st[st.size()-1]][st[st.size()-2]];
			st.pop_back();
			st.pop_back();
			st.push_back(add);
		} else {
			for (int l=0;l<st.size();l++)
				for (int r=l+1;r<st.size();r++) 
				 if (opp[st[l]][st[r]])
					st.clear();
		}
	}
	string res="[";
	for (int i=0;i<st.size();i++) {
		res+=char(st[i]+'A');
		if (i+1<st.size()) res+=", ";
	}
	res+=']';
	print(res);
}

int main () {
//	ios_base::sync_with_stdio=0;
	freopen("B-large.in","r",stdin);
	ouf.open("output.txt");
	precalc();
	int n;
	cin >> n;
	for (int i=0;i<n;i++) solve();
}
