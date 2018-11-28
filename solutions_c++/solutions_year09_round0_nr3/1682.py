#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>

using namespace std;

const string welcome = "welcome to code jam";
const int length = welcome.size();

void CalculateTime(_int64 ** bottomUp, string text, int numChars)
{
	for (int i = numChars; i >= 0; i--)
		bottomUp[i][length] = 1;
	for (int j = length; j >=0; j--)
		bottomUp[numChars][j] = 0;
	bottomUp[numChars][length] = 1;

	for (int i = numChars - 1; i >=0; i--)
		for (int j = length - 1; j >=0; j--) {
			int it = i;
			bottomUp[i][j] = 0;
			if (numChars - i >= length - j) {
				if (text[i] == welcome[j]) {
					bottomUp[i][j] += bottomUp[i+1][j+1];
					it++;
				}
				while (welcome[j] != text[it] && it < numChars)
					it++;

				bottomUp[i][j] += bottomUp[it][j];
			}
		}
}

int main()
{
	ifstream in;
	in.open("C-small-attempt1.in");
    ofstream out;
	out.open("result.txt");
    
	string temp;
	getline(in, temp);

	int cases = atoi(temp.c_str());

	for (int count = 0; count < cases; count++) {
		string text;
		getline(in, text);
	
		const int numChars = text.size();

		_int64 ** bottomUp = new _int64* [numChars+1];

		for (int i = 0; i <= numChars; i++) 
			bottomUp[i] = new _int64[length+1];

		CalculateTime(bottomUp, text, numChars);

		/*

		for(int i = 0; i <= numChars; i++) {
			for (int j = 0; j <= length; j++)
				cout << bottomUp[i][j];
			cout << endl;
			}
			*/

		int result = bottomUp[0][0] % 10000;
        
		
		int add = 0;
		if (result < 1000)
			add++;
		if (result < 100)
			add++;
		if (result < 10)
			add++;
	

		out << "Case #" << count + 1 <<": ";

		for (int i = 0; i < add; i++)
			out << "0";
		out << result << endl; 

		for (int i = 0; i <= numChars; i++)
			delete [] bottomUp[i];
        
		delete [] bottomUp;
	}
	in.close();
	out.close();
	return 0;

}
