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

const int pN=25;
const int N=1<<pN;
const int lim=1<<30;
int a[N];
int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	
	int tn;
	scanf("%d\n", &tn);
	for(int tt=0;tt<tn;tt++){
		char s[200];
		scanf("%s\n", s);
		int n=strlen(s);
		reverse(s, s+n);
		int p=min(pN, n);
		for(int i=0;i<N;i++) a[i]=0;
		int res=0;
		bool t=false;
		for(ll i=0;i<N && !t;i++){
			if(i<(1<<p)) a[i]=1;
			for(int j=0;j<p && a[i]==1;j++){
				if(s[j]!='?' && s[j]!='0'+(((i*i)>>j)&1)) a[i]=0;
			}
			res+=a[i];
			if(a[i]==1){
				for(ll k=i;k<lim && k*k<(ll)1<<n && !t;k=k+(1<<p)){
					t=true;
					for(int j=0;j<n && t;j++){
						if(s[j]!='?' && s[j]!='0'+(((k*k)>>j)&1)) t=false;
					}
					if(t){
						cerr<<"res "<<k<<endl;
						printf("Case #%d: ", tt+1);
						for(int j=n-1;j>=0;j--) printf("%c", (char)('0'+(((k*k)>>j)&1)));
						printf("\n");
					}

				} 
			}	
		}
		cerr<<res<<endl;
	}
	return 0;
}
