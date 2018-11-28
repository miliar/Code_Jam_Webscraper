#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

char letters[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main()
{
	freopen("A-small-attempt0.in", "rt" ,stdin);
	freopen("A-small-attempt0.out", "wt", stdout);
	int n;
	cin >> n;
	string line;
	getline(cin, line);
	for (int i=0; i < n; i++)
	{
		getline(cin, line);
		for (int j=0; j<line.size(); j++)
			if (line[j] != ' ')
				line[j] = letters[line[j] - 'a'];
		cout << "Case #" << i+1 << ": " << line << endl;
	}
	return 0;
}