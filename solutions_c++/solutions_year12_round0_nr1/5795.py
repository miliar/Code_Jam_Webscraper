#include <iostream>
#include <vector>;
#include <fstream>;
#include <string>;
using namespace std;

struct Character
{
	char normal;
	char google;
};

char getChar(char c, vector<Character> language)
{
	for(int i=0; i<language.size(); i++)
	{
		if (language[i].google == c)
			return language[i].normal;
	}
	return '!';
}

void main()
{
	ifstream inFile;
	ofstream outFile;
	inFile.open("A-small-attempt0.in");
	//inFile.open("test.in");
	//inFile.open("A-large-practice.in");
	outFile.open("output.txt");

	vector <Character> language;
	Character character;

	character.normal = 'a';
	character.google = 'y';
	language.push_back(character);
	character.normal = 'b';
	character.google = 'n';
	language.push_back(character);
	character.normal = 'c';
	character.google = 'f';
	language.push_back(character);
	character.normal = 'd';
	character.google = 'i';
	language.push_back(character);
	character.normal = 'e';
	character.google = 'c';
	language.push_back(character);
	character.normal = 'f';
	character.google = 'w';
	language.push_back(character);
	character.normal = 'g';
	character.google = 'l';
	language.push_back(character);
	character.normal = 'h';
	character.google = 'b';
	language.push_back(character);
	character.normal = 'i';
	character.google = 'k';
	language.push_back(character);
	character.normal = 'j';
	character.google = 'u';
	language.push_back(character);
	character.normal = 'k';
	character.google = 'o';
	language.push_back(character);
	character.normal = 'l';
	character.google = 'm';
	language.push_back(character);
	character.normal = 'm';
	character.google = 'x';
	language.push_back(character);
	character.normal = 'n';
	character.google = 's';
	language.push_back(character);
	character.normal = 'o';
	character.google = 'e';
	language.push_back(character);
	character.normal = 'p';
	character.google = 'v';
	language.push_back(character);
	character.normal = 'q';
	character.google = 'z';
	language.push_back(character);
	character.normal = 'r';
	character.google = 'p';
	language.push_back(character);
	character.normal = 's';
	character.google = 'd';
	language.push_back(character);
	character.normal = 't';
	character.google = 'r';
	language.push_back(character);
	character.normal = 'u';
	character.google = 'j';
	language.push_back(character);
	character.normal = 'v';
	character.google = 'g';
	language.push_back(character);
	character.normal = 'w';
	character.google = 't';
	language.push_back(character);
	character.normal = 'x';
	character.google = 'h';
	language.push_back(character);
	character.normal = 'y';
	character.google = 'a';
	language.push_back(character);
	character.normal = 'z';
	character.google = 'q';
	language.push_back(character);

	int totalNumber = 0;
	inFile >> totalNumber;
	int counter = 0;

	string word;
	getline(inFile,word);
	while(counter < totalNumber)
	{
		outFile << "Case #";
		outFile << counter+1;
		outFile << ": ";

		vector<string> words;
		string line;
		getline(inFile,line);

		while(line.find_first_of(' ') < line.size())
		{
			string word = line.substr(0,line.find_first_of(' '));
			line.erase(0,line.find_first_of(' ')+1);
			words.push_back(word);
		}
		words.push_back(line);

		for(int i=0; i<words.size(); i++)
		{
			for(int j=0; j<words[i].size(); j++)
			{
				char c = getChar(words[i][j],language);
				outFile << c;
			}
			outFile << " ";
		}
		outFile << "\n";

		counter ++;
	}
}