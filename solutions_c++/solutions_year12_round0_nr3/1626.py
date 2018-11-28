#include <iostream>
#include <bitset>

#define MAX 2000000

using namespace std;

int getMin(int len) {
	int min = len == 0 ? 0 : 1;
	int i;
	--len;
	for (i = 0; i < len; ++i) {
		min *= 10;
	}
	return min;
}

int getMax(int len) {
	return getMin(len + 1) - 1;
}

int intlen(int x) {
	int len = 0;
	while (x > 0) {
		++len;
		x /= 10;
	}
	return len;
}

void check(int store[], int &s_count, int tmp) {
	int i;
	for (i = 0; i < s_count; ++i) {
		if (store[i] == tmp)
			return;
	}
	store[s_count++] = tmp;
}

void inc_count(bitset<MAX+1> &bit, int &count, int len, int low, int high, int a, int b) {
	int min = getMin(len);
	for (int i = low; i <= high; ++i) {
		if (bit[i] == 1) {
			continue;
		}
		int tmp = i;
		int s_count = 0;
		for (int j = 0; j < len - 1; ++j) {
			tmp = tmp / 10 + (tmp % 10) * min;
			if (tmp != i && tmp >= a && tmp <= b && intlen(tmp) == len && !bit[tmp]) {
					bit.set(tmp, 1);
					++s_count;
			}
		}
		count += (s_count * (s_count + 1)) / 2;
	}
}

int main(int argc, char const *argv[])
{
	int t;
	cin >> t;
	for (int pt = 1; pt <= t; ++pt) {
		int a, b;
		cin >> a >> b;
		bitset<MAX + 1> bit;
		int lena = intlen(a);
		int lenb = intlen(b);
		int diff = lenb - lena;
		int count = 0;
		if (diff == 0) {
			inc_count(bit, count, lena, a, b, a, b);
		}
		else {
			inc_count(bit, count, lena, a, getMax(lena), a, b);
			for (int j = 1; j < diff; ++j) {
				inc_count(bit, count, lena + j, getMin(lena + j), getMax(lena + j), a, b);
			}
			inc_count(bit, count, lenb, getMin(lenb), b, a, b);
		}
		cout << "Case #" << pt << ": " << count << endl;
	}
	return 0;
}