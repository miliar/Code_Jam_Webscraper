#include <iostream>

using namespace std;
int main () {
char arr[26] = {
	'y', 'h', 'e', 's', 'o', // a b c d e
	'c', 'v', 'x', 'd', 'u', // f g h i j
	'i', 'g', 'l', 'b', 'k', // k l m n o
	'r', 'z', 't', 'n', 'w', // p q r s t
	'j', 'p', 'f', 'm', 'a', 'q'// u v w x y z
};
freopen("1.txt", "r",stdin);
freopen("1o.txt", "w+",stdout);

	int n, num = 1;
	cin >> n;
	char s[105];
	cin.getline (s, 105);
	while (n--) {
	char s[105];
	cin.getline (s, 105);
	int len = strlen (s);
		for (int i = 0; i < len; i++) {
			if (s[i] != ' ')
				s[i] = arr[ s[i] - 'a' ];
		}
	
	cout << "Case #" << num << ": " << s << endl;
	num++;
	}

};
