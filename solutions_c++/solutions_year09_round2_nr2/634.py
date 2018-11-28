/* Rajat Goel [C++] */
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<sstream>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;
const int    INF =     0x7FFFFFFF;
const double EPS =     1e-7;
typedef pair<int,int>  pii;
typedef long long      int64;
#define loop(i,n)      for(int i=0;i<n;i++)
#define foreach(i,a)   for(typeof((a).begin()) i=(a).begin();i!=(a).end();++i)
#define present(x,in)  (find((in).begin(),(in).end(),x) != (in).end())
#define all(a)         (a).begin(),(a).end()
#define cast(a,b)      { ostringstream myOut; myOut << a ; istringstream myIn ( myOut.str() ); myIn >> b; }
inline int fCMP(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}
int main() {
	int T;
	cin >> T;
	for(int cas=1;cas<=T;cas++) {
		cout << "Case #" << cas << ": ";
		string str;
		cin >> str;
		if (next_permutation(str.begin(), str.end())) {
			cout << str << endl;
		} else {
			sort(str.begin(), str.end());
			int i = 0;
			while(str[i]=='0') i++;
			str = str[i] + str.substr(0, i) + "0" + str.substr(i+1);
			cout << str << endl;
		}
	}
	return 0;
}
