#include <stdio.h>
#include <iostream>
#include <vector>
#include <list>
#include <cmath>
#include <fstream>
#include <algorithm>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <complex>
#include <iterator>
#include <cstdlib>

using namespace std;

#define EPS (1e-10)
#define EQ(a,b) (abs((a) - (b)) < EPS)
#define EQV(a,b) (EQ((a).real(),(b).real()) && EQ((a).imag(),(b).imag()))

typedef complex<double> P;
typedef long long ll;

const int MAX_SIZE = 10000;

long long N;
ll PD;
ll PG;

void yakubun(ll &a,ll&b){
	for(ll i = 2; i <= max(a,b); i++){
		if(a%i==0 && b%i==0){
			a/=i;
			b/=i;
			i--;
		}
	}
}

bool solve(){

	if(PG==100){
		if(PD!=100)
			return false;
	}
	else if(PG==0){
		if(PD!=0)
			return false;
	}

	// –ñ•ª
	ll a,b;
	a = PD;
	b = 100;
	yakubun(a,b);
	
	if(b > N){
		return false;
	}

	return true;
	
	//int c,d;
	//c = PG;
	//d = 100;

	//int e = d - b;
	//int f = c - a;
	//if(f > e)
	//	return false;
	//return true;

}

int main(){

	ifstream ifs("input.txt");
	ofstream ofs("output.txt");

	int t;
	ifs >> t;
//	cin >> t;
	for(int i = 0; i < t; i++){
		//cin >> N >> PD >> PG;
		ifs >> N >> PD >> PG;
//		cout << "Case #" << i+1 << ": " << flush;
		ofs << "Case #" << i+1 << ": " << flush;
		if(solve()){
		//	cout << "Possible" << endl;
			ofs << "Possible" << endl;
		}
		else{
			ofs << "Broken" << endl;
//			cout << "Broken" << endl;
		}
	}

	int x;
	cin >> x;

	return 0;
}