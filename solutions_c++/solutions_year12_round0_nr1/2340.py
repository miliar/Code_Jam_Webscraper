#include <iomanip>
#include <numeric>
#include <functional>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <cmath>
#include <cctype>
#include <sstream>
#include <map>
#include <set>
#include <cstdio>
#include <queue>
#define f(i,x,y) for(int i=x;i<y;i++)
#define fd(i,y,x) for(int i=y;i>=x;i--)
#define FOR(it,A) for( typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define impr(A) for( typeof A.begin() chen = A.begin(); chen !=A.end(); chen++ ) cout<<*chen<<" "; cout<<endl
#define ll long long
#define vint vector<int>
#define clr(A,x) memset(A,x,sizeof(A))
#define CLR(v) f(i,0,n) v[i].clear()
#define oo (1<<30)
#define ones(x) __builtin_popcount(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define pb push_back
#define eps (1e-9)
#define cua(x) (x)*(x)
using namespace std;
string ss[3] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
"de kr kd eoya kw aej tysr re ujdr lkgc j"};
string out[3] = {"our language is impossible to understand",
"there are twenty six factorial possibilities",
"so it is okay if you want to just give up"};
int val[256];

int main()
{
	val['z']  = 'q'; val['q'] = 'z';
	f(i,0,3) f(j,0,ss[i].size()) val[ss[i][j]] = out[i][j];
	int T;
	cin >> T;
	int caso = 1;
	string cad; getline (cin, cad);
	while (T--){
		getline (cin, cad);
		cout<< "Case #" << caso++ << ": ";
		f(i,0,cad.size()) cout << char (val[cad[i]]); cout << endl;

	}
}

