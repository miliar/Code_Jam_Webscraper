#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
using namespace std;

#define WIN32_LEAN_AND_MEAN
#undef UNICODE
#include <windows.h>

string desktopDir();
size_t listFiles(const string &dir, const string &prefix, const string &sufix, list<string> *files);

int main(int argc, char **args)
{
    string dir = "./";
    list<string> files;
    if (listFiles(dir, "A-", ".in", &files) == 0)
        return -2;

    for (list<string>::iterator fileIte = files.begin(); fileIte != files.end(); ++fileIte)
    {
    	if (*fileIte == "A-sample.in")
    		continue;

        ifstream input((dir + *fileIte).c_str());
        ofstream output((dir + fileIte->substr(0, fileIte->find('.')) + ".out").c_str());

        int numCases;
        input >> numCases;
        for (int caseNum = 0; caseNum < numCases; ++ caseNum)
        {
        	char gameBoard[4][4];

        	for (int i = 0; i < 4; i++) {
        		for (int j = 0; j < 4; j++) {
        			input >> gameBoard[i][j];
        		}
        	}

        	// Check for vertical/horizontal lines
        	char horizontalChar = 'T';
        	char verticalChar = 'T';
        	char descendingChar = 'T';
        	char ascendingChar = 'T';
        	bool emptyChar = false;
        	for (int i = 0; i < 4; i++) {
        		horizontalChar = 'T';
        		verticalChar = 'T';

        		for (int j = 0; j < 4; j++) {
        			if (gameBoard[i][j] == '.')
        				emptyChar = true;

        			if (horizontalChar == 'T')
        				horizontalChar = gameBoard[i][j];
        			else if (gameBoard[i][j] != 'T' && horizontalChar != gameBoard[i][j])
        				horizontalChar = '\0';

        			if (verticalChar == 'T')
        				verticalChar = gameBoard[j][i];
					else if (gameBoard[j][i] != 'T' && verticalChar != gameBoard[j][i])
						verticalChar = '\0';
        		}

        		if (horizontalChar == 'X' || horizontalChar == 'O' || verticalChar == 'X' || verticalChar == 'O') {
        			descendingChar = ascendingChar = '\0';
        			break;
        		}

        		if (descendingChar == 'T')
        			descendingChar = gameBoard[i][i];
    			else if (gameBoard[i][i] != 'T' && descendingChar != gameBoard[i][i])
    				descendingChar = '\0';

        		if (ascendingChar == 'T')
        			ascendingChar = gameBoard[3 - i][i];
				else if (gameBoard[3 - i][i] != 'T' && ascendingChar != gameBoard[3 - i][i])
					ascendingChar = '\0';
			}

            string result;
            if (horizontalChar == 'X' || verticalChar == 'X' || descendingChar == 'X' || ascendingChar == 'X')
            	result = "X won";
            else if (horizontalChar == 'O' || verticalChar == 'O' || descendingChar == 'O' || ascendingChar == 'O')
				result = "O won";
            else if (emptyChar)
            	result = "Game has not completed";
            else
            	result = "Draw";

            stringstream caseResult;
            caseResult << "Case #" << caseNum + 1 << ": " << result;
            output << caseResult.str() << endl;
            cout << caseResult.str() << endl;
        }
    }

    return 0;
}

size_t listFiles(const string &dir, const string &prefix, const string &sufix, list<string> *files)
{
    files->clear();

    string fileMask = dir + prefix + "*" + sufix;
    WIN32_FIND_DATA info;
    HANDLE hFind = FindFirstFile(fileMask.c_str(), &info);
    if (hFind != INVALID_HANDLE_VALUE)
    {
        do
        {
            if (strlen(info.cFileName) > 0)
                files->push_back(info.cFileName);
        } while (FindNextFile(hFind, &info));

        FindClose(hFind);
    }

    return files->size();
}
