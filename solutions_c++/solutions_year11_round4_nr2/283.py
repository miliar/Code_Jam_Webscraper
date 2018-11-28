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
typedef long double ld;
typedef pair<int, int> pi;
const ld E=1e-8;
const int inf=(int)1e9;

struct pt{
	ld x, y, w;
	pt(){}
	pt(ld _x, ld _y, ld _w): x(_x), y(_y), w(_w){}
};

inline pt operator !(pt p){
	return pt(p.x, p.y, -p.w);
}

inline pt operator +(pt p1, pt p2){
	if(fabs(p1.w+p2.w)<E){
		cerr<<"FAIL! "<<p1.x<<" "<<p1.y<<" "<<p1.w<<endl;
		cerr<<"----- "<<p2.x<<" "<<p2.y<<" "<<p2.w<<endl;
	}	
    assert(fabs(p1.w+p2.w)>E);
	return pt((p1.x*p1.w+p2.x*p2.w)/(p1.w+p2.w), (p1.y*p1.w+p2.y*p2.w)/(p1.w+p2.w), p1.w+p2.w);
}	 


int a[510][510];
pt s[510][510];

pt getr(int x1, int y1, int x2, int y2){
	pt res= (s[x1][y1]+s[x2+1][y2+1]);
	//cerr<<res.x<<" "<<res.y<<" "<<res.w<<endl;
    res=res+(!s[x1][y2+1])+(!s[x2+1][y1]);
	//cerr<<res.x<<" "<<res.y<<" "<<res.w<<endl;
    res=res+(pt(x1, y1, -a[x1][y1]))+(pt(x1, y2, -a[x1][y2]))+(pt(x2, y1, -a[x2][y1]))+(pt(x2, y2, -a[x2][y2]));
	return res;
}

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int tn;
	scanf("%d", &tn);
	for(int tt=0;tt<tn;tt++){
		int n, m, d;
		scanf("%d%d%d\n", &n, &m, &d);
		char c;
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				scanf("%c", &c);
				a[i][j]=c-'0'+d;
			}
			scanf("\n");
		}
		for(int i=0;i<n+1;i++) s[i][0].w=0;
		for(int i=0;i<m+1;i++) s[0][i].w=0;
		for(int i=0;i<n;i++) for(int j=0;j<m;j++){
		//	cerr<<i<<" "<<j<<endl;
			s[i+1][j+1]=(!s[i][j])+(pt(i, j, a[i][j])+s[i+1][j])+s[i][j+1];
		}
		//for(int i=0;i<n+1;i++) for(int j=0;j<m+1;j++) cerr<<i<<" "<<j<<" "<<s[i][j].x<<" "<<s[i][j].y<<" "<<s[i][j].w<<endl;
		int res=0;
		for(int i=0;i<n;i++) for(int j=0;j<m;j++){
			for(int k=1;i-k>=0 && i+k<n && j-k>=0 && j+k<m;k++){
				pt p=getr(i-k, j-k, i+k, j+k);
				if(fabs(p.x-i)<E && fabs(p.y-j)<E) res=max(res, 2*k+1);
			}
		}
		for(int i=0;i<n;i++) for(int j=0;j<m;j++){
			for(int k=2;i-k>=0 && i+k<=n && j-k>=0 && j+k<=m;k++){
				pt p=getr(i-k, j-k, i+k-1, j+k-1);
				if(fabs(p.x-i+0.5)<E && fabs(p.y-j+0.5)<E) res=max(res, 2*k);
			}
		}
		printf("Case #%d: ", tt+1);
		if(res==0) printf("IMPOSSIBLE\n");
		else printf("%d\n", res);
	}
	return 0;
}
