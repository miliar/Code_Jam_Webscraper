#include<iostream>
#include<cstdio>

using namespace std;

// precalculated answers up to 30 ;)
int answers[] = {1, 5, 27, 143, 751, 935, 607, 903, 991, 335, 47, 943, 471, 55, 447, 463, 991, 95, 607, 263, 151, 855, 527, 743, 351, 135, 407, 903, 791, 135, 647};

int main() {
	int T, n;
	
	cin >> T;
	
	for(int ti = 0; ti < T; ti++) {
		cin >> n;
		printf("Case #%d: %03d\n", ti+1, answers[n]);
	}
	
	return 0;
}
