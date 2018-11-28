#include<iostream>
#include<vector>
#include<string.h>
#include<stdio.h>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<math.h>
#include<limits.h>
using namespace std;
#define FOR(i,a,b) for(i = (a); i < (b); i++)
#define RFOR(i,a,b)for(i = (b); i >= (a); i--)
#define FORI(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(v) (v).size()
#define ll long long int
#define ii pair<int,int>
void f(int i){
        cout << "Case #" << i << ": ";
}
int main()

{
//	ios_base::sync_with_stdio(0);	
	int i,j,k;
	int n;
	cin >> n;
	int a[2000];
	FOR(i,1,n+1){
		f(i);
		int t , xtotal = 0 , total = 0 ,ans = 0 ;
		cin >> t;

		FOR(j,0,t){
			cin >> a[j];
			total += a[j];
			xtotal ^= a[j];	
		}
		sort(a , a + t);
		bool b = 0;
		FOR(j,0,t){
			if((a[j] ^ xtotal) == a[j]){
				b = 1;
				ans = total - a[j];
				break;
			}
		
		}
		if(b)
			cout << ans << "\n";
		else
			cout << "NO\n";
	//	f(i);
		
	}

	return 0;
}
