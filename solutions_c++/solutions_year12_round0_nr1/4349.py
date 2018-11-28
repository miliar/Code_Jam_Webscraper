#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <fstream>
#include <cstring>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;

#define FOR(i, a, b) for (int i = a; i < b; i++) 
#define REP(i, n) FOR(i,0,n)
#define GI ({int t;scanf("%d",&t);t;})
#define GL ({ll t;scanf("%lld",&t);t;})
#define GD ({double t;scanf("%lf",&t);t;})
#define pb push_back 
#define sz size()
#define TRvi(c, it) for (vi::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvii(c, it) for (vii::iterator it = (c).begin(); it != (c).end(); it++)
#define TRmsi(c, it) for (msi::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 1000000007
#define flush(x) memset(x,-1,sizeof(x))
#define MAXN 100010

int main()
{
	string s="yhesocvxduiglbkrztnwjpfmaq";
	int t=GI;
	cin.get();
	int k=1;
	while(t--)
	{
		cout<<"Case #"<<k++<<": ";
		string c;
		getline(cin,c,'\n');
		REP(i,c.sz) if(c[i]!=' ') cout<<s[c[i]-'a']; else cout<<c[i];
		cout<<endl;
	}
}
