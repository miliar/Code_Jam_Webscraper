#include <iostream>

using namespace std;

int main()
{
	char map[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	int T;
	cin >> T;
	cin.ignore();
	int num = 1;
	for(num; num<=T; num++)
	{
		string input;
		getline(cin, input);

		cout << "Case #"<<num<<": ";
		for(int i=0; input[i] != '\0'; i++)
		{
			if( input[i] == ' ')	
				{
					cout << " ";
					continue;
				}
			int index = input[i] - 'a';
			cout << map[index];
		
		}
		cout << "\n";

	}
	return 0;
}
