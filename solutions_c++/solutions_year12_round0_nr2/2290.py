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

int d[200];

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int I,T,n,s,p,r,t,i;
	cin>>T;
	for(I=1;I<=T;I++) {
		cin>>n>>s>>p;
		for(i=0;i<n;i++) cin>>d[i];
		sort(d,d+n);
		r=0;
		for(i=0;i<n;i++) {
			t=(d[i]/3)+(d[i]%3?1:0);
			if(t>=p) r++;
			else if(s && d[i]>=2 && (d[i]%3)!=1 && (t+1)>=p){
				s--;
				r++;
			}
		}
		cout<<"Case #"<<I<<": "<<r<<"\n";
	}
	return 0;
}
