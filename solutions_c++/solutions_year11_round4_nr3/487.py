#include <stdio.h>
#include <iostream>
#include <set>
#include <map>
#include <string>
#include <string.h>
#include <queue>
#include <algorithm>
#include <math.h>
#include <sstream>
#include <complex>
#include <fstream>
using namespace std;

void solve();
#define mp make_pair
#define pb push_back
int main(){	
    freopen("input", "r", stdin);
    freopen("output","w",stdout);
	
	int t;
	cin>>t;
	for(int i=1;i<=t;++i){
		printf("Case #%d: ",i);
		solve();
	}
    return 0;
}
typedef long long int li;
#define int li
#ifdef int
#define INT "%lld"
#else
#define INT "%ld"
#endif
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef double ld;
void solve(){
	int n;
	scanf(INT,&n);
	if(n==1){
		printf("0\n");
		return;
	}
	int b[1111];
	memset(b,0,sizeof(b));
	vector<int> p;
	p.push_back(2);
	for(int i=3;i<=n;i+=2){
		bool g=true;
		for(int j=0;j<p.size();++j){
			if(i%p[j]==0){
				g=false;
				break;
			}
		}
		if(g){
			p.push_back(i);
		}
	}
	int ans=0;
	for(int i=0;i<p.size();++i){
		for(int j=p[i]*p[i];j<=n;j*=p[i]){
			++ans;
		}
	}
	printf(INT"\n",ans+1);
}