/** Used Matt McCutchen's C++ Big Integer Library **/
/** http://mattmccutchen.net/bigint/ **/

#include <stdio.h>
#include <iostream>
#include <string>
#include "bigint/BigIntegerLibrary.hh"
#define	MAX	1024

using namespace std;

BigInteger t[MAX];
BigInteger diff[MAX];

BigInteger gcd(BigInteger a, BigInteger b){
	BigInteger r = a%b;
	if(r==0)
		return b;
	else
		return gcd(b,r);
}
int main(){
	int C,tc,i,j,N;
	string str;
	BigInteger gcds;

	scanf("%d", &C);
	for(tc=1;tc<=C;tc++){
		scanf("%d", &N);
		for(i=0;i<N;i++){
			cin >> str;
			t[i] = stringToBigInteger(str);
		}

		for(i=0,j=0;i<N-1;i++){
			if((t[i+1]-t[i]) > (BigInteger) 0)
				diff[j] = t[i+1]-t[i];
			else
				diff[j] = t[i]-t[i+1];

			if(diff[j]!=0)
				j++;
//			cout << diff[i] << " ";
		}
//		printf("\n");
		gcds = diff[0];
		for(i=1;i<j;i++)
			gcds = gcd(gcds, diff[i]);

		if(t[i]%gcds == 0)
			gcds = 0;
		else
			gcds -= t[i]%gcds;

		cout << "Case #" << tc << ": " << gcds << endl;

	}
    return 0;
}

