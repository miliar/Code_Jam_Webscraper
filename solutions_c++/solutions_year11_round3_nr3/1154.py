#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <cstring>

#include <iostream>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <utility>
#include <queue>

#define fo(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define fr(a,b) fo( a, 0, ( b ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	
	int test, t=1, n;
	long long l, h, i;
	long long freq[1100];
	bool flag;
	
	cin >> test;
	while (test--){
		cin >> n >> l >> h;
		fi(n){
			cin >> freq[i];
		}
		
		for (i = l; i<=h; i++){
			flag = true;
			//cout << "DBG: i: " << i << " flag: " << flag << endl;
			for (int j=0; j<n; j++){
				if ( ((freq[j]%i) != 0)
					&& ((i%freq[j] != 0)) ){
					flag = false;
					//cout << "DBG: i: " << i << " freq " << j << " : " << freq[j] << " flag: " << flag << endl;
					//cout << "DBG: pq f[j]%i: " << freq[j]%i << " e i%f[j]: " << i%freq[j] << endl;
					break;
				}
			}
			if (flag) break;
		}
		
		if (flag) cout << "Case #" << t++ << ": " << i << "\n";
		else cout << "Case #" << t++ << ": NO\n";
	}
	
	return 0;
}