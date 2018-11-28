#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <sstream>
#include <fstream>
#include <queue>

using namespace std;

#define forn(i, n) for(int i = 0; i<(int)(n); i++)
#define forsn(i, m, n) for(int i = (int)(m); i<(int)(n); i++)
#define si(x) x.size()
#define mp make_pair
#define pb push_back
#define all(x) x.begin(),x.end()

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef pair<int, ii> iii;
typedef vector<vi> vvi;

typedef long long int tint;

const int maxl = 300000 + 1000;
const int maxn = 1000 + 100;

int t, n;

queue<ii> op1, op2;

int main(){
	cin >> t;
	forn(tt, t){
		cin >> n;
		forn(i, n){
			char c; int ea; cin >> c >> ea;
			if(c == 'O') op1.push(mp(i, ea));
			else op2.push(mp(i, ea));
		}	
		
		int pos1 = 1, pos2 = 1;
		
		int res = 0;
		
		forn(i, n){
			if(op1.empty() || (!op2.empty() && op1.front().first > op2.front().first)){
				swap(pos2, pos1);
				swap(op1, op2);
			}
			ii act = op1.front(); op1.pop();
			int d = abs(act.second - pos1) + 1;
			
			res += d;
			pos1 = act.second;
			if(abs(pos2 - op2.front().second) <= d) pos2 = op2.front().second;
			else if(pos2 < op2.front().second) pos2 += d;
			else pos2 -= d;
		}
		
		cout << "Case #" << tt+1 << ": " << res << endl;
	}	
	return 0l;
}
