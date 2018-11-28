#include <iostream>
#include <fstream>

using namespace std;

int main (void)
{
	cout << "Starting" << endl;

	//open the file
	ifstream inFile ("A-small-attempt0.in");
	ofstream outFile ("A-small-attempt0.out");

	//get the number of cases
	int N;
	inFile >> N;

	inFile.get();

	for (int n = 1; n <= N; n++)
	{
		cout << "Start case" << endl;

		outFile << "Case #" << n << ": ";

		char in, out;

		in = inFile.get();
	
		while (in != '\n' && in != EOF)
		{
			switch (in)
			{
			case 'a':
				out = 'y';
				break;
			case 'b':
				out = 'h';
				break;
			case 'c':
				out = 'e';
				break;
			case 'd':
				out = 's';
				break;
			case 'e':
				out = 'o';
				break;
			case 'f':
				out = 'c';
				break;
			case 'g':
				out = 'v';
				break;
			case 'h':
				out = 'x';
				break;
			case 'i':
				out = 'd';
				break;
			case 'j':
				out = 'u';
				break;
			case 'k':
				out = 'i';
				break;
			case 'l':
				out = 'g';
				break;
			case 'm':
				out = 'l';
				break;
			case 'n':
				out = 'b';
				break;
			case 'o':
				out = 'k';
				break;
			case 'p':
				out = 'r';
				break;
			case 'q':
				out = 'z';
				break;
			case 'r':
				out = 't';
				break;
			case 's':
				out = 'n';
				break;
			case 't':
				out = 'w';
				break;
			case 'u':
				out = 'j';
				break;
			case 'v':
				out = 'p';
				break;
			case 'w':
				out = 'f';
				break;
			case 'x':
				out = 'm';
				break;
			case 'y':
				out = 'a';
				break;
			case 'z':
				out = 'q';
				break;
			case ' ':
				out = ' ';
				break;
			}

			//output the translation
			outFile << out;

			in = inFile.get();
		}

		outFile << endl;
	}

	inFile.close();
	outFile.close();

	return 0;
}