#include <iostream>

#define MAXVALUE 10000000

using namespace std;

/*
Patrick's adition is in fact bitwise XOR. So, if there are two piles equal for Patrick, that means they are bitwise equal, 
and we have that the XOR of the piles is 0. Since XOR is commutative and associative, we can pick any two piles, and if we XOR 
the totals (Patrick's), we get 0. Furthermore, the XOR of all candies is also going to be 0.
So we now know how to decide if it is possible or not, by comparing the XOR of all candies to 0.
Now we just have to pick the smallest non-empty pile for Patrick, which is obviously a pile composed by just the smallest candy.
Concluding, Sean gets all of them except the smallest.
*/
int main(){
	int iCases, nCases;
	cin >> nCases;
	
	int i, n, t;
	int min, sum, xsum;
	for (iCases=1; iCases <= nCases; iCases++){
		sum=0;
		xsum=0;
		min=MAXVALUE;
		cin >> n;
		
		for (i=0; i<n; i++){
			cin >> t;
			if (t<min)
				min=t;
			sum+=t;
			xsum^=t;
		}
		
		cout << "Case #" << iCases << ": ";
		if (xsum!=0)
			cout << "NO";
		else
			cout << sum-min;
		cout << endl;
	}
	return 0;
}
