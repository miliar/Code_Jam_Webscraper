#include <iostream>
#include <fstream>
#include <string>
#include <limits.h>
using namespace std;

#define INPUT_FILE "./input.txt"
#define OUTPUT_FILE "./output.txt"

#define T 42

//struct d
//{
//    int digit;
//    unsigned int count;
//};

int main()
{
	int iTestCase=0;
    
	string line;
	ifstream inputFile (INPUT_FILE);
	ofstream outputFile (OUTPUT_FILE);

	if (inputFile.is_open())
	{
		inputFile >> iTestCase;
		getline (inputFile, line);

        for (int iCase = 0; iCase < iTestCase; iCase++)
        {     
            unsigned long digit = 0;
            inputFile >> digit;

            char dstr[1000000];
            _ultoa(digit, dstr, 10);
            size_t iStrlen = strlen(dstr);
            int chararray[10] = {0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0};
            for (unsigned int len = 0; len < iStrlen; len++)
            {
                char ch = dstr[len];
                int curD = atoi(&ch);
                chararray[curD]++;
            }

            for (int j = (digit+1); j < ULONG_MAX; j++)
            {
                _ultoa(j, dstr, 10);
                iStrlen = strlen(dstr); 
                int testchararray[10] = {0, 0, 0, 0, 0,
                                 0, 0, 0, 0, 0};
                for (unsigned int len = 0; len < iStrlen; len++)
                {
                    //int curD = atoi(&dstr[len]);
                    char ch = dstr[len];
                    int curD = atoi(&ch);
                    testchararray[curD]++;
                }

                if (/*testchararray[0] == chararray[0] &&*/
                    testchararray[1] == chararray[1] &&
                    testchararray[2] == chararray[2] &&
                    testchararray[3] == chararray[3] &&
                    testchararray[4] == chararray[4] &&
                    testchararray[5] == chararray[5] &&
                    testchararray[6] == chararray[6] &&
                    testchararray[7] == chararray[7] &&
                    testchararray[8] == chararray[8] &&
                    testchararray[9] == chararray[9])
                {
                    outputFile << "Case #" << (iCase+1) << ": " << dstr << "\n";
                    break;
                }
            }
        }
	}
	else 
		cout << "Unable to open file"; 

	return 0;
}