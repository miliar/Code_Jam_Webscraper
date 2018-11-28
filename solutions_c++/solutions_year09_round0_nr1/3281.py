#include <fstream>
#include <conio.h>
#include <list>
#include <string>

#define BUFFER_LINE 100000

using namespace std;

list <list<char>> parsePattern(char* line, int token)
{
	list <list<char>> pattern;

	char* head = line;
	char* end = head + strlen(line);

	for(int itoken = 1; itoken <= token; itoken++)
	{
		list <char> token;
		if(*head == '(')
		{
			head++;
			while(*head != ')')
			{
				token.push_back(*head);
				head++;
			}
			head++;
		}
		else
		{
			token.push_back(*head);
			head++;
		}
		pattern.push_back(token);
	}

	return pattern;
}

int findPattern(list <list<char>> pattern, list <char*> words)
{
	int count = 0;
	
	list <char*>::iterator word;
	for ( word = words.begin( ); word != words.end( ); word++ )
	{
		char* key = *word;
		list <list<char>>::iterator iter;
		bool match = true;
		for ( iter = pattern.begin( ); match && iter != pattern.end( ); iter++ )
		{
			char k = *key++;	
			list <char> temp = *iter;
			list <char>::iterator iter2;
			for ( iter2 = temp.begin( ); iter2 != temp.end( ); iter2++ )
			{
				if(k == *iter2)
				{
					match = true;
					break;
				}
				else
				{
					match = false;
				}
			}
		}

		if(match) count++;
	}

	return count;
}

long main()
{
	
	ifstream inputFile("Input.txt");
	char inbuf[BUFFER_LINE];
	if(inputFile.good())
	{
		ofstream outputFile("Output.txt", ios::out);
		inputFile.getline(inbuf,BUFFER_LINE);
		
		long length, words, cases;
		sscanf(inbuf, "%d %d %d", &length, &words, &cases);
		
		list <char*> allwords;
		for(int iwords = 1; iwords <= words; iwords++)
		{
			inputFile.getline(inbuf,BUFFER_LINE);
			char* temp = new char[BUFFER_LINE];
			sprintf(temp, "%s", inbuf);
			allwords.push_back(temp);
		}

		for(int icases = 1; icases <= cases; icases++)
		{
			inputFile.getline(inbuf,BUFFER_LINE);
			list <list<char>> pattern = parsePattern(inbuf, length);
			//printf("Case #%d: %d\n", icases, findPattern(pattern, allwords));
			outputFile << "Case #" << icases << ": " << findPattern(pattern, allwords) << "\n";
		}

		inputFile.close();
		outputFile.close();
	}
	else
	{
		printf("Error : Can not open input file.\n");
	}

	printf("Press any key to continue...");
	getch();
	return 0;
}

		/*list <char*>::iterator iter;
		printf("Words : ");
		for ( iter = allwords.begin( ); iter != allwords.end( ); iter++ )
			printf("%s ", *iter);
		printf("\n");*/