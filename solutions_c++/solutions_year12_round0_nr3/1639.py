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
	//freopen("out.txt","w",stdout);
	ofstream out("out.txt");
	int t;
	cin >> t;
	FOR(tt,0,t){
		out << "Case #" << tt+1 << ": ";
		int a,b;
		cin >> a >> b;
		int l = 0,aa = a;
		while (aa){
			aa/=10;
			l++;
		}
		int deg = 1;
		FOR(i,0,l-1)
			deg*=10;
		int res = 0;
		set<int> q;
		FOR(i,a,b){
			q.clear();
			int k = i;
			FOR(j,0,l){
				int x = k%10;
				k/=10;
				k+= x*deg;
				if (k>i && k>=a && k<=b) {q.insert(k);}
			}
			res+=q.size();
		}
		out << res << endl;
		cout << tt + 1 << endl;
	}
	return 0;
}