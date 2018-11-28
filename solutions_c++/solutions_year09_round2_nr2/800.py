#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <stack>
#include <set>
#include <sstream>
#define sz size()
#define MP make_pair
#define eps (1e-9)
using namespace std;
typedef long long int64;

int main() {	   
	int t, i;
	string a;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> t;
	for (i = 1; i <= t; i++){
		cin >> a;
		if (!next_permutation(a.begin(), a.end())){
			a += "0";
			sort(a.begin(), a.end());
			swap(a[0], a[a.find_first_of("123456789")]);
		}
		cout << "Case #" << i << ": " << a << '\n';
		
	}


	return 0;
}