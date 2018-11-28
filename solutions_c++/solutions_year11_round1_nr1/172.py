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

__int64 n , pd , pg;

bool ok() {
	int i , j , k;
	double a , b , c;
	if ((pd>0)&&(pg==0)) return false;
	if ((pd<100)&&(pg==100)) return false;
	for (i=1; i<=n; i++) {
		a=i;
		a=a/100*pd;
		if ((a-(__int64)(a+0.00000001))<0.0000001) return true;
	}
	return false;
}

int main() {
	freopen("in.txt" , "r" , stdin);
	freopen("a.txt" , "w" , stdout);
	int i , j , k , tt , ttt;
	cin >> ttt;
	for (tt=1; tt<=ttt; tt++) {
		scanf("%I64d%I64d%I64d" , &n,  &pd , &pg);
		if (ok()) printf("Case #%d: Possible\n" , tt);
		else printf("Case #%d: Broken\n" , tt);
	}
	return 0;
}