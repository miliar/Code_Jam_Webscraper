/*
 * Round1A_A.cpp
 *
 *  Created on: 2011/05/21
 *      Author: masamichi1222
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int gcd(int a, int b)
{
	while(a != b) {
		if (a < b) b -= a;
		else a -= b;
	}
	return a;
}

int main( )
{
	int tt, N, PD, PG;

	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	int gc[101];
	gc[0] = 1;
	for(int i=1; i<101; i++){
		gc[i] = gcd(i,100);
//		cout << gc[i] << endl;
	}

	cin >> tt;
	for(int t = 1; t <= tt; ++ t )
	{
		cin >> N;
		cin >> PD;
		cin >> PG;

		string ans = "Possible";
		if(PD!=100 && PG==100) ans = "Broken";
		if(PD!=0 && 100/gc[PD]>N) ans = "Broken";
		if(PD!=0 && PG==0) ans = "Broken";

//		cout << N << " : " << PD << " : " << PG << " ";
		cout << "Case #" << t << ": " << ans << endl;
	}

	return 0;
}
