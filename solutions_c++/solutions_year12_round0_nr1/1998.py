#include <iostream>
#include <string>
using namespace std;

char decode[] = "yhesocvxduiglbkrztnwjpfmaq";

int main()
{
	int T;
	cin >> T;
	getchar();
	for (int i = 1; i <= T; ++i) {
		string str;
		getline(cin, str);
		for (int j = 0; j < str.size(); ++j) {
			if (str[j] < 'a' || str[j] > 'z') continue;
			str[j] = decode[str[j] - 'a'];
		}
		cout << "Case #" << i << ": ";
		cout << str << endl;
	}

	return 0;
}
