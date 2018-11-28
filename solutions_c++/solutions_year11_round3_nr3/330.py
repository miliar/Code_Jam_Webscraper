//BISMILLAHIRRAHMANIRRAHIM



#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cctype>
#include <climits>
#include <cmath>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <set>
#include <map>
using namespace std;

#define pii pair < int , int >
#define i64 long long
#define CLR(x) memset(x,0,sizeof x)
#define SET(x,y) memset(x,y,sizeof x)


#define mx 20000

int cn[mx],a[200];

int main() {
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int i,k,n,I,T,j,h,l,s;
	cin>>T;
	for(I=1;I<=T;I++) {
		cin>>n>>l>>h;
		memset(cn,0,sizeof cn);
		for(i=0;i<n;i++) {
			scanf("%d",&a[i]);
			for(j=a[i]<<1;j<=h;j+=a[i]) cn[j]++;
			s=sqrt(a[i]);
			for(j=1;j<=s;j++) if(!(a[i]%j)) {
				if(j<=h) cn[j]++;
				if((a[i]/j)<=h && (a[i]/j)!=j) cn[a[i]/j]++;
			}
			/*for(j=0;j<=h;j++) cout<<cn[j]<<' ';
			puts("");*/
		}
		bool f=1;
		for(i=l;i<=h;i++) if(cn[i]==n) {
			f=0;
			break;
		}
		printf("Case #%d: ",I);
		if(f) puts("NO");
		else cout<<i<<'\n';
	}
	return 0;
}

