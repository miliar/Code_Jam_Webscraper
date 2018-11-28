#include <cstdlib>
#include <iostream>

using namespace std;

char sub[] = "yhesocvxduiglbkrztnwjpfmaq";

int
main ()
{
	int N;
	string input;
	
	cin >> N;
	cin.ignore ();
	
	for (int j = 1; j <= N; j++)
	{
		getline(cin, input);
		
		cout << "Case #" << j << ": ";
		for (int i = 0; i < input.size (); i++) {
			cout << ((input[i] == ' ') ? input[i] : sub[input[i]-'a']);
		}
		cout << endl;
	}
	
	return EXIT_SUCCESS;
}
