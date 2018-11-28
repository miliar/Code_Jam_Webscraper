#include <iostream>
#include <string>
#include <cmath>

using namespace std;

#define infile "1.in"
#define outfile "1.out"

long long n, pd, pg;

long long MIN(long long a, long long b){
	if(a<=b) return a;
	else return b;
}

string solvecase(){
	if(pg==100){
		if(pd!=100) return "Broken";
		else return "Possible";
	}
	if(pg==0){
		if(pd!=0) return "Broken";
		else return "Possible";
	}


	for(long long d=1; d<=MIN(n, 10000); d++){
		if((d*pd)%100==0){
			for(long long k=0; k<100; k++){
				if((pg*d+pg*k)%100==0){
					//cout << d << " " << k ;
					return "Possible";
				}
			}
		}
	}
	return "Broken";
}

void solve(){
	int t;
	cin >> t;
	for(int i=0; i<t; i++){
		cin >> n >>  pd >> pg;
		cout << "Case #" << i+1 << ": " << solvecase() << endl;
	}
}

int main(){
	freopen(infile, "r", stdin);
	freopen(outfile, "w", stdout);
	solve();
	return 0;
}