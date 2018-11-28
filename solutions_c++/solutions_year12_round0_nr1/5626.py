#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;

string translate(string G);

int main()
{
	ifstream inFile;
	ofstream outFile;
	inFile.open("input.in", ios::in);
	outFile.open("output.out", ios::out);

	if (inFile.is_open())
	{
		int T;
		string G, S;

		getline(inFile, G);
		T = atoi(G.c_str());

		for (int i = 0; i < T; i++)
		{
			getline(inFile, G);
			S = translate(G);
			if (outFile.is_open())
			{
				outFile << "Case #" << i + 1 << ": " << S << endl;
			}
			else
			{
				cout << "Blad zapisu!" << endl;
				return -1;
			}
		}
		inFile.close();
		outFile.close();
	}
	else
	{
		cout << "Blad odczytu!" << endl;
		return -1;
	}
	return 0;
}

string translate(string G)
{
	char Googlerese[26] = {'y', 'n', 'f', 'i', 'c', 'w', 'l', 'b', 'k', 'u', 'o', 'm', 'x', 's', 'e', 'v', 'z', 'p', 'd', 'r', 'j', 'g', 't', 'h', 'a', 'q'};
	string S;

	for (unsigned int i = 0; i < G.size(); i++)
	{
		char Googlerese_character = G.at(i);
		if (Googlerese_character == ' ')
		{
			S += ' ';
		}
		else
		{
			char English_character = 97;
			while (1)
			{
				if (Googlerese_character == Googlerese[English_character - 97])
				{
					break;
				}
				English_character++;
			}
			S += English_character;
		}
	}
	return S;
}