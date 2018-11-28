#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <map>
#include <cstring>
#include <string>
#include <cmath>

using namespace std;

	
int main(){

	freopen("b_small.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int cases;
	
	cin >> cases; 

	for (int casenum=1;casenum<=cases;casenum++){
		double L,P,C;
		int LL,PP,CC;
		cin >> LL >> PP >> CC;
		L = (double)LL;
		P = (double)PP;
		C = (double)CC; 
		
		double a = log(log(P/L)/log(C))/log(2.);
		int aa = (int)(a);
		double r = abs(a - aa*1.0);
		if (r>10e-10) aa++;
		if (P<=L*C) aa=0;
		cout << "Case #" << casenum << ": " << aa << endl;
	}

	return 0;
}