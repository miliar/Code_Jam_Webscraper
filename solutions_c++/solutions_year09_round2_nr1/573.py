#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <numeric>
#define beg 10000000
#define pb push_back
#define mp make_pair
#define sz(x) (int)x.size()
#define ss stringstream
#define pf pop_front()
#define nd second
#define st first
#define fr(i, n) for(int i = 0; i < (int)n; i++)
#define LL long long
#define vi vector<int>
#define pii pair<int, int>
#define vii vector<pii >
#define vs vector<string>
#define LD long double

using namespace std;

//always reset global variables!

string prop[200000];
LD prob[200000];

int par(int x) { return x/2; }
int left(int x) { return 2*x; }
int right(int x) { return 2*x + 1; }

void buildTree(string s, int a) {
	s = s.substr(1, sz(s) - 2);
//	cout << s << endl;
	ss input(s);
	string p;
	double t;
	input >> t;
	input >> p;
	prob[a] = t;
	prop[a] = p;
	int cnt = 0;
	int kur = 0;
	vs v;
	fr(i, sz(s)) {
		if(s[i] == '(') {
			if(cnt == 0) kur = i + 1;
			cnt++;
		}
		if(s[i] == ')') {
			cnt--;
			if(cnt == 0) {
				v.pb(s.substr(kur - 1, i - kur + 2));
			}
		}
	}
	if(prop[a] != "") {
		buildTree(v[0], left(a));
		buildTree(v[1], right(a));
	}
}

void solveCase(int Case) {
	cout << "Case #" << Case << ":" << endl;
	int L;
	cin >> L;
	string tree("");
	string s;
	getline(cin, s);
	fr(i, L) {
		getline(cin, s);
		tree += s;
	}
	buildTree(tree, 1);
	int A;
	cin >> A;
	fr(i, A) {
		string name;
		cin >> name;
		int how_many;
		cin >> how_many;
		set<string> P;
		fr(j, how_many) {
			string temp;
			cin >> temp;
			P.insert(temp);
		}
		double ans = 1;
		int kur = 1;
		 do {
//		 	cout << name << " " << kur << endl;
			ans *= prob[kur];
			if(prop[kur] == "") break;
			if(P.find(prop[kur]) != P.end()) kur = left(kur); else kur = right(kur);
		} while(true);
		printf("%.7lf\n", ans);
	}
}

int main() {
	int N;
	cin >> N;
	fr(i, N) solveCase(i + 1);
	return 0;
}
