#include <iostream>
#include <string>

using namespace std;

void main()
{
	int n;

	cin >> n;
	cin.clear(); cin.ignore(INT_MAX,'\n');
	for (int i = 0; i < n; i++)
	{
		string output;
		char input[110];
		cin.getline(input, 110);

		int k = 0;
		while (input[k] != 0)
		{
			switch (input[k])
			{
			case 'a': output.push_back('y'); break;
			case 'b': output.push_back('h'); break;
			case 'c': output.push_back('e'); break;
			case 'd': output.push_back('s'); break;
			case 'e': output.push_back('o'); break;
			case 'f': output.push_back('c'); break;
			case 'g': output.push_back('v'); break;
			case 'h': output.push_back('x'); break;
			case 'i': output.push_back('d'); break;
			case 'j': output.push_back('u'); break;
			case 'k': output.push_back('i'); break;
			case 'l': output.push_back('g'); break;
			case 'm': output.push_back('l'); break;
			case 'n': output.push_back('b'); break;
			case 'o': output.push_back('k'); break;
			case 'p': output.push_back('r'); break;
			case 'q': output.push_back('z'); break;
			case 'r': output.push_back('t'); break;
			case 's': output.push_back('n'); break;
			case 't': output.push_back('w'); break;
			case 'u': output.push_back('j'); break;
			case 'v': output.push_back('p'); break;
			case 'w': output.push_back('f'); break;
			case 'x': output.push_back('m'); break;
			case 'y': output.push_back('a'); break;
			case 'z': output.push_back('q'); break;
			default: output.push_back(input[k]);
			}
			k++;
		}

		cout << "Case #" << i + 1 << ": " << output << endl;
	}
}
