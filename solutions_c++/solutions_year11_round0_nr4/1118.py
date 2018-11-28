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

int T,n;
int a[1000];
int res = 0;

int main()
{
	cin >> T;
	f(cases,0,T){
		cin >> n;
		f(i,0,n) scanf("%d", a+i ), a[i]--;
		res = 0;
		f(i,0,n)if( a[i]!=i ) res++;
		printf("Case #%d: %d.000000\n", cases+1, res );
	}
}
