
#include <iostream>
#include <string>
#include <map>
using namespace std;

int get_size(int val) {
	int count = 0;
	while(val != 0) {
		val /= 10;
		count++;
	}

	return count;
}

int exp10(int val) {
	int value = 10;
	for (int i=1; i<val; i++) {
		value *= 10;
	}

	return value;
}

int moved_to_front(int value, int value_length, int esize, int size) {
	int new_value = value / esize;
	new_value += (value % esize) * exp10(value_length - size);
	return new_value;
}

bool recycled_pair(int n, int m, int size) {
	int section_size = 1;	
	int e_section_size = 1;
	for (section_size = 1, e_section_size = 10; section_size < size; section_size++, e_section_size *= 10) {
		if (n == moved_to_front(m, size, exp10(section_size), section_size)) {
			// cout << "section size: " << section_size << endl;
			return true;
		}
	}

	return false;
}

int main() {
	int c = 0, N;
	cin >> N;
	while (c++ < N) {
		int A, B;
		cin >> A >> B;
		int size = get_size(A);

		int count = 0;
		for (int n=A; n<B; n++) {
			for (int m=n+1; m<=B; m++) {
				if (recycled_pair(n, m, size)) {
					// cout << "   " << n << ", " << m << endl;
					count++;
				}
			}
		}

		cout << "Case #" << c << ": " << count << endl;
	}

	return 0;
}

