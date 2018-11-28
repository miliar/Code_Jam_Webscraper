#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<cassert>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<vector>
#include<string>
#include<set>
#include<map>
#include<queue>

using namespace std;

#define repp(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define rep(i,n) repp(i,0,(n)-1)

#define pb push_back
#define mp make_pair

typedef long long ll;
typedef pair<int,int> pint;

int in(){int a; scanf("%d",&a); return a;}
int dx[4]={1,0,-1,0},dy[4]={0,1,0,-1};

typedef pair<pint,int> tint;
#define one first.first
#define two first.second
#define thr second

int gcd(int a,int b){
	return a?gcd(b%a,a):b;
}

int main(){
	int t=in();
	rep(cas,t){
		cout << "Case #" << cas+1 << ": ";
		ll n=in();
		int d=in();
		int g=in();
		if(d > 0 && g==0) goto imp;
		if(100/gcd(d,100) > n) goto imp;
		if(d<100 && g==100) goto imp;
		cout << "Possible" << endl;
		continue;
		imp:;
		cout << "Broken" << endl;
	}
    return 0;
}

