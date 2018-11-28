#include <iostream>
#include <string>
#include <sstream>
#include <map>


using namespace std;

int main()
{
	map<char, char> translator;
	translator['a'] = 'y';
	translator['b'] = 'h';
	translator['c'] = 'e';
	translator['d'] = 's';
	translator['e'] = 'o';
	translator['f'] = 'c';
	translator['g'] = 'v';
	translator['h'] = 'x';
	translator['i'] = 'd';
	translator['j'] = 'u';
	translator['k'] = 'i';
	translator['l'] = 'g';
	translator['m'] = 'l';
	translator['n'] = 'b';
	translator['o'] = 'k';
	translator['p'] = 'r';
	translator['q'] = 'z';
	translator['r'] = 't';
	translator['s'] = 'n';
	translator['t'] = 'w';
	translator['u'] = 'j';
	translator['v'] = 'p';
	translator['w'] = 'f';
	translator['x'] = 'm';
	translator['y'] = 'a';
	translator['z'] = 'q';

	int T;
	string line, word, translated_word;
	char letter;
	bool is_uppercase;

	//Get the number of test cases
	cin >> T;

	//Get that end of line
	getline(cin, line);

	//For each test case
	for(int i = 0; i<T; ++i)
	{
		//Print test case thingy
		cout << "Case #" << i+1 << ":";

		//Read the line
		getline(cin, line);

		stringstream lineGetter(line);

		//Get each word
		while(lineGetter >> word)
		{
			//Clear the translated word
			translated_word = "";

			//And translate each letter
			for(int j = 0; j<word.length(); ++j)
			{

				//DEBUG:
//				cout << word[j] << " " << ((int)word[j]) << endl;

				//Check if it's uppercase, make it lowercase for the translation
				if(((int)word[j]) > 64 && ((int)word[j]) < 91)
				{
					is_uppercase = true;
					word[j] += 32;
				}
				else
					is_uppercase = false;
					
				//Translate it
				letter = translator.find(word[j])->second;

				//If it was uppercase, make the translation uppercase too
				if(is_uppercase)
					letter -= 32;

				//Add it to the translated word
				translated_word += letter;
			}

			//Show the translated word
			cout << " " << translated_word;
		}
		
		//Print newline
		cout << endl;
	}
}
