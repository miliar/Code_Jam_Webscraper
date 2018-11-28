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

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int tn;
	scanf("%d", &tn);
	for(int tt=0;tt<tn;tt++){
		int n, m;
		scanf("%d%d\n", &n, &m);
		char s[100][100];
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++) scanf("%c", &s[i][j]);
			scanf("\n");
		}
		int a[100][100];
		int res=0;
		for(int x=0;x<1<<(n*m);x++){
			for(int i=0;i<n;i++) for(int j=0;j<m;j++) a[i][j]=0;
			for(int i=0;i<n;i++) for(int j=0;j<m;j++){
				if(((x>>(i*m+j))&1)==0){
					if(s[i][j]=='|') a[(i+1)%n][j]++;
					else if(s[i][j]=='/') a[(i+1)%n][(j+m-1)%m]++;
					else if(s[i][j]=='\\') a[(i+1)%n][(j+m+1)%m]++;
					else a[i][(j+1)%m]++;
				}else{
					if(s[i][j]=='|') a[(i+n-1)%n][j]++;
					else if(s[i][j]=='/') a[(i-1+n)%n][(j+m+1)%m]++;
					else if(s[i][j]=='\\') a[(i-1+n)%n][(j+m-1)%m]++;
					else a[i][(j-1+m)%m]++;
				}
			}
			bool t=true;
			for(int i=0;i<n;i++) for(int j=0;j<m;j++) if(a[i][j]!=1) t=false;
			if(t) res++;
		}
		printf("Case #%d: %d\n", tt+1, res);
	}
	return 0;
}
