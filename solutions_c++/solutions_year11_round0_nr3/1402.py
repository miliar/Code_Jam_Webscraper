#include <iostream>
using namespace std;

int main()
{
	int tests;
	int candyamount;
	int candyvalues[1000];
	bool gonext = false;
	int xorsum;
	int sum;
	int minvalue;
	cin >> tests;
	for(int i = 1; i<=tests; i++){
		xorsum = 0;
		sum = 0;

		cin >> candyamount;
		for(int j=0; j<candyamount; j++){
			cin >> candyvalues[j];
		}

		minvalue = candyvalues[0];
		for(int j=0; j<candyamount; j++){
			xorsum^=candyvalues[j];
			sum+=candyvalues[j];
			if(candyvalues[j]<minvalue){
				minvalue = candyvalues[j];
			}
		}
		if (xorsum != 0){
			cout << "Case #" << i << ": NO\n";
		}
		else{
			cout << "Case #" << i << ": " << sum-minvalue << "\n";
		}
	}
	cin >> tests;
}