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
#define PB(x) push_back(x)

#define mx 2000009
bool vis[mx];
int lg[mx];

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int i,a,b,I,T,t,j;
	for(i=1;i<=mx;i=a) {
		a=i*10;
		for(j=i;j<a && j<mx;j++) lg[j]=i;
	}
	cin>>T;
	i64 r;
	for(I=1;I<=T;I++) {
		cin>>a>>b;
		r=0;
		for(i=a;i<=b;i++) {
			t=i;
			j=0;
			while(1) {
				t=(t/10)+lg[i]*(t%10);
				//cout<<i<<' '<<t<<'\n';
				//getchar();
				if(t==i) break;
				if(t>=a && t<=b && lg[t]==lg[i]) j++;
			}
			r+=j;
		}
		r>>=1;
		cout<<"Case #"<<I<<": "<<r<<'\n';
	}
	return 0;
}
