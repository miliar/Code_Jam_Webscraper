#include <iostream>
#include <fstream>
using namespace std;

int get_next_num(int num);

int main (int argc, char * const argv[]) 
{
	char s[1000];
	cin >> skipws;
	cin >> s;
	int n = atoi(s);
	for (int i = 0; i < n; ++i) {
		cin >> s;
		int num = atoi(s);
		cerr << i+1 << ": read number " << num << "  ";
		num = get_next_num(num);
		cerr << "got number " << num << endl;
		cout << "Case #" << i+1 << ": " << num << endl;
	}
	return 0;
}

bool is_candidate(int num, int num_mod_9, int c, int digits[10])
{
	if (c % 9 != num_mod_9)
		return false;
	char b[100];
	sprintf(b, "%d", c);
	int cdigits[10] = {
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0
	};
	for (const char* p = b; *p != 0; ++p)
		++cdigits[*p - '0'];
	return memcmp(&digits[1], &cdigits[1], sizeof(int)*9) == 0;
}

int get_next_num(int num)
{
	char b[100];
	sprintf(b, "%d", num);
	int digits[10] = {
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
	};
	for (const char* p = b; *p != 0; ++p)
		++digits[*p - '0'];
	int num_mod_9 = num % 9;
	for (int i = num; ++i; ) {
		if (is_candidate(num, num_mod_9, i, digits))
			return i;
	}
	return -1;
}
