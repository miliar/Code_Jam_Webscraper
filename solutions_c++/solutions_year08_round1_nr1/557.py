
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

        typedef vector<long long> INT_VECTOR;
        INT_VECTOR vector1;
        INT_VECTOR vector2;
        int nVecSize = 0, nTemp = 0;

        if ( bFromFile )
        {
            fsInput >> nVecSize;
            for ( int i = 0; i < nVecSize; i++ )
            {
                fsInput >> nTemp;
                vector1.push_back(nTemp);
            }
            for ( int i = 0; i < nVecSize; i++ )
            {
                fsInput >> nTemp;
                vector2.push_back(nTemp);
            }
        }
        else
        {
            cin >> nVecSize;
            for ( int i = 0; i < nVecSize; i++ )
            {
                cin >> nTemp;
                vector1.push_back(nTemp);
            }
            for ( int i = 0; i < nVecSize; i++ )
            {
                cin >> nTemp;
                vector2.push_back(nTemp);
            }
        }

        sort( vector1.begin(), vector1.end() );
        sort( vector2.begin(), vector2.end() );
        reverse( vector2.begin(), vector2.end() );
        
        long long nSum = 0;
        for ( int i = 0; i < nVecSize; i++ )
        {
            nSum += vector1[i] * vector2[i];
        }

        stringstream sMsg;
        sMsg << "Case #" << nIndex << ": " << nSum;
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