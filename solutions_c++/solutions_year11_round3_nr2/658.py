#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <sstream>
#include <algorithm>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <climits>
#include <cmath>

using namespace std;

#define RP(i,j,k) for(int i=j; i<k; ++i)
#define R(i,x) RP(i,0,(x).size())
#define RP3(x,y,z) RP(i,0,x) RP(j,0,y) RP(k,0,z)
#define RI(i,x) for(typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define pB push_back
#define P(a) cout << #a << " : " << a << endl;
#define M make_pair

template <class T, class R>
ostream & operator<<(ostream & o, pair<T,R> a){return o<<a._1<<"," << a._2;}

template <class T>
ostream & operator<<(ostream & o, vector<T> a){R(i,a) o<<a[i]<<","; return o;}

typedef vector<string> vs;
typedef vector<int> vi;
typedef long long ll;

int v[1100];
int a[1100];

int l,t,n,c;

int bp[2];

bool isboost(int i, int bc){
	if(bc>1 && bp[1]==i) return true;
	if(bc>0 && bp[0]==i) return true;
	return false;
}

int sp;
int test(int bc){
	int e=0;
	sp=0;
	for(int i=0; i<n; ++i){
		int f=e+v[i]*2;
		if(f>=t && t>=e) sp=i;
		if(isboost(i, bc) && f>t){
			int ts=max(t,e);
			int dr=(f-ts)/2;
			f=ts+dr;
		}
		e=f;
	}
	return e;
}

int solve(){
	int normal=test(0);
		
	if(l==0) return normal;
	
	int best=1e9;
	if(l==1)
	for(int b1=0; b1<n; ++b1){
		bp[0]=b1;
		int res=test(1);
		if(res<best) best=res;
		/*if(l==2){
			bp[1]=sp;
			int r2=test(2);
			int mx=-1;
			for(int i=sp+1; i<n; ++i)
				if(mx==-1 || v[mx]<v[i]) mx=i;
			bp[1]=mx;
			int r3=test(2);
			if(r2<best) best=r2;
			if(r3<best) best=r3;
		}*/
	}
	if(l==2)
	for(int b1=0; b1<n; ++b1)
	for(int b2=0; b2<n; ++b2){
		bp[0]=b1;
		bp[1]=b2;
		int res=test(2);
		if(res<best) best=res;
		/*if(l==2){
			bp[1]=sp;
			int r2=test(2);
			int mx=-1;
			for(int i=sp+1; i<n; ++i)
				if(mx==-1 || v[mx]<v[i]) mx=i;
			bp[1]=mx;
			int r3=test(2);
			if(r2<best) best=r2;
			if(r3<best) best=r3;
		}*/
	}
	
	return best;
}

int main()
{
	int C;
	cin >> C;
	
	for(int cs=1; cs<=C; ++cs)
	{
		ll T;
		cin >> l >> T >> n >> c;
		if(T>1e9) T=1e9;
		t=T;
		
		for(int i=0; i<c; ++i)
			cin >> a[i];
			
		for(int i=0; i<n; ++i)
			v[i]=a[i%c];
		
		cout << "Case #" << cs << ": " << solve();
		
		cout << endl;
	}
	
	return 0;
}