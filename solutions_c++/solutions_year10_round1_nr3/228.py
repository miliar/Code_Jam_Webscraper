// #includes {{{
#include <algorithm>
#include <numeric>
 
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
 
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>
#include <cstring>
 
#include <cmath>
#include <complex>
using namespace std;
// }}}
// pre-written code {{{
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define RREP(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
// }}}

const int N=2000000;

int l[N], c[N];

int binsearch(int n){
	int l=1, r=n-1;//l is o r is x
	while(r-l>1){
		int m=(l+r)/2;
		if(c[m]<n){
			l=m;
		}else{
			r=m;
		}
	}
	return l;
}

void find(int n){
	//int i=n-1;
	/*
	while(1){
		assert(i>=0);
		if(c[i]>=n){
		}else{
			break;
		}
		i--;
	}
	*/
	l[n]=binsearch(n)+1;
	c[n]=l[n]+n-1;
}

typedef long long Int;

Int intersection(int a1, int a2, int b1, int b2){
	if(a1<=b1){
		if(b1<=a2){
			if(a2<=b2){
				return a2-b1+1;
			}else{
				return b2-b1+1;
			}
		}else{
			return 0;
		}
	}else{
		return intersection(b1, b2, a1, a2);
	}
}

int main() {
	l[1]=c[1]=1;
	for(int i=2;i<N;i++){
		find(i);
//		cout<<i<<" "<<l[i]<<" "<<c[i]<<endl;
	}
	int T;
	cin>>T;
	REP(ct, T){
		int a1, a2, b1, b2;
		cin>>a1>>a2>>b1>>b2;
		Int num=0;
		for(int i=a1;i<=a2;i++){
			Int val=intersection(l[i], c[i], b1, b2);
			num+=val;
		}
		num=(Int)(a2-a1+1)*(b2-b1+1)-num;
		printf("Case #%d: %lld\n", ct+1, num);
	}
	return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
