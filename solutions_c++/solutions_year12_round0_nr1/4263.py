#include <iostream>
#include <string>
#include <map>

using namespace std;

int main()
{
	int t;
	string g;
	map<char, char> decryption;
	
	decryption.insert(make_pair('a', 'y'));
	decryption.insert(make_pair('b', 'h'));
	decryption.insert(make_pair('c', 'e'));
	decryption.insert(make_pair('d', 's'));
	decryption.insert(make_pair('e', 'o'));
	decryption.insert(make_pair('f', 'c'));
	decryption.insert(make_pair('g', 'v'));
	decryption.insert(make_pair('h', 'x'));
	decryption.insert(make_pair('i', 'd'));
	decryption.insert(make_pair('j', 'u'));
	decryption.insert(make_pair('k', 'i'));
	decryption.insert(make_pair('l', 'g'));
	decryption.insert(make_pair('m', 'l'));
	decryption.insert(make_pair('n', 'b'));
	decryption.insert(make_pair('o', 'k'));
	decryption.insert(make_pair('p', 'r'));
	decryption.insert(make_pair('q', 'z'));
	decryption.insert(make_pair('r', 't'));
	decryption.insert(make_pair('s', 'n'));
	decryption.insert(make_pair('t', 'w'));
	decryption.insert(make_pair('u', 'j'));
	decryption.insert(make_pair('v', 'p'));
	decryption.insert(make_pair('w', 'f'));
	decryption.insert(make_pair('x', 'm'));
	decryption.insert(make_pair('y', 'a'));
	decryption.insert(make_pair('z', 'q'));
	
	cin >> t;
	
	string line;
	
	getline(cin, line);
	
	for (int i = 0; i < t; i++)
	{
		getline(cin, g);
		
		for (int j = 0; j < g.size(); j++)
		{
			if (decryption.find(g[j]) != decryption.end())
			{
				g[j] = decryption[g[j]];
			}
		}
		
		cout << "Case #" << i + 1 << ": " << g << '\n';
	}
}
