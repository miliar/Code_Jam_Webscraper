#include <iostream>

using namespace std;

int A1, A2, B1, B2;

bool loosing(int a, int b);

bool winning(int a, int b) {
	int c;
	if(a < b) {
		c = a; a = b; b = c;
	}
	c = a / b * b;
	return loosing(a-c, b) || (c > b && loosing(a-c+b, b));
}

bool loosing(int a, int b) {
	if(a == b)
		return true;
	int c;
	if(a < b) {
		c = a; a = b; b = c;
	}
	if(b + b > a)
		return winning(b, a-b);
	else
		return false;
}

int count() {
	int c = 0;
	for(int i=A1; i<=A2; i++)
		for(int j=B1; j<=B2; j++)
			if(winning(i,j))
				c ++;
	return c;
}

int main(int argc, char* argv) {
	int T;
	cin >>T;
	for(int i=0; i<T; i++) {
		cin >>A1 >>A2 >>B1 >>B2;
		cout <<"Case #" <<i+1 <<": " <<count() <<endl;
	}
	return 0;
}
