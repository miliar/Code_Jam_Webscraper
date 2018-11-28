#include <iostream>
#include <string>

using namespace std;

typedef unsigned int uint;
typedef unsigned long ulong;

int main()
{
	uint T;
	string input;
	
	ios_base::sync_with_stdio(false);
	
	/* Character Map */
	char decode[] = "yhesocvxduiglbkrztnwjpfmaq";
	
	/* Read number of cases */
	cin >> T;
	getline(cin, input);

	for (uint t = 1; t <= T; ++t)
	{
		/* Read the line */
		getline(cin, input);
		
		/* Decode the input */
		for (uint i = 0; i < input.size(); ++i)
		{
			if (input[i] != ' ')
				input[i] = decode[input[i] - 'a'];
		}
		
		/* Display the output */
		cout << "Case #" << t << ": ";
		cout << input << "\n";
	}
	
	cout.flush();

	return 0;
}

