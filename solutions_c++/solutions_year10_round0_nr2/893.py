#include <iostream>
#include <vector>

using namespace std;

int findGcd(int a, int b) {
	if(b == 0)
		return a;
	
	return findGcd(b, a - b * (a / b));
	
}

int doCase() {
	int N;
	
	cin >> N;
	
	int gcd = 0;
	int minTime = INT_MAX;
	
	int first;
	
	cin >> first;
	
	gcd = 0;
	
	for(int i = 1; i < N; i++) {
		int num;
		cin >> num;
		
		if(num < minTime)
			minTime = num;

		num -= first;
		if(num == 0)
			continue;
		if(num < 0)
			num = -num;
		
		gcd = findGcd(gcd, num);
	}

	int futureTime = minTime % gcd;
	if(futureTime != 0)
		futureTime = gcd - futureTime;
	
	return futureTime;
}


int main (int argc, char * const argv[]) {

	int C;
	
	cin >> C;
	
	for(int i = 0; i < C; i++) {
		int result = doCase();
		
		cout << "Case #" << (i + 1) << ": " << result << endl;
	}
	
	
    return 0;
}
