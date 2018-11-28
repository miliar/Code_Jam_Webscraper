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
#define INT "%lld"
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef double ld;

int gcd(int a,int b){
	if(!b)
		return a;
	return gcd(b,a%b);
}
void solve(){
	int n,pd,pg;
	scanf(INT INT INT,&n,&pd,&pg);
	int g=gcd(pd,100);
	bool f=false;
	if((100/g)<=n){
		//cout<<n<<' '<<pd<<' '<<pg;
		f=true;
	}
	if((pd!=0 && pg==0))
		f=false;
	if(pd!=100 && pg==100)
		f=false;
	if(f)
		printf("Possible\n");
	else
		printf("Broken\n");
}