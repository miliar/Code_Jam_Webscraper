#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
	ifstream infile("input.in");
	ofstream outfile("output.txt");
	vector<string> googlephrases;
	int N = 0;
	infile>>N;
	for(int i = 0; i < N+1; i++)
	{
		string x;
		getline(infile, x);
		googlephrases.push_back(x);
	}
	for(int i = 1; i < N+1; i++)
	{
		string unTranslated = googlephrases[i];
		string translated = unTranslated;
		for(int j = 0; j < unTranslated.size(); j++)
		{
			switch(unTranslated[j])
			{
			case 'a' :
				{
					translated[j] = 'y';
					break;
				}
			case 'b':
				{
					translated[j] = 'h';
					break;
				}
			case 'c':
				{
					translated[j] = 'e';
					break;
				}
			case 'd':
				{
					translated[j] = 's';
					break;
				}
			case 'e':
				{
					translated[j] = 'o';
					break;
				}
			case 'f':
				{
					translated[j] = 'c';
					break;
				}
			case 'g':
				{
					translated[j] = 'v';
					break;
				}
			case 'h':
				{
					translated[j] = 'x';
					break;
				}
			case 'i':
				{
					translated[j] = 'd';
					break;
				}
			case 'j':
				{
					translated[j] = 'u';
					break;
				}
			case 'k':
				{
					translated[j] = 'i';
					break;
				}
			case 'l' :
				{
					translated[j] = 'g';
					break;
				}
			case 'm':
				{
					translated[j] = 'l';
					break;
				}
			case 'n':
				{
					translated[j] = 'b';
					break;
				}
			case 'o':
				{
					translated[j] = 'k';
					break;
				}
			case 'p':
				{
					translated[j] = 'r';
					break;
				}
			case 'q':
				{
					translated[j] = 'z';
					break;
				}
			case 'r':
				{
					translated[j] = 't';
					break;
				}
			case 's':
				{
					translated[j] = 'n';
					break;
				}
			case 't':
				{
					translated[j] = 'w';
					break;
				}
			case 'u':
				{
					translated[j] = 'j';
					break;
				}
			case 'v':
				{
					translated[j] = 'p';
					break;
				}
			case 'w':
				{
					translated[j] = 'f';
					break;
				}
			case 'x':
				{
					translated[j] = 'm';
					break;
				}
			case 'y':
				{
					translated[j] = 'a';
					break;
				}
			case 'z':
				{
					translated[j] = 'q';
					break;
				}
            case ' ':
				{
				    translated[j] = ' ';
				    break;
				}
			default:
				{
					cout<<"ERROR SMW";
				}
			}
		}
		googlephrases[i] = translated;
	}
	for(int i = 1; i < googlephrases.size(); i++)
	{
		cout<<"Case #"<<i<<": "<<googlephrases[i]<<endl;
		outfile<<"Case #"<<i<<": "<<googlephrases[i]<<endl;
	}
	return 0;
}


