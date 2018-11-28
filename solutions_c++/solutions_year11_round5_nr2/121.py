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

int a[10010];
int b[10010];
int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int tn;
	scanf("%d", &tn);
	for(int tt=0;tt<tn;tt++){
		int n;
		scanf("%d", &n);
		for(int i=0;i<=10000;i++) a[i]=0;
		int k;
		for(int i=0;i<n;i++){
			scanf("%d", &k);
			a[k]++;
		}
		int res=inf;
		int st=0;
		int en=0;
		for(int i=1;i<=10001;i++){
			if(a[i]<en-st){
				for(int j=st;j<en-a[i];j++) res=min(res, i-b[j]);
				st=en-a[i];
			}else if(a[i]>en-st){
				for(int j=en;j<a[i]+st;j++) b[j]=i;
				en=a[i]+st;
			}
		}
		printf("Case #%d: ", tt+1);
		if(n==0) printf("0\n");
		else printf("%d\n", res);
	}
	return 0;
}
