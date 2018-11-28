#include <iostream>
#include <string>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.in","w",stdout);
	int testcases;
	cin >> testcases;
	cin.ignore();
	for(int i = 0; i < testcases; i++){
		string input;
		getline(cin, input);
		for(int j = 0; j < input.length(); j++){
			if(input[j] == ' ')
				continue;
			else if(input[j] == 'y')
				input[j] = 'a';
			else if(input[j] == 'n')
				input[j] = 'b';
			else if(input[j] == 'f')
				input[j] = 'c';
			else if(input[j] == 'i')
				input[j] = 'd';
			else if(input[j] == 'c')
				input[j] = 'e';
			else if(input[j] == 'w')
				input[j] = 'f';
			else if(input[j] == 'l')
				input[j] = 'g';
			else if(input[j] == 'b')
				input[j] = 'h';
			else if(input[j] == 'k')
				input[j] = 'i';
			else if(input[j] == 'u')
				input[j] = 'j';
			else if(input[j] == 'o')
				input[j] = 'k';
			else if(input[j] == 'm')
				input[j] = 'l';
			else if(input[j] == 'x')
				input[j] = 'm';
			else if(input[j] == 's')
				input[j] = 'n'; 
			else if(input[j] == 'e')
				input[j] = 'o';
			else if(input[j] == 'v')
				input[j] = 'p';
			else if(input[j] == 'z')
				input[j] = 'q';
			else if(input[j] == 'p')
				input[j] = 'r';
			else if(input[j] == 'd')
				input[j] = 's';
			else if(input[j] == 'r')
				input[j] = 't';
			else if(input[j] == 'j')
				input[j] = 'u';
			else if(input[j] == 'g')
				input[j] = 'v';
			else if(input[j] == 't')
				input[j] = 'w';
			else if(input[j] == 'h')
				input[j] = 'x';
			else if(input[j] == 'a')
				input[j] = 'y';
			else if(input[j] == 'q')
				input[j] = 'z';
		}
		cout << "Case #" << i+1 << ": " << input << endl;
	}
	return 0;
}