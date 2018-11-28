
#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;


int getPair(long a, long max, int len, ofstream & out){
	int sum =  0;
	long mod = 1, total = 1;
	
	for ( int i = 1 ; i <= len; i ++){
		total *= 10;
	}

	for ( int i = 1 ; i < len; i++){
		mod = mod * 10;
		long last =  a % mod;
		long first = a / mod;
		
		long b = last * total / mod + first;
		if ( (b <= max) && (b > a) )  {
			sum ++;
			//out << a <<","<< b <<endl;
		}
	}
	return sum;
}

int getLength(long num){
	int res = 0;
	while (( num /10 ) != 0){
		res++;
		num /= 10;
	}
	if ( num > 0 ) res++;
	return res;
}
int main(int argv, char** args){
	ifstream in;
	in.open("small.in");
	ofstream out;
	out.open("small.out");
	int T;
	long A,B;
	in >> T;
	
	for (int  i = 0; i < T; i++){
		in >> A >> B;
		long sum = 0;
		int len = getLength(B);
		for ( long j = A; j < B; j++){
			sum += getPair(j,B,len, out);
				
		}
		out << "Case #" << i+1 << ": " << sum << endl;
	}
	
}