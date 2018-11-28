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

int main() {
	int T;
	ifstream infile;
	ofstream outfile;
	infile.open("B-large.in");
	outfile.open("Qual-B-large.out");
	infile >> T;
	fe(t, 1, T) {
		int N, S, P;
		infile >> N >> S >> P;
		vector<int> v(N,-1);
		f(i,0,N) infile >> v[i];
		vector<bool> vc(N,false);
		f(i,0,N) {
			int base = (v[i]==0)?0:(v[i]/3);
			int rest = (v[i]==0)?0:(v[i]%3);
			if(base >= P || (rest > 0 && base+1 >= P)) vc[i] = true;
		}
		f(i,0,N) {
			if(S <= 0) break;
			if(vc[i]) continue;
			int base = (v[i]==0)?0:(v[i]/3);
			int rest = (v[i]==0)?0:(v[i]%3);
			switch(rest) {
			case 0:
				if(base+1 >= P && base > 0) { vc[i] = true; S--; }
				break;
			case 2:
				if(base+2 >= P) { vc[i] = true; S--; }
				break;
			}
		}
		int res = count(all(vc), true);

		outfile << "Case #" << t << ": " << res << endl;;
		cout << "Case #" << t << ": " << res << endl;;
	}

	return 0;
}