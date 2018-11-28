#include <iostream>
#include <math.h>
using namespace std;
//returns the number of digits in the int
int numDigits(int in){
	int numDigits = 0;
	while(in > 0){
		numDigits++;
		in = in/10;
	}
	return numDigits;
}

//shifts the digigits 1 to the right, with the en being placed at the start
int shift(int in, int digits){
	int out = 0;
	out = in / 10;
	out = pow(10, digits-1)*(in%10) + out;
	return out;
}//shift

int main() {
	int N,A,B;
	cin>>N;
	for (int n=1; n <= N; n++){
		cout<<"Case #"<<n<<": ";
		cin>>A>>B;
		int digits = numDigits(A);
		int count = 0;
		for (int a=A; a<=B; a++){
			int b = a;
			do{
			b = shift(b, digits);
			if (b<=B && b>=A && b!=a)
				count++; 
			}while(b!=a);
		}
		cout<<(count/2)<<endl;
	}//for
}
