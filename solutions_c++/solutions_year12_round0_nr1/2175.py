#include <iostream>
#include <string>

using namespace std;

int main()
{
	static const char mapping[] = "yhesocvxduiglbkrztnwjpfmaq";
	
	int T;
	cin >> T;

	cin.get(); // get the first \n, for getline to work properly

	for (int nTestCase = 1; nTestCase <= T; nTestCase++)
	{
		string G;

		getline(cin, G);
		for (string::iterator c = G.begin(); c != G.end(); ++c)
			if (*c != ' ')
				*c = mapping[*c - 'a'];

		cout << "Case #" << nTestCase << ": " << G << endl;
	}

	return 0;
}
