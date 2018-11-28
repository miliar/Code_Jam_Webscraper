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
const int    INF =     0x0FFFFFFF;
const double EPS =     1e-7;
typedef pair<int,int>  pii;
typedef long long      LL;
typedef long double    LD;
#define loop(i,n)      for(int i=0;i<n;i++)
#define foreach(i,a)   for(typeof((a).begin()) i=(a).begin();i!=(a).end();++i)
#define present(x,in)  (find((in).begin(),(in).end(),x) != (in).end())
#define all(a)         (a).begin(),(a).end()
#define cast(a,b)      { ostringstream myOut; myOut << a ; istringstream myIn ( myOut.str() ); myIn >> b; }
inline int fCMP(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}
char arr[100][100];int n;
vector<int> last;

int main() {
	int T;cin >> T;
	for (int cas=1;cas<=T;cas++) {
		printf("Case #%d: ", cas);
		cin>>n;
		last.resize(n);
		last.assign(n,0);
		loop(i,n)loop(j,n) {
			cin >> arr[i][j];
			if (arr[i][j]=='1') last[i]=j;
		}
		int ans = 0;
		loop(i,n) {
			int index=i;
			while(last[index]>i)index++;
			int tmp = last[index];
			ans+=index-i;
			for(int j=index;j>i;j--) {
				last[j]=last[j-1];
			}
			last[i]=tmp;
		}
		cout << ans << endl;
	}
	return 0;
}
