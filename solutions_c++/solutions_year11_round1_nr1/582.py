#include<iostream>
#include<sstream>
#include<vector>
#include<map>
#include<string>
#include<string.h>
#include<algorithm>
#include<math.h>
#include<queue>
#include<stack>
#include<stdio.h>
#include<stdlib.h>
#define INF (1<<29)
#define EPS (1e-7)
#define two(a) (1<<(a))
#define rep(a,b) for(a=0 ; a<b ; ++a)
#define xrep(a,b,c) for(a=b ; a<c ; ++a)
#define sca(t) scanf("%d",&t)
#define scal(t) scanf("%lld",&t)
typedef long long ll;
using namespace std;

ll n,d,g;

int check(int x){
	int i;
	if((100-d)%x==0 && d%x==0) return 1;
	return 0;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("palarge.out","w",stdout);
	int t,tt,i;
	cin >> t;
	for(tt=1 ; tt<=t ; tt++){
		cin >> n >> d >> g;
		cout << "Case #" << tt << ": ";
		if(g==100){
			if(d==100){
				cout << "Possible" << endl;
			}
			else cout << "Broken" << endl;
			continue;
		}
		if(g==0){
			if(d!=0){
				cout << "Broken" << endl;
			}
			else cout << "Possible" << endl;
			continue;
		}
		for(i=1 ; i<=100 ; i++){
			if(100%i==0){
				if(check(100/i)){
					break;
				}
			}
		}
		int w=i;
		if(n>=w){
			cout << "Possible" << endl;
		}
		else cout << "Broken" << endl;
	}
}
