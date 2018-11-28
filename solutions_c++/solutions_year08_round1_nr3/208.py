#include <iostream>
#include <cstdio>
using namespace std;

int main() 
{
	// Table of precomputed values, LOL. Thankyou my trusty Canon F-65
	int table[] = {1, 5, 27, 143, 751, 935, 607, 903, 991, 335, 47, 943, 471, 55, 447, 
		463, 991, 95, 607, 263, 151, 855, 527, 743, 351, 135, 407, 903, 791, 
		135, 647};
	
	int C;
	
	cin >> C;
	for (int cas=1; cas<=C;++cas)
	{
		
		int n;
		cin >> n;
		
		cout << "Case #" << cas << ": ";
		printf("%03d\n",table[n]);
	}
	return 0;
}