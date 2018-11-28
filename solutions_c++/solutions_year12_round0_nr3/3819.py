#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <deque>
#include <set>
using namespace std;

#define sz size()
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define C(a) memset((a),0,sizeof(a))
#define inf 1000000000
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define pi 2*acos(0.0)
#define sqr(a) (a)*(a)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second

typedef vector<int> vint;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
const int INF=2000000000;   
 
int main( ) {
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
	//freopen("input.txt","r",stdin);
	int a,b,n,cnt=0;
	cin>>n;
	rep(huy,n){
		cin>>a>>b;
		cnt=0;
		FOR(i,a,b){
			int g=i,pow=1;
			while(g/=10)pow*=10;
			g=i;
			while(1){
				g=(g%10)*pow+g/10;
				if(g>i && g<=b)cnt++;
				if(g==i)break;
			}

		}
		printf("Case #%d: %d\n",huy+1,cnt);

	}
	
	return 0;
}