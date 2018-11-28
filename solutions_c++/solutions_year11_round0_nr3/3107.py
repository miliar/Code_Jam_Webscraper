#include <iostream>
#include <cstdio>
#include <vector>
#include <math.h>
#include <string>
#include <cstdlib>
#include <sstream>
#include <limits.h>

using namespace std;

int main()
{
	int t,n,test = 0;
	cin >> t;
	
	while(t--){
		cin >> n;
		test++;
		int *A = new int[n];
		int c = 0;
		int xr = 0;
		int sum = 0;
		int mval = INT_MAX;

		for(int i=0;i<n;i++){
			cin >> A[i];
			xr ^= A[i];
			mval = min(mval , A[i]);
			sum += A[i];
		}

		if(xr == 0)
			c = 1;
		if(c == 0)
			cout << "Case #" << test << ": " << "NO\n";
		else
			cout << "Case #" << test << ": " << sum-mval << "\n";
	}
		
	return 0;
}
