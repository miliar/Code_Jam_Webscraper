#include <algorithm>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string key = "welcome to code jam";

unsigned int wordcount(const char *input, int index)
{
	unsigned int count = 0;
	char *string = const_cast<char *>(input);

	while (1) {
		char *ret = NULL;
		ret = strchr(string, key[index]);
		if (!ret) break;
		count += index < 18 ? wordcount(ret, index+1) : 1;
		count %= 10000;
		string = ret + 1;
	}

	return count;	
}

int main(void)
{
	unsigned int N;
	int i;
	string input;

	cin >> N;
	getline(cin, input);
	for (i = 0; i < N; i++) {
		unsigned int count = 0;

		getline(cin, input);
		count = wordcount(input.data(), 0);
		printf("Case #%d: %04d\n", i+1, count);
	}

	return 0;
}

