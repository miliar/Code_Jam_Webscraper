#include "stdlib.h"
#include "iostream"

using namespace std;

int main()
{
	int n;
	cin >> n;
	char s[101];
	cin.getline(s, 101, 10);
	string english = "qwertyuiopasdfghjklzxcvbnm ";
	string translate_english = "ztcprajkevydiwlbuomqhfgnsx ";
	for (int i = 0; i < n; i++) {
		cin.getline(s, 101, 10);
		cout << "Case #" << (i + 1) << ": ";
		for (int j = 0; s[j] != 0; j++) {
			int index = translate_english.find(s[j]);
			cout << english[index];
		}
		cout << endl;
	}
	return 0;
}
