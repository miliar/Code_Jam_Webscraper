#include <iostream>
#include <cstdlib>
#include <sstream>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define abs(x) ((x) > 0 ? (x) : -1*(x))
#define max(x, y) ((x) > (y) ? (x) : (y))
#define min(x, y) ((x) < (y) ? (x) : (y))

int numpos(int A)
{
	int pos = 0;
	
	while(A) {
		pos++;
		A /= 10;
	}
	
	return pos;
}

int rotate(int A, int pos)
{
	int num = 1;
	pos = pos - 1;
	
	while(pos--) {
		num *= 10;
	}
	
	return (A - (A % num)) / num + (A % num)*10;
}

int main()
{
	int T, A, B, pos, x;
	
	cin >> T;
	
	for(int i = 1; i <= T; i++) {
		int pair = 0;

		cin >> A;
		cin >> B;

		for (int j = A; j <= B; j++) {
			pos = numpos(j);
			x = rotate(j, pos);
		
			while (x != j) {
				if (x > j && x <= B) pair++;
				x = rotate(x, pos);
			}
		}
		
		cout << "Case #" << i << ": " << pair << endl;
	}
	
	return 0;
}
