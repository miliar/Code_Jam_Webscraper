#include <iostream>
#include <vector>
#include <map>
#include <stdlib.h>
#include <limits.h>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for(int t=1; t<=T; t++){
		int N;
		int add=0, sum=0, minPrice=INT_MAX;
		cin >> N;
		for(int n=0; n<N; n++){
			int p;
			cin >> p;
			add ^= p;
			sum += p;
			minPrice = min(minPrice, p);
		}
		if (add != 0)  cout << "Case #" << t << ": NO" << endl;
		else  cout << "Case #" << t << ": " << sum-minPrice<< endl;
	}
	return 0;
}

