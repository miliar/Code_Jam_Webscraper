#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cmath>
#include <iostream>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <queue>
#include <cstring>
#include <ctime>
using namespace std;

#define pii pair<int,int>
#define MPII make_pair<int,int>
#define PLL pair<lng,lng>
#define MPLL make_pair<lng,lng>
#define PI 3.1415926535897932384626433832795
#define DEG2RAD (PI/180.0)
#define RAD2DEG (1.0/DEG2RAD)
#define pb push_back
#define mp make_pair
#define VI vector<int>
#define VS vector<string>
#define VD vector<double>
#define forn(i,n) for(int i=0;i<n;++i)
#define fornr(i,n) for(int i=n-1;i>=0;--i)
#define forn1(i,n) for(int i=0;i<n+1;++i)
#define forv(i,v) for(int i=0;i<v.size();++i)
#define forvr(i,v) for(int i=v.size()-1;i>=0;--i)
#define fors(i,s) for(int i=0;i<s.length();++i)
#define EPS 1e-12
#define eps EPS
#define ABS(a) ((a)<0?-(a):(a))
#define EQ(a,b) (ABS((a)-(b))<EPS)
#define maxll ((1LL<<62)-1+(1LL<<62))
#define SQ(a) ((a)*(a))
#define SWAP(t,a,b) {t ____tmpasdasdasd=(a);(a)=(b);(b)=____tmpasdasdasd;}
#define abs(a) ((a)<0?-(a):(a))
#define ALL(a) (a).begin(),(a).end()


int c;
int num[1000];

long long getsum(int i) {
long long xsum1=0,sum1=0,sum2=0,xsum2=0;
	forn(j, c) {
		if (i>>j & 0x01) {
			xsum1 ^= num[j];
			sum1 += num[j];
		} else {
			xsum2 ^= num[j];
			sum2 += num[j];
		}
	}
	if (xsum2 != xsum1) return -1;
	return (sum2>sum1)?sum2:sum1;
}

int main(){
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);

	int tc;
	cin>>tc;
	long long res=-1;

	forn(q,tc){
		cin >> c;
		forn(i,c) {scanf("%d", &num[i]);}
		
		res=-1;
		for(int i=1;i<(1<<c)-1;i++) {
			long long tmp=getsum(i);
			if (tmp>res) res=tmp;
		}

		if (res>-1) {
			cout<<"Case #"<<q+1<<": "<<res<<endl;
		} else {
			cout<<"Case #"<<q+1<<": NO"<<endl;
		}
	}

	return 0;
}
