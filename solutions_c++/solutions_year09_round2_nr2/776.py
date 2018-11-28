#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<queue>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>

using namespace std;

#define fo(a,b) for(a=0;a<b;a++)
#define pf printf
#define sf scanf
#define re return

int main() {
	//freopen("b1.in","r",stdin);
	//freopen("b1.out","w",stdout);
	int t, i;
	int cases = 1;
	for( sf("%d", &t); t--; ) {
		string s;
		cin >> s;
		string ss = s;
		if( next_permutation(s.begin(), s.end() ) ) {
			pf("Case #%d: ", cases++);
			cout << s << endl;
		}
		else {
			sort(ss.begin(), ss.end() );
			string res = "";
			for(i=0;i<ss.size();i++)
			 if( ss[i] != '0' ) break;

			res += ss[i]; res += '0';
			ss.erase(ss.begin()+ i);

			res += ss;
			pf("Case #%d: ", cases++);
			cout << res << endl;
		}

	}
	return 0;
}
