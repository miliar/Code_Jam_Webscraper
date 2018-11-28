#include <iostream>
#include <fstream>
using namespace std;

int *create_digits_array(int x) {
	int z = x;

	// In case 0 ever shows up
	if(x == 0) {
		int *ans = new int[1];
		ans[0] =1;
		return ans;
	}

	// Count number of digits
	int numDigits = 1;
	while(z/10 != 0) {
		z /= 10;
		numDigits++;
	}

	int i = 1;
	int *ans = new int[numDigits];
	ans[0] = numDigits;
	do {
		ans[i] = x%10;
		i++;
		x /= 10;
	} while (x != 0);

	return ans;
}

int number_from_digits(int *digits) {
	int num = 0;
	for(int i = digits[0]; i > 0; i--) {
		num += digits[i];
		num *= 10;
	}
	num /= 10;

	return num;
}

void cycle_digits(int *digits) {
	// Make sure not to cycle the zero index
	
	// Highest digit
	int j = digits[1];

	// Shift all the others up one
	for(int i = 1; i < digits[0]; i++)
		digits[i] = digits[i+1];

	digits[digits[0]] = j;
}

int recycle_count(int a, int b) {

	int rCount = 0;
	for(int i = a; i < b; ++i) {
		int *c = create_digits_array(i);
		do {
			cycle_digits(c);
			int d = number_from_digits(c);
			
			if(d > i && d <= b)
				rCount++;

		} while(i != number_from_digits(c));

		delete c;
	}
	return rCount;	
}

int main(int argc, char **argv) {
	ifstream in(argv[1]);
	ofstream out(argv[2]);
	char killer[256];


	int num; in >> num; in.getline(killer,256);

	for(int i = 0; i < num; ++i) {
		int a, b;
		in >> a; in >> b; in.getline(killer,256);
		out << "Case #" << i+1 << ": " << recycle_count(a,b) << endl;
		cout << "Case #" << i+1 << ": " << recycle_count(a,b) << endl;
	}

	in.close();
	out.close();
	return 0;
}
