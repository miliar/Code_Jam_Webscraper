#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#define LL long long
using namespace std;

int gcd(int x, int y){
	int z = x % y;
	while (z){
		x = y;
		y = z;
		z = x % y;
	}
	return y;
}

bool check(LL n, int p1, int p2){
	int x, y;
	if (p1 == 0){
		x = 0;
		y = 1;
	}
	else{
		x = p1 / gcd(100, p1);
		y = 100 / gcd(100, p1);
	}

	if (y > n)
		return 0;

	if (p2 == 0){
		if (x == 0)
			return 1;
		else
			return 0;
	}

	if (p2 == 100){
		if (x == y)
			return 1;
		else
			return 0;
	}

	return 1;
}

int main(){
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);

	int t;
	cin >> t;
	LL n;
	int p1, p2;
	for (int i = 1; i <= t; i++){
		cin >> n >> p1 >> p2;
		if (check(n, p1, p2))
			cout << "Case #" << i << ": " << "Possible\n";
		else
			cout << "Case #" << i << ": " << "Broken\n";
	}

	return 0;
}
