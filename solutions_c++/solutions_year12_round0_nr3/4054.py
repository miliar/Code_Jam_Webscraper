#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
using namespace std;


set< pair<int, int> > sols;
int A, B;

void solve(int n){
	if(n < 10 || n % 10 == 0)
		return;
	int a = n;
	int digits = (int)log10(n);
	int times = powl(10, digits);
	do{
		n = (n % 10) * times + (n / 10);
		if(n >= A && n <= B && n != a)
			sols.insert(make_pair(min(a, n), max(a, n)));
		//cout << n << endl;
	}while(n != a);
}

int main(){
	freopen("in.in", "r", stdin);
	int T;
	cin >> T;
	for(int c = 1; c <= T; c++){
		cin >> A >> B;
		sols.clear();
		for(int i = A; i <= B; i++){
			solve(i);
		}
		cout << "Case #" << c << ": " << sols.size() << endl;
		/*
		for(set<pair<int, int> >::iterator it = sols.begin(); it != sols.end(); it++){
			cout << it->first << " " << it->second << endl;
		}
		//*/
	}
	return 0;
}

