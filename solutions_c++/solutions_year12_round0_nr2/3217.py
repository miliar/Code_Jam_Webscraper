#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <cmath>
#include <cstring>
#include <cstdlib>

using namespace std;

#define pb push_back
#define mp make_pair
#define rep(i,n) for(int i=0;i<(int)(n);++i)
#define REP(i,j,k) for(int i=j;i<(int)(k);++i)
#define foreach(i,c) for(__typeof(c.begin()) i=c.begin();i!=c.end();++i)
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef long long ll;
const int INF = 99999999;
const double EPS = 1e-9;

int T,N,S,p;
vi t;

int main()
{
	cin >> T;
	rep(i,T){
		int ans=0;
		cin >> N >> S >> p;
		t.resize(N);
		rep(j,N) cin >> t[j];
		sort(all(t));
		rep(j,N){
			int res[3];
			res[0]=res[1]=res[2]=(t[j]/3);
			int k=0;
			while(res[0]+res[1]+res[2]<t[j]) res[k++]++;
			if(res[0]>=p) ans++;
			else if(S>0&&res[0]==res[1]&&res[1]!=0&&res[0]+1>=p){
				ans++;
				S--;
			}
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
		t.clear();
	}
	
    return 0;
}
