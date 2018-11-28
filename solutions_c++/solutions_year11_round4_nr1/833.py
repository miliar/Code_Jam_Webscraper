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
int len , n , t;
int st[2000] , en[1111] , w[2222] , s , r;

void cg(int &p , int &q) {
	int t=p;
	p=q;
	q=t;
}

void qs(int p , int q) {
	int i=p , j=q , k=w[rand()%(q-p+1)+p];
	do {
		while (w[i]<k) i++;
		while (w[j]>k) j--;
		if (i<=j) {
			cg(st[i],st[j]);
			cg(en[i],en[j]);
			cg(w[i],w[j]);
			i++;
			j--;
		}
	}
	while (i<=j);
	if (i<q) qs(i,q);
	if (p<j) qs(p,j);
}

int main() {
	freopen("in.txt" , "r" , stdin);
	freopen("a.txt" , "w" , stdout);
	int i , j , k , tt , tol , ttt;
	double a , b , c , ans , t;
	cin >> tt;
	for (ttt=1; ttt<=tt; ttt++) {
		cin >> len >> s >> r >> t >> n;
		tol=0;
		ans=0;
		for (i=1; i<=n; i++) {
			cin >> st[i] >> en[i] >> w[i];
			tol+=(en[i]-st[i]);
		}
		qs(1,n);
		w[0]=0;
		st[0]=0;
		en[0]=len-tol;
		for (i=0; i<=n; i++) {
			a=(en[i]-st[i])*1.0/(w[i]+r);
			if (a<t) {
				t-=a;
				ans+=a;
			}
			else {
				ans+=t;
				b=t*(w[i]+r);
				b=en[i]-st[i]-b;
				ans+=b*1.0/(s+w[i]);
				break;
			}
		}
		for (j=i+1; j<=n; j++) ans+=((en[j]-st[j])*1.0/(s+w[j]));
		printf("Case #%d: %lf\n" , ttt , ans);
	}
	return 0;
}