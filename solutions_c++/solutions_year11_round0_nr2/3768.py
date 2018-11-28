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

void pvc(vector<char> v) {
	cout << "[ ";
	for (int i = 0; i < sz(v); i++)
		cout << v[i] << " ";
	cout << " ]" << endl;
}
void pvs(vector<string> v) {
	cout << "[ ";
	for (int i = 0; i < sz(v); i++)
		cout << v[i] << " ";
	cout << " ]" << endl;
}
void prnt(vector<char> v) {
	cout << "[";
	for (int i = 0; i < sz(v); i++) {
		if (i != sz(v) - 1)
			cout << v[i] << ", ";
		else
			cout << v[i];
	}
	cout << "]" << endl;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("B-small-attempt1.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		int C;
		cin >> C;
		vector<string> CV;
		vector<char> CVv;
		for (int x = 0; x < C; x++) {
			string tmp;
			cin >> tmp;
			string ss = tmp.substr(0, 2);
			CV.pb(ss);
			reverse(all(ss));
			CV.pb(ss);

			CVv.pb(tmp[2]);
			CVv.pb(tmp[2]);

		}
	//	pvs(CV);
	//	pvc(CVv);
		int D;
		cin >> D;
		vector<char> DV;
		vector<char> DVv;
		for (int x = 0; x < D; x++) {
			string tmp;
			cin >> tmp;
			DV.pb(tmp[0]);
			DVv.pb(tmp[1]);
			DV.pb(tmp[1]);
			DVv.pb(tmp[0]);

		}
		//pvc(DV);
		//pvc(DVv);
		int N;
		cin >> N;
		string inv;
		string res = "";
		cin >> inv;
		vector<char> fin;
		fin.pb(inv[0]);
		for (int y = 1; y < N; y++) {

			string s1 = convert<char, string> (fin.back());
			string s2 = convert<char, string> (inv[y]);
			if (cpresent(CV,s1+s2)) {
				int indx = find(all(CV),s1+s2)  - CV.begin();
				if(!fin.empty()){fin.pop_back();
				fin.pb(CVv[indx]);
				}

			} else if (cpresent(DV,inv[y])) {
				int indx = find(all(DV),inv[y])  - DV.begin();

				if (cpresent(fin,DVv[indx])) {
					//cerr<<DVv[indx]<<endl;
					fin.clear();
				} else
					fin.pb(inv[y]);

			} else {

				fin.pb(inv[y]);
			}

		}

		cout << "Case #" << i << ": ";
		prnt(fin);
	}

	return 0;
}

