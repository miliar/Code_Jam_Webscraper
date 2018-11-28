#include <string>
#include <vector>
#include <iostream>
#include <fstream>

using namespace std;

#define forn(i,n) for(int i=0;i<int(n);++i)
const int INF = 1000*1000*1000;
int best[105][1005];
vector<string> sites;
vector<string> qs;
bool can(int i, int j){
	return sites[i]!=qs[j];
}
string dummy;
int main(){
	int N; cin >> N;
	forn(c, N){
		int n; cin >> n;
		vector<int> x(n), y(n);
		forn(i, n)cin >> x[i];
		forn(i, n)cin >> y[i];
		int m = INF;
		vector<int> o(n);
		forn(i,n)o[i]=i;
		do{
			int r=0;
			forn(i, n)r+=x[o[i]]*y[i];
			m = min(m, r);
		}while(next_permutation(o.begin(), o.end()));
		cout << "Case #" << c+1 << ": " << m << endl;
	}
	return 0;
}
