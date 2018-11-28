#include<iostream>
#include<vector>
#include<map>
#include<fstream>
#include<string>
#include<math.h>
#include<queue>
#include<stack>
#include<sstream>
#include<algorithm>
#include<set>
#include<stdio.h>
#include<stdlib.h>

#define vint vector <int>
#define vstring vector <string>
#define np(a) next_permutation(a.begin(),a.end())
#define ff(i,n) for (i=0; i<n; i++)
#define pb(a,b) a.push_back(b)
#define mkp make_pair
#define all(a) a.begin() , a.end()

/*

sort(a.begin(),a.end(),f) for vint a;
sort(a,a+n) for int a[n] where a[0] is smallest;

reverse(a.begin(),a.end()) for vint a;
reverse(a,a+n) for int a[n];

pair <int , string> a;

multiset<int> mymultiset (myints,myints+5);

*/

using namespace std;
typedef __int64 ll;
stringstream ss;

char mp[33][33];
bool op[33][33];
char ans[3333];
int cn , opn;

int main() {
	freopen("in.txt" , "r" , stdin);
	freopen("b.txt" , "w" , stdout);
	int i , j , k , m , n , tt;
	char ch;
	string s;
	cin >> tt;
	for (k=1; k<=tt; k++) {
		cin >> cn;
		for (i=0; i<26; i++)
			for (j=0; j<26; j++) {
				mp[i][j]=' ';
				op[i][j]=false;
			}
		for (i=1; i<=cn; i++) {
			cin >> s;
			mp[s[0]-'A'][s[1]-'A']=mp[s[1]-'A'][s[0]-'A']=s[2];
		}
		cin >> opn;
		for (i=1; i<=opn; i++) {
			cin >> s;
			op[s[0]-'A'][s[1]-'A']=op[s[1]-'A'][s[0]-'A']=true;
		}
		cin >> n >> s;
		m=0;
		for (i=0; i<n; i++) {
			if ((m>0)&&(mp[s[i]-'A'][ans[m]-'A']!=' ')) {
				ans[m]=mp[s[i]-'A'][ans[m]-'A'];
				continue;
			}
			for (j=1; j<=m; j++) if (op[ans[j]-'A'][s[i]-'A']) break;
			if (j<=m) {
				m=0;
				continue;
			}
			m++;
			ans[m]=s[i];
		}
		printf("Case #%d: [" , k);
		if (m==0) printf("]\n");
		else {
			cout << ans[1];
			for (i=2; i<=m; i++) cout << ", " << ans[i];
			cout << "]\n";
		}
	}
	return 0;
}