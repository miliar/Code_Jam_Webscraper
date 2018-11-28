
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <math.h>
#include <vector>
#include <map>

using namespace std;

int main( int argc, char *argv[]) 
{

    bool bFromFile = false;
    int nCount = 0;
    string strInputFile, strOutputFile;
    ifstream fsInput;
    ofstream fsOutput;
    int nIndex = 0;

    if ( argc == 1 )
    {
        cout << "Input count:";
        cin >> nCount;
        bFromFile = false;
    }
    else if ( argc == 3)
    {
        strInputFile = argv[1];
        strOutputFile = argv[2];
        cout << "Input file: " << strInputFile << "  Out file:" << strOutputFile << endl;
        bFromFile = true;
        fsInput.open(strInputFile.c_str());
        fsInput >> nCount;
        fsOutput.open(strOutputFile.c_str());
    }
    else
    {
        cout << "Wrong input paramters." << endl;
        return 0;
    }

    while( nCount-- > 0 )
    {
        nIndex++;


        long long maxNum = 0, keysNum = 0, lettersNum = 0;
        typedef vector <long long> LONG_VECTOR;
        LONG_VECTOR freqVector;

        if ( bFromFile )
        {
            fsInput >> maxNum >> keysNum >> lettersNum;
            for ( long long i = 0; i < lettersNum; i++ )
            {
                long long lTemp = 0;
                fsInput >> lTemp;
                freqVector.push_back( lTemp );
            }
        }
        else
        {
            cin >> maxNum >> keysNum >> lettersNum;
            for ( long long i = 0; i < lettersNum; i++ )
            {
                long long lTemp = 0;
                cin >> lTemp;
                freqVector.push_back( lTemp );
            }
        }

        sort(freqVector.begin(), freqVector.end());
        reverse(freqVector.begin(), freqVector.end());

        typedef vector<LONG_VECTOR> KEY_ARRANGE_VECTOR;
        KEY_ARRANGE_VECTOR keyArrangeVector;
        for ( long long i = 0; i < keysNum; i++ )
        {
            LONG_VECTOR tempVector;
            keyArrangeVector.push_back(tempVector);
        }

        for ( long long i = 0; i < lettersNum; i++)
        {
            long long keyIndex = i % keysNum;
            keyArrangeVector[keyIndex].push_back( freqVector[i] );
        }

        bool bPossible = true;
        for ( long long i = 0; i < keysNum; i++)
        {
            if ((long long)keyArrangeVector[i].size() > maxNum )
            {
                bPossible = false;
                break;
            }
        }

        long long pressNum = 0;
        if (bPossible)
        {
            for ( long long i = 0; i < keysNum; i++ )
            {
                long long tempPressNum = 0;
                for ( long long j = 0; j < (long long)keyArrangeVector[i].size(); j++)
                {
                    tempPressNum += (j + 1) * keyArrangeVector[i][j];
                }
                pressNum += tempPressNum;
            }
        }
        stringstream sMsg;
        sMsg << "Case #" << nIndex << ": ";
        if (bPossible)
            sMsg << pressNum;
        else
            sMsg << "IMPOSSIBLE";
        sMsg.flush();
        cout << sMsg.str() << endl;
    
        if (bFromFile)
            fsOutput << sMsg.str() << endl;
    }

    if (bFromFile)
    {
        fsInput.close();
        fsOutput.flush();
        fsOutput.close();
    }
    cout << "End" << endl;
}