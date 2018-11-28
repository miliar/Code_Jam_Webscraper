#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>

using namespace std;

int getCount(string * dictionary, int dicLength, string sample, int wordLength)
{
	int result = 0;
	string * partition = new string[wordLength];
	int start = 0;
	for (int i = 0; i < wordLength; i++) {
		if (sample[start] == '(') {
			int end = sample.find(')', start);
			partition[i] = sample.substr(start + 1, end - start -1);
			start = end + 1;
		}
		else {
			partition[i] = sample[start];
			start++;
		}
	}

	for (int i = 0; i < dicLength; i++) {
		string test = dictionary[i];
		int j;
		for (j = 0; j < wordLength; j++) {
			if (partition[j].find(test[j]) == string::npos)
				break;
		}
		if (j == wordLength)
			result++;
	}

	delete [] partition;
	return result;
}


int main()
{
	ifstream in;
	in.open("A-large.in");
    ofstream out;
	out.open("result.txt");
    
	string temp;
	getline(in, temp);
    
	int start = temp.find(" ", 0);
	const int wordLength = atoi(temp.substr(0, start).c_str());

	start++;
	int end = temp.find(" ", start);
	const int dicLength = atoi(temp.substr(start, end - start).c_str());

	start = end + 1;
	const int cases = atoi(temp.substr(start).c_str());

	string * dictionary = new string[dicLength];
	for (int i = 0; i < dicLength; i++) 
		getline(in, dictionary[i]);

	for (int count = 0; count < cases; count++) {
		string sample;
		getline(in, sample);
		int numPossible = getCount(dictionary, dicLength, sample, wordLength);
		out << "Case #" << count + 1 << ": " << numPossible << endl;
	}

	delete [] dictionary;
	in.close();
	out.close();
	return 0;
}