#include <iostream>
#include <string.h>
#include <stdlib.h>

using namespace std;

int main()
{
//	char code[] = "ynficwlbkuomxsevzpdrjgthaq";
//	char code[] = "abcdefghijklmnopqrstuvwxyz";
	char code[] = "yhesocvxduiglbkrztnwjpfmaq";
	char ch, input[101];
	int cases, count = 1;

	cin.getline(input, 101);
	cases = atoi(input);

	while(cases > 0) {
		cin.getline(input, 101);
		cout << "Case #" << count << ": ";
		for (int i = 0; i < strlen(input); i++) {
			ch = input[i];
			if (ch >= 'a' && ch <= 'z') {
				ch = code[ch - 'a'];
			}
			cout << ch;
		}
		cout << "\n";
		cases--;
		count++;
	}
	return 0;
}