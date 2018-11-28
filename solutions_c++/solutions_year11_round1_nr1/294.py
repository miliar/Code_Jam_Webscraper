#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <fstream>
#include <map>
#include <set>
#include <list>
#include <algorithm>

using namespace std;

typedef long long ll;

/*ll gcd(ll a, ll b){
	if(b == 0)return a;
	return gcd(b, a % b);
}*/

int gcd(int a,int b){
	if(b == 0)return a;
	return gcd(b, a % b);
}
/*
int isvalid(int d, int c, int C){
	for(int i = 0; ; ++i){
*/
int main()
{
	int T, pd, pg;
	ll n;
	int a, b, c, d, g1, g2;
	cin>>T;
	for(int tt = 1; tt <= T; ++tt){
		cin>>n>>pd>>pg;
		/*g1 = gcd(pd, 100);
		g2 = gcd(pg, 100);
		if(pd == 0){
			a = 0, b = 1;
		}else {
			a = pd / g1, b = 100 / g1;
		}
		if(pg == 0){
			c = 0, d = 1;
		}else {
			c = pg / g2, d = 100 / g2;
		}*/
		cout<<"Case #"<<tt<<": ";
		if(pd != 100 && pg == 100){
			cout<<"Broken"<<endl;
		}else if(pd != 0 && pg == 0){
			cout<<"Broken"<<endl;
		}else if(pd == 0 || pd == 100){
			cout<<"Possible"<<endl;
		}else {
			g1 = gcd(pd, 100);
			if(100 / g1 > n){
				cout<<"Broken"<<endl;
			}else {
				cout<<"Possible"<<endl;
			}
		}
	}
	return 0;
}


		
