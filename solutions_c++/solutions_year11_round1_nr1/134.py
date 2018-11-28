#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

//#define debug

#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()
#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef long long lint;

const int inf = 0x7fffffff;
const int white = 0, gray = 1, black = 2;

const int Size = 20000;

char buffer[Size];

lint gcd(lint a, lint b) {
	if(b == 0)
		return a;
	return gcd(b, a % b);
}

int solution(int nTest) {
	lint n;
	lint ch1, ch2;
	lint zn1 = 100, zn2 = 100;
	cin >> n >> ch1 >> ch2;
	lint c = gcd(ch1, zn1);
	ch1 /= c;
	zn1 /= c;
	c = gcd(ch2, zn2);
	ch2 /= c;
	zn2 /= c;

	printf("Case #%d: ", nTest + 1);


	if(zn1 > n) {
		puts("Broken");
		return 1;
		
	}
	

	lint d = zn1;
	lint a = zn2 - zn1 % zn2;
	lint g = ch1;
	lint l = (a + d) / zn2;
	l *= ch2;
	l -= g;
	//cerr << a << " " << l << endl;
	if(l < 0 || a < 0 || l > a) {
		puts("Broken");
		return 1;
	}


	puts("Possible");




	return 1;
}

int main() {
	freopen("input.txt", "r", stdin);
#ifndef debug
	freopen("output.txt", "w", stdout);
#endif

	int i = 0, n = 999999;

	scanf("%d", &n);

	while(i < n && solution(i))
		i++;

	return 0;
}

