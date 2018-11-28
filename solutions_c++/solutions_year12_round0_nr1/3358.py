#include <iostream>
#include <map>

//a b c d e f g h i j k l m n o p q r s t u v w x y z
//y n f i c w l b k u o m x s e v z p d r j g t h a q

using namespace std;

int main() {
	map<char, char> m;

	m.insert(make_pair('y', 'a'));
	m.insert(make_pair('n', 'b'));
	m.insert(make_pair('f', 'c'));
	m.insert(make_pair('i', 'd'));
	m.insert(make_pair('c', 'e'));
	m.insert(make_pair('w', 'f'));
	m.insert(make_pair('l', 'g'));
	m.insert(make_pair('b', 'h'));
	m.insert(make_pair('k', 'i'));
	m.insert(make_pair('u', 'j'));
	m.insert(make_pair('o', 'k'));
	m.insert(make_pair('m', 'l'));
	m.insert(make_pair('x', 'm'));
	m.insert(make_pair('s', 'n'));
	m.insert(make_pair('e', 'o'));
	m.insert(make_pair('v', 'p'));
	m.insert(make_pair('z', 'q'));
	m.insert(make_pair('p', 'r'));
	m.insert(make_pair('d', 's'));
	m.insert(make_pair('r', 't'));
	m.insert(make_pair('j', 'u'));
	m.insert(make_pair('g', 'v'));
	m.insert(make_pair('t', 'w'));
	m.insert(make_pair('h', 'x'));
	m.insert(make_pair('a', 'y'));
	m.insert(make_pair('q', 'z'));

	int n;
	cin >> n;
	cin.ignore(1);

	for (int i = 0; i < n; i++) {
		string line;
		string answer;
		getline(cin, line);

		for (int j = 0; j < line.size(); j++) {
			char lookup = line[j];
			if (m.find(lookup) != m.end())
				answer += m[lookup];
			else
				answer += lookup;
		}

		cout << "Case #" << i+1 << ": " << answer << endl;
	}
}
