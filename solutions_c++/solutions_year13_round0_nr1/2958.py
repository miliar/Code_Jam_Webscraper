// Danger! Too many bugs! HadronWave (c)
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <queue>
#include <deque>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <cmath>
#include <iomanip>
#include <functional>


using namespace std;

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;

const long long mod = 1000000007;

ll binpow(ll a,ll n){
    ll res = 1;
    while(n){
        if(n&1) res *= a;
        a *= a;
        res %= mod;
        a %= mod;
        n >>= 1;
    }
    return res;
}

int main() {
    int T;
	int x,o,t;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	vector<string> test(4);
	cin >> T;
	for(int c = 1;c<=T;++c){
		bool emp,f,s; emp = f = s = false;

		for(int i = 0;i<4;++i){
			cin >> test[i];
			if(!emp)
			for(int j=0;j<4;++j){
				if(test[i][j]=='.') {
					emp = true;
					break;
				}
			}
		}
		
		for(int i = 0;i<4;++i){
			x = o = t = 0;
			for(int j=0;j<4;++j){
				if(test[i][j]=='X') ++x;
				else if(test[i][j]=='O') ++o;
				else if(test[i][j]=='T') ++t;
			}
			if(x==4 || (x==3 && t)) f = true;
			else if(o==4 || (o==3 && t)) s = true;
		}

		for(int i = 0;i<4;++i){
			x = o = t = 0;
			for(int j=0;j<4;++j){
				if(test[j][i]=='X') ++x;
				else if(test[j][i]=='O') ++o;
				else if(test[j][i]=='T') ++t;
			}
			if(x==4 || (x==3 && t)) f = true;
			else if(o==4 || (o==3 && t)) s = true;
		}
		
		x = o = t = 0;

		for(int i = 0;i<4;++i){
			if(test[i][i]=='X') ++x;
			else if(test[i][i]=='O') ++o;
			else if(test[i][i]=='T') ++t;
		}
		
		if(x==4 || (x==3 && t)) f = true;
		else if(o==4 || (o==3 && t)) s = true;
		x = o = t = 0;

		for(int i = 0;i<4;++i){
			if(test[i][3-i]=='X') ++x;
			else if(test[i][3-i]=='O') ++o;
			else if(test[i][3-i]=='T') ++t;
		}
		
		if(x==4 || (x==3 && t)) f = true;
		else if(o==4 || (o==3 && t)) s = true;
		
		cout << "Case #" << c << ": ";
		
		if(!f && !s){
			if(emp)	cout << "Game has not completed";
			else cout  << "Draw";
		}else{
			if(f) cout << "X won";
			else if(s) cout << "O won";
		}
		cout << endl;
	}		
	return 0;
}