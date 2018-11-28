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

	freopen("a_large.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	int cases;
	long N,K;

	cin >> cases;

	for (int casenum=1; casenum<=cases; casenum++){
		cin >> N >> K;
		if ((K+1)%(1<<N)==0) cout << "Case #" << casenum << ": ON" << endl;
		else cout << "Case #" << casenum << ": OFF" << endl;
	}

	return 0;
}