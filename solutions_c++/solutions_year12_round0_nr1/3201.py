// Problem A. Speaking in Tongues
#include <iostream>
#include <string>
#include <algorithm>

const char *map = "yhesocvxduiglbkrztnwjpfmaq";

void decode(char &c) {
	if (c == ' ') return;
	
	c = *(map + c - 'a');
}

int main()
{
	using namespace std;

	int n;
	cin >> n;
	string s;
	getline(cin, s);

	for (int i = 1; i <= n; ++i) {
		getline(cin, s);
		for_each(s.begin(), s.end(), decode);
		printf("Case #%d: %s\n", i, s.c_str());
	}

	return 0;
}




