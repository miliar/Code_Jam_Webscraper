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

int main() {
	freopen("in.txt" , "r" , stdin);
	freopen("c.txt" , "w" , stdout);
	int i , j , k , tt , n , x , mi , he , e;
	cin >> tt;
	for (k=1; k<=tt; k++) {
		cin >> n;
		he=0;
		mi=99999999;
		x=0;
		for (i=1; i<=n; i++) {
			cin >> e;
			if (e<mi) mi=e;
			he+=e;
			x^=e;
		}
		if (x!=0) printf("Case #%d: NO\n" , k);
		else printf("Case #%d: %d\n" , k , he-mi);
	}
	return 0;
}