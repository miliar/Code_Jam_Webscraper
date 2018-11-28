#include <iomanip>
#include <ctime>
#include <numeric>
#include <functional>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <climits>
#include <cmath>
#include <cctype>
#include <sstream>
#include <map>
#include <set>
#include <cstdio>
#include <queue>
#define f(i,x,y) for(int i=x;i<y;i++)
#define fd(i,y,x) for(int i=y;i>=x;i--)
#define ll long long
#define vint vector<int>
#define clr(A,x) memset(A,x,sizeof(A))
#define CLR(v) f(i,0,n) v[i].clear()
#define oo (1<<30)
#define ones(x) __builtin_popcount(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define poner push_back
#define eps (1e-9)
using namespace std;

int T;

int main()
{
	cin >> T; ll n,pd,pg;
	f(cases,0,T){
		cin >> n >> pd >> pg;
		cout << "Case #" << cases+1 << ": ";
		ll d = __gcd(pd,100LL);
		ll p = pd/d, q = 100/d;
		bool pos = 1;
		if( q>n ) pos = 0;
		else{
			if( p!=q && pg==100 ) pos = 0;
			else{
				if( p && pg==0 ) pos = 0;
				else pos = 1;
			}
		}
		cout << (pos? "Possible" : "Broken") << endl;
	}
}
