#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<sstream>
using namespace std;

#define FOR(i,a,b) for(int i = (a); i < int(b); ++ i)
#define REP(i,n) FOR(i,0,n)
#define sz size()
#define pb push_back
#define cs c_str()
#define V(x) vector< x >

typedef V(int) VI;
typedef V(VI) VVI;
typedef V(string) VS;

int toInt(string s){ int r=0; istringstream sin(s); sin>>r; return r; }

int main() {
	string t;
	int num;
	getline(cin,t);
	num = toInt(t);
		
	REP(z,num) {
		int S, Q, res = 0, sum = 0;
		
		getline(cin,t);
		S = toInt(t);		
		string eng[S];
		REP(i,S) getline(cin,eng[i]);
		getline(cin,t);
		Q = toInt(t);
		
		VI arr(S,0);
		REP(i,Q) {
			string query;
			getline(cin,query);
			REP(j,S) {
				if(query == eng[j] && !arr[j]) {
					if(sum == S-1) {
						res++, sum = 0;
						REP(i,arr.sz) arr[i] = 0;
					}
					sum++, arr[j] = 1;
					break;
				}
			}
		}
		cout << "Case #" << z+1 << ": "<< res <<endl;
	}
	return 0;
}

