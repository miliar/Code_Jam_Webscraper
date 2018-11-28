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

int a[100000];
int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int tt=0;tt<t;tt++){
		int n;
		scanf("%d", &n);
		for(int i=0;i<n;i++) scanf("%d", a+i);
		int res=0;
		for(int i=0;i<n;i++) res^=a[i];
		printf("Case #%d: ", tt+1);
		if(res==0){
			int m=a[0];
			ll sum=0;
			for(int i=0;i<n;i++){
				sum+=a[i];
				m=min(m, a[i]);
			}
			printf("%I64d\n", sum-m);
		}else printf("NO\n");
	}		 
	return 0;
}
