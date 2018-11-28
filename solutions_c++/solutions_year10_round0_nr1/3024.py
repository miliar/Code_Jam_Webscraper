#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

//code of suren

int main(){
	int T ;
	cin >> T ;
	for (int i = 1; i <= T; ++i) {
		int N,K;
		cin >> N >> K ;
		int test = (K+1)%int(pow(2.0,N));
		if(test==0) cout << "Case #" << i <<": ON" << endl ;
		else cout << "Case #" << i <<": OFF" << endl;
	}
	return 0;
}
