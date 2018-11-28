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
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define REPEAT(i,a,b) for(int i=a;i<b;++i)
#define REP(i,n) REPEAT(i,0,n)
#define RREP(i,n) for(int i=n-1;i>=0;--i)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
#define mkp make_pair

typedef long long ll;
typedef vector <int> vi;
ll GCD(ll x,ll y){
	if(y == 0) return x;
	if(x == 0) return y;
	return GCD(y,x%y);
	
	}
int main(){
	int T;
	cin>>T;
	REP(z,T){
		int n,l,h;
		cin>>n>>l>>h;
		vi v(n);
		REP(i,n) cin>>v[i];
		int ans=-1,j,t;
		REPEAT(i,l,(h+1)){
			t = 0;
			for(j=0;j<n;j++){
				if(i>= v[j] && i%v[j]) {
					t = 1;
					break;
					}
				else if(i<=v[j] && v[j]%i) {
					t = 1;
					break;
					}
				}
			if(t == 0){
				ans = i;
				break;
				}
			}
		cout<<"Case #"<<z+1<<": ";
		if(ans!=-1)
			cout<<ans<<endl;
		else cout<<"NO"<<endl;
			
		}	
	}