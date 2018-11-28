#include<fstream>
#include<string>

using namespace std;

int howManyExact(string* strings, string testString, int numOfStrings, int stringLength) {
	int numOfExact = 0;

	for(int i = 0; i < numOfStrings; i++) {
		int dataIndex = 0;
		
		bool inParen = false;

		for(int j = 0; j < testString.length(); j++) {
			if(testString[j] == '(') {
				inParen = true;
			} else if(testString[j] == ')') {
				inParen = false;
			} else if(testString[j] == strings[i][dataIndex]) {
				if(dataIndex == stringLength - 1)
					numOfExact++;
				dataIndex++;
				if(inParen) 
					while(1) {
						if(testString[j + 1] == ')' || testString[j + 1] == NULL) break;
						j++;
					}
			} else {
				if(!inParen) break;
			}
		}
	}

	return numOfExact;
}

int main() {

	ifstream input;
	input.open("A-small-attempt2.in");

	int stringLength;
	input >> stringLength;

	int numOfStrings;
	input >> numOfStrings;

	int numOfTests;
	input >> numOfTests;

	string *strings = new string[numOfStrings];
	for(int i = 0; i < numOfStrings; i++) {
		input >> strings[i];
	}

	ofstream output;
	output.open("A-small-attempt2.out");
	for(int i = 0; i < numOfTests; i++) {
		string testString;
		input >> testString;

		output << "Case #" << i + 1 << ": " << howManyExact(strings, testString, numOfStrings, stringLength) << endl;
	}
	
	input.close();
	output.close();
	return 0;
}