#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <ctime>
#include <climits>
#include <cassert>
//#pragma comment(linker, "/STACK:640000000")
#ifdef _Win32
#  define I64 "%I64d"
#else
#  define I64 "%lld"
#endif
#define fs first
#define sc second
#define mp make_pair
#define pb push_back
#define next ksdjgsd
#define prev lsfnasd
using namespace std;
typedef long long ll;
typedef double ld;
typedef pair<int, int> pi;
const ld E=1e-8;
const int inf=(int)1e9;

ld b[1010];
ld e[1010];
ld l[1010];
ld w[1010];
int p[1010];

inline bool comp(int x, int y){
	return w[x]<w[y];
}

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int tn;
	scanf("%d", &tn);
	for(int tt=0;tt<tn;tt++){
		ld x, s, t, r;
		int n;
		scanf("%lf%lf%lf%lf%d", &x, &s, &r, &t, &n);
		for(int i=0;i<n;i++) scanf("%lf%lf%lf", b+i, e+i, w+i);
		for(int i=0;i<n;i++) l[i]=e[i]-b[i];
		ld sum=0;
		for(int i=0;i<n;i++) sum+=l[i];
		l[n]=x-sum;
		w[n]=0;
		n++;
		for(int i=0;i<n;i++) w[i]+=s;
		r-=s; 
		for(int i=0;i<n;i++) p[i]=i;
		sort(p, p+n, comp);
		ld res=0;
		for(int i=0;i<n;i++){
			if(t>E){
				if(t>l[p[i]]/(w[p[i]]+r)-E){
					res+=l[p[i]]/(w[p[i]]+r);
					t-=l[p[i]]/(w[p[i]]+r);
				}else{
					res+=t;
					res+=(l[p[i]]-t*(w[p[i]]+r))/w[p[i]];
					t=0;
				}
			}else res+=l[p[i]]/w[p[i]];
		}
		printf("Case #%d: %.10lf\n", tt+1, res);
	}
	return 0;
}
