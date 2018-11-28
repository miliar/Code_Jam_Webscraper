#include <iostream>
using namespace std;

int get_digits(long num) {
	int digits=0;
	for (; num>0; num/=10)
		digits++;
	return digits;
}

int main() {
	int T=0, cases=0;
	long A=0, B=0, m=0, n=0, result=0;
	int digits=0;
	long i, j;
	cin>>T;
	for (cases=1; cases<=T; cases++) {
		cin>>A>>B;
		result=0;
		for (m=A; m<B; m++) {
			n=m;
			digits=0;
			j=1;
			for (; n>0; n/=10) {
				digits++;
				j*=10;
			}
			j/=10;
//cout<<"digits="<<digits<<" , j="<<j<<endl;
			for (n=m, i=digits-1; i>0; i--) {
				n=(n/10)+(j*(n%10));
				if (n>m && n<=B) {
//cout<<m<<"\t"<<n<<endl;
					result++;
				}
			}
		}
		cout<<"Case #"<<cases<<": "<<result<<endl;
	}
	return 0;
}
