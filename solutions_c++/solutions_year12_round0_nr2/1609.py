#include <iostream> 
#include <vector>
#include <set>
#include <cstdio>
#include <cmath>
#include <string>
#include <algorithm>
#include <map>
#include <queue>
#include <memory.h>
#include <fstream>
using namespace std;

#define FOR(i,a,b) for(int (i)=(a);(i)<(b);(i)++)
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define PB push_back
#define PII pair<int,int>
#define CLEAR(a) memset((a),0,sizeof((a)))
#define X first
#define Y second

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> VI;

const double pi=3.141592653589793;
const int INF=2000000000;
const int mod=1000000007;
map <char,char> a;
int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin >> t;
	FOR(tt,0,t){
		cout << "Case #" << tt+1 << ": ";
		int n,s,p;
		cin >> n >> s >> p;
		int a[105];
		FOR(i,0,n)
			cin >> a[i];
		if (p == 0){
			cout << n << endl;
			continue;
		}
		if (p == 1){
			int k = 0;
			FOR(i,0,n)
				if (a[i]) ++k;
			cout << k << endl;
			continue;
		}
		int k1 = 0, k2 = 0;
		FOR(i,0,n){
			if (a[i] >= 3*p-2) k1++;
			else if (a[i] >= 3*p-4) k2++; 
		}
		cout << k1 + min(s,k2) << endl;
	}
	return 0;
}