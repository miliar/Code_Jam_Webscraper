

#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include "BigIntegerLibrary.hh"

using namespace std;

//Input has to be supplied via command-line input redirection

BigInteger get_gcd(BigInteger a, BigInteger b){
    BigInteger c;
    if(a<b) {
        c = a; a = b; b = c;
    }
    while(1) {
		if(b==0)return a;
  		c = a%b;
  		if(c==0) return b;
  		a = b;
  		b = c;
    }
}

int main(int argc, char **argv){
	int C = 0; cin >> C;

	for(int i=0; i<C; i++){
		int N=0;cin >> N;
		vector<BigInteger> numbers;
		for(int n=0; n<N; n++){
			string s =""; cin>>s;
			BigInteger nn = stringToBigInteger(s);
			numbers.push_back(nn); 
		}

		sort(numbers.begin(), numbers.end(), less<BigInteger>());

		if(N==2){
			BigInteger third = numbers[1]+(numbers[1]-numbers[0]);		
			numbers.push_back(third);
			N++;
		}

		BigInteger gcd_num=numbers[0];
		for(int j=0; j<N; j++){
			gcd_num = get_gcd(gcd_num, numbers[j]);
		}
		//cout << "gcd = " << gcd_num << endl;

		vector<BigInteger> diff;
		for(int j=0; j<(N-1); j++){
			BigInteger d =0;
			d = numbers[j+1] - numbers[j];
			//cout << d << " ";
			diff.push_back(d);
		}
		//cout << endl;

		BigInteger gcd_diff=diff[0];
		for(int j=0; j<(N-1); j++){
			gcd_diff = get_gcd(gcd_diff, diff[j]);
		}
		//cout << "gcd = " << gcd_diff << endl;

		BigInteger Y = 0;
		//if(N == 2){
			//Y = gcd_num - gcd_diff;
			//if(Y < 0)Y*=-1;
		//}else{
			if((gcd_num - gcd_diff) == 0)Y=0;
			else Y = gcd_diff - (numbers[0]%gcd_diff);
		//}

		//cout << "Y : " << Y<< endl;
		cout << "Case #" << i+1 << ": " << bigIntegerToString(Y) << endl;
	}
}
