/*
 * Template for code jam - different includes and templates
 * Real task code is in the end
 * Mikhail Dektyarow <mihail.dektyarow@gmail.com>, 2009
 */
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#include <iostream>
#include <string>
using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)
#define REPD(i, n) for (int i((n)-1); i >= 0; --i)
#define ALL(c) (c).begin(), (c).end()

/*
 * complex code:)
 */
template<typename T> void remin(T& a, const T& b) { if (b < a) a = b; }
template<typename T> void remax(T& a, const T& b) { if (b > a) a = b; }
template<class T1, class T2>inline istream& operator>> (istream& s, pair<T1, T2> &p) {	return s >> p.first >> p.second;}
template<class T1, class T2>inline ostream& operator<< (ostream& s, const pair<T1, T2>p) {	return s << "(" << p.first << " " << p.second << ")";}
template<class T1>inline ostream& operator<< (ostream& s, const vector<T1> container) {
	for (typename vector<T1>::const_iterator i = container.begin(); i != container.end(); i++) {
		s << *i << " ";
	}
	return s;
}
template<class T1>inline istream& operator>> (istream&s, vector<T1> &container) {
	for (typename vector<T1>::iterator i = container.begin(); i != container.end(); i++) {
		s >> *i;
	}
	return s;
}
typedef pair<int,int> ipair;
typedef long long int int64;
template<class T>T euclid(T a, T b, T &x, T &y) {
	if (b > a)
		swap(a, b);
	if (b == 0) {
		x = 1;
		y = 0;
		return a;
	}
	T x2 = 1, x1 = 0, y2 = 0, y1 = 1, q, r;
	while (b > 0) {
		q = a / b;
		r = a - q * b;
		x = x2 - q * x1;
		y = y2 - q * y1;
		a = b;
	   	b = r;
		x2 = x1; x1 = x;
	   	y2 = y1;
		y1 = y;
	}
	x = x2;
	y = y2;
	return a;
}

/*
 * Real code
 */

void convert_to(vector<int> &ch, int base, int num) {
	REP(i, ch.size()) {
		ch[i] = num % base;
		num /= base;
	}
}
int convert_from(vector<int> &ch, int base) {
	int res, base1;
	res = 0;
	base1 = 1;
	REP(i, ch.size()) {
		res += ch[i]*base1;
		base1 *= base;
	}
	return res;
	//cout << "conf_from: " << ch << ": " << res 
}
void change(vector<int> &ch, int base) {
	int sum;
	sum = 0;
	REP(i, ch.size()) {
		sum += ch[i]*ch[i];
	}
	convert_to(ch, base, sum);
}
int is_happy(int num, int base) {
	set<int> was;
	vector<int> ch(20);
	convert_to(ch, base, num);
	int flag, cur;
	flag = 0;
	//cout << "num " << num << " base " << base << "\n";
	while (!flag) {
		cur = convert_from(ch, base);
		//cout << ch << ": " << cur << "\n";
		if (was.count(cur))
			break;
		was.insert(cur);
		flag = ch[0] == 1;
		for (int i=1; i<20; i++) {
			flag = flag && !ch[i];
		}
		if (flag) {
			break;
		}
		change(ch, base);
	}
	return flag;
}

int main(void) {
	vector<set<int> > happies(20);
	int flag;
	//for (int cur=2; cur < 1000000; cur++) {
		//flag = 1;
		//for (int i=2; i<=9; i++) {
			//if (!is_happy(cur, i)) {
				//flag = 0;
				//break;
			//}
		//}
		//if (flag) {
			//cout << cur << "\n";
			//break;
		//}
	//}
	//return 0;
	int T;
	char c[100];
	cin >> T;
	cin.getline(c, 10, '\n');
	REP(i, T) {
		cin.getline(c, 200, '\n');
		char cur[50];
		vector<int> bases;
		int cpos;
		cpos = 0;
		REP(j, strlen(c)) {
			if (c[j] == ' ') {
				cur[cpos] = 0;
				bases.push_back(atoi(cur));
				cpos = 0;
			}
			else {
				cur[cpos++] = c[j];
			}
		}
		cur[cpos] = 0;
		bases.push_back(atoi(cur));
		int flag;
		cout << "Case #" << i+1 << ": ";
		for (int cur=2; cur < 100000; cur++) {
			flag = 1;
			REP(j, bases.size()) {
				if (!is_happy(cur, bases[j])) {
					flag = 0;
					break;
				}
			}
			if (flag) {
				cout << cur << "\n";
				break;
			}
		}
	}
	return 0;
}
