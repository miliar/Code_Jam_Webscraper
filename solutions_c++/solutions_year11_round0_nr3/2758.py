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
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define pb push_back
#define mp make_pair
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
#define f(i,a,b) for(int i=(a);i<(b);++i)
#define fr(i,a,b) for(int i=(a);i>(b);--i)
#define fe(i,a,b) for(int i=(a);i<=(b);++i)
#define fre(i,a,b) for(int i=(a);i>=(b);--i)
string itoa(int i) { stringstream ss; ss<<i; return ss.str(); }
#define same(a,b) (fabs((a)-(b))<0.0000001)
#define even(a) ((a)%2==0) 
#define odd(a)  ((a)%2==1)
#define present(c,x) ((c).find(x) !=(c).end())
#define cpresent(c,x) (find(all(c),x)) 
#define LIMIT_BOUND 15

bool possSplit(const vector<int>& v) {
	f(i,0,v.size()) {
		if(odd(v[i]))
			return false;
	}
	return true;
}

bool possSplit(const vector<int>& vs, const vector<int>& vp) {
	f(i,0,vs.size()) {
		if(vs[i]%2 != vp[i]%2)
			return false;
	}
	return true;
}

bool possSplit(const vector<int>& vs, const vector<int>& vp, int digit) {
	f(i,digit,vs.size()) {
		if(vs[i]%2 != vp[i]%2)
			return false;
	}
	return true;
}

vector<int> candy;

bool checkPoss(bitset<LIMIT_BOUND> state, int index, int digit) {
	vector<int> vs(20, 0), vp(20, 0);
	f(i,0,candy.size()) {
		int c = candy[i];
		int k = 0;
		if(state[i]) {
			while(c > 0) {
				vs[k] += c % 2;
				c /= 2;
				k++;
			}
		}
		else {
			while(c > 0) {
				vp[k] += c % 2;
				c /= 2;
				k++;
			}
		}
	}
	if(possSplit(vs, vp, digit)) {
		//cout << "Possible" << endl;
		return true;
	}
	//cout << "Impossible" << endl;
	return false;
}
long long getScore(bitset<LIMIT_BOUND> state) {
	vector<int> vs(20, 0), vp(20, 0);
	bool sh = false, sp = false;
	f(i,0,candy.size()) {
		int c = candy[i];
		int k = 0;
		if(state[i]) {
			while(c > 0) {
				vs[k] += c % 2;
				c /= 2;
				k++;
			}
			sh = true;
		}
		else {
			while(c > 0) {
				vp[k] += c % 2;
				c /= 2;
				k++;
			}
			sp = true;
		}
	}
	if(sh && sp && possSplit(vs, vp)) {
		long long score = 0;
		f(i,0,candy.size()) {
			if(state[i]) score += candy[i];
		}
		//cout << "Score: " << score << endl;
		return score;
	}
	//cout << "Impossible" << endl;
	return 0;
}

int getBinaryDivide(int a, int b) {
	int res = 0;
	//cout << "Check " << a << " " << b << ": ";
	while(a > 0 && b > 0) {
		res++;
		a /= 2; b /= 2;
	}
	if(a > 0) {
		//cout << res << endl;
		return res;
	}
	//cout << "Same" << endl;
	return 0;
}
long long res = 0;
long long solve(int i, bitset<LIMIT_BOUND> state) {
	//cout << i << ": " << state.to_string() << endl;
	if(i >= candy.size()) {
		//cout << "Last Get Score" << endl;
		res = max(res, getScore(state));
		return res;
	}
	if(i > 0) {
		int prev = candy[i-1];
		int now = candy[i];
		int divide = getBinaryDivide(prev, now);
		if(!checkPoss(state, i, divide))
			return 0;
	}
	res = max(res, solve(i+1, state));
	state[i] = 1;
	res = max(res, solve(i+1, state));
	return res;
}

int main() {
	int T, C, N;

	ifstream infile;
	ofstream outfile;
	infile.open("C-small-attempt0.in");
	outfile.open("C-out-small.in");
	infile >> T;
	//cin >> T;

	fe(t, 1, T) {
		infile >> N;
		//cin >> N;

		vector<int> v(20, 0);
		candy.clear();
		f(n, 0, N) {
			infile >> C;
			//cin >> C;
			candy.push_back(C);
			int i = 0;
			while(C > 0) {
				v[i] += C % 2;
				C /= 2;
				i++;
			}
		}
		sort(all(candy), greater<int>());
		res = 0;
		if(possSplit(v)) {
			bitset<LIMIT_BOUND> bs;
			bs.reset();
			res = solve(0, bs);
		}
		outfile << "Case #" << t << ": ";
		//cout << "Case #" << t << ": ";
		if(res == 0) 
			outfile << "NO" << endl;
			//cout << "NO" << endl;
		else 
			outfile << res << endl;
			//cout << res << endl;
	}

	return 0;
}