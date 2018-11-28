#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

vector <int> v;

int main() {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int t,n,d;
	int _xor1,_xor0,_sum1,_sum0;
	scanf("%d",&t);
	for (int z=0;z<t;z++) {
		scanf("%d",&n);
		v.clear();
		v.resize(n);
		for (int i=0;i<n;i++) scanf("%d",&v[i]);
		d = n/2;
		int res = -1;
		for (int l=1;l<=d;l++) {
			string s;
			s.resize(n,'1');
			for (int i=0;i<l;i++) s[i]='0';
		//	cout << "->" << s << endl;
			do {
				_xor1 = _xor0 = _sum1 = _sum0 = 0;
				for (int i=0;i<n;i++) 
					if (s[i]=='0') {
						_xor0^=v[i];
						_sum0+=v[i];
					} else {
						_xor1^=v[i];
						_sum1+=v[i];
					}
					if (_xor0==_xor1) res = max( res , max(_sum1 , _sum0));
			} while(next_permutation(s.begin(),s.end()));
		}
		cout << "Case #" << z+1 << ": "; 
		if (res==-1) cout << "NO"; else cout << res;
		cout << endl;
	}

}