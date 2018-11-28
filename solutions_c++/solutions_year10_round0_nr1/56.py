#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <stack>
#include <sstream>
#include <cmath>
#include <map>

using namespace std;

int main(void){
	int n;
	cin >> n;
	for(int i = 0; i < n; i++){
		int N, K;
		cin >> N >> K;

		cout << "Case #" << (i+1) << ": ";
		if((K%(1<<N)) == (1<<N)-1) cout << "ON" << endl;
		else cout << "OFF" << endl;
	}
	return 0;
}
