#include <iostream>
#include <string>
using namespace std;

char map[] = "yhesocvxduiglbkrztnwjpfmaq";
int main(void)
{
    int kiss = 1, count;
    string s;
    int i;;
    for (cin >> count, cin.get(); kiss <= count; kiss++) {
	s = "";
	getline(cin, s);
	cout << "Case #" << kiss << ": ";
	for (i = 0; i < s.length(); i++)
	    if (s[i] >= 'a' && s[i] <= 'z')
		cout << map[s[i] - 'a'];
	    else
		cout << s[i];
	cout << endl;
    }
    return 0;
}
