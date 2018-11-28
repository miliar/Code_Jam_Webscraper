#include <iostream>
#include <fstream>
#include <string>
using namespace std;

#define INPUT_FILE "./input.txt"
#define OUTPUT_FILE "./output.txt"

#define L 15
#define D 5000
#define N 500

typedef struct {
	string str;
	bool check;
} Dict;

int main()
{
	int iTestCase=0;
	int iWord=0;
	int iCharAtWord=0;
    
	string line;
	ifstream inputFile (INPUT_FILE);
	ofstream outputFile (OUTPUT_FILE);

	if (inputFile.is_open())
	{
		inputFile >> iCharAtWord;
		inputFile >> iWord;
		inputFile >> iTestCase;
		getline (inputFile, line);

		string sDictionary[D]; // словарь
		// read words
		for (int i = 0; i < iWord; i++)
		{
			getline (inputFile, line);
			sDictionary[i] = line;
		}
		
		for (int iCase=0; iCase<iTestCase; iCase++)
		{
			Dict sTestDictionary[L];

			//int iNumWords = 0;		// kol-vo slov dlja testa
			int iNumTestWord = 0;	// kol-vo neizvesnux slov
			bool next = false;

			getline (inputFile, line);
			if (line == "")
			{
				outputFile << "Case #" << iCase+1 << ": " << 0 << "\n";
				continue;
			}

			line+='|';
			size_t foundBegin = line.find_first_of("(");
			size_t FoundEnd = line.find_first_of(")");
			int iFoundEndPrev = 0;	

			if (foundBegin == string::npos)
			{
				for (int t = 0; t < line.length()-1; t++)
				{
					sTestDictionary[iNumTestWord].str = line.at(t);//substr( FoundEnd,foundBegin );
					sTestDictionary[iNumTestWord].check=false;
					iNumTestWord++;
				}
			}
			else
            {
			    if (foundBegin > 0)
			    {
				    for (int t = 0; t < foundBegin; t++)
				    {
					    sTestDictionary[iNumTestWord].str = line.at(t);//substr( FoundEnd,foundBegin );
					    sTestDictionary[iNumTestWord].check=false;
					    iNumTestWord++;
				    }
			    }

			    while (1)
			    {
				    if (FoundEnd == string::npos)
				    {
					    foundBegin = line.find_last_of(")");
					    FoundEnd = line.find_last_of("|");
					    if ((foundBegin+1) ==FoundEnd )
					    {
						    break;
					    }
					    for (int t = foundBegin+1; t < FoundEnd; t++)
					    {
						    sTestDictionary[iNumTestWord].str = line.at(t);//substr( FoundEnd,foundBegin );
						    sTestDictionary[iNumTestWord].check=false;
						    iNumTestWord++;
					    }
					    break;
				    }
				    else
				    {
					    if (iFoundEndPrev+1 != foundBegin && iFoundEndPrev != 0)
					    {
						    for (int t = iFoundEndPrev+1; t < foundBegin; t++)
						    {
							    sTestDictionary[iNumTestWord].str = line.at(t);//substr( FoundEnd,foundBegin );
							    sTestDictionary[iNumTestWord].check=false;
							    iNumTestWord++;
						    } 
                            //iNumTestWord--;
                            foundBegin = line.find_first_of("(", iFoundEndPrev-1);
			                
			                FoundEnd = line.find_first_of(")", foundBegin); 
                            iFoundEndPrev=0;
                            continue;;
					    }
                        else
                        {
					        sTestDictionary[iNumTestWord].str = line.substr( foundBegin, FoundEnd-foundBegin+1 );
					        sTestDictionary[iNumTestWord].check=true;
                        }
				    }
				    foundBegin = line.find_first_of("(", FoundEnd);
				    iFoundEndPrev=FoundEnd;
				    FoundEnd = line.find_first_of(")", FoundEnd+1);
				    iNumTestWord++;
			    }// while (1)
            }
				
			unsigned int iRaz = 0;
			for (int iWordsToCheck = 0; iWordsToCheck < iWord; iWordsToCheck++)
			{
				bool plus = true;
				for (int i=0; i<sDictionary[iWordsToCheck].length() && plus; i++)
				{
					if (sTestDictionary[i].check)
					{
						if (sTestDictionary[i].str.find(sDictionary[iWordsToCheck].at(i)) == string::npos)
							plus = false;
					}
					else
					{
						if (sDictionary[iWordsToCheck].at(i) != sTestDictionary[i].str.at(0))
							plus = false;
					}
					
				}
				if (plus)
					iRaz++;
				
			}
			outputFile << "Case #" << iCase+1 << ": " << iRaz << "\n";
		}
	}
	else 
		cout << "Unable to open file"; 

	//inputFile.close();
	
	return 0;
}