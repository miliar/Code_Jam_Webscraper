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

void putCombi(vector<vector<int> >& vc, string s) {
	int e1 = s[0] - 'A', e2 = s[1] - 'A', c = s[2] - 'A';
	vc[e1][e2] = c;
	vc[e2][e1] = c;
}
void putOpp(vector<int>& vd, vector<vector<int> >& vdd, string s) {
	int e1 = s[0] - 'A', e2 = s[1] - 'A';
	vdd[e1][e2] = 1;
	vdd[e2][e1] = 1;
}
int getCombi(vector<vector<int> >& vc, char e1, char e2) {
	return vc[e1-'A'][e2-'A'];
}
int getOpp(vector<int>& vd, vector<vector<int> >& vdd, char e) {
	f(i,0,vd.size()) {
		if(vd[i] > 0) {
			if(vdd[i][e-'A'] > 0)
				return 1;
			if(vdd[e-'A'][i] > 0)
				return 1;
		}
	}
	return -1;
}

int main() {
	int T, C, D, N;
	string s;

	ifstream infile;
	ofstream outfile;
	infile.open("B-large.in");
	outfile.open("B-out-large.in");
	infile >> T;
	//cin >> T;

	fe(t, 1, T) {
		//infile >> N;
		vector<vector<int> > vc(26, vector<int>(26,-1));
		vector<int> vd(26, 0);
		vector<vector<int> > vdd(26, vector<int>(26,-1));

		infile >> C;
		//cin >> C;
		f(c, 0, C) {
			infile >> s;
			//cin >> s;
			putCombi(vc, s);
		}
		infile >> D;
		//cin >> D;
		f(d, 0, D) {
			infile >> s;
			//cin >> s;
			putOpp(vd, vdd, s);
		}
		vector<char> res;
		infile >> N;
		infile >> s;
		//cin >> N;
		//cin >> s;
		res.push_back(s[0]);
		vd[s[0]-'A'] += 1;
		f(i, 1, s.length()) {
			char now = s[i];
			//cout << now << endl;
			bool combi = false;
			if(res.size() > 0) {
				char last = res[res.size()-1];
				int comb = getCombi(vc, now, last);
				if(comb >= 0) {
					res.pop_back();
					vd[last - 'A'] -= 1;
					res.push_back('A' + comb);
					//cout << last << " + " << now << " = " << (char)('A'+comb) << endl;
					combi = true;
				}
			}
			bool opp = false;
			if(!combi) {
				if(getOpp(vd, vdd, now) > 0) {
					//cout << "Clear All" << endl;
					res.clear();
					fill(all(vd), 0);
					opp = true;
				}
			}
			if(!combi && !opp) {
				//cout << "Push Back" << endl;
				res.push_back(now);
				vd[now-'A'] += 1;
			}
		}
		outfile << "Case #" << t << ": [";
		//cout << "Case #" << t << ": [";
		f(i, 0, res.size()) {
			outfile << res[i];
			//cout << res[i];
			if(i < res.size() - 1)
				outfile << ", ";
				//cout << ", ";
		}
		outfile << "]" << endl;
		//cout << "]" << endl;
	}

	return 0;
}