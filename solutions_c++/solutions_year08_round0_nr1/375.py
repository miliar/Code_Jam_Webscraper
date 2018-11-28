
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

        int nEngineCount = 0, nQueryCount = 0;
        vector<string> engineVector;
        vector<string> queryVector;
        map<string, int> queryMap;

        //string strTemp;
        char charbuf[110];
        if ( bFromFile )
        {
            fsInput >> nEngineCount;
            fsInput.getline(charbuf, 10);//skip the first line
            for ( int i = 0; i < nEngineCount; i++ )
            {
                fsInput.getline(charbuf, 110);
                engineVector.push_back( charbuf );
            }
            fsInput >> nQueryCount;
            fsInput.getline(charbuf, 10);//skip the first line
            for ( int i = 0; i < nQueryCount; i++ )
            {
                fsInput.getline(charbuf, 110);
                queryVector.push_back( charbuf );
            }
        }
        else
        {
            //cout << "Input Engine Count:" << endl;
            cin >> nEngineCount;
            cin.getline(charbuf, 10);//skip the first line
            for ( int i = 0; i < nEngineCount; i++ )
            {
                cin.getline(charbuf, 110);
                engineVector.push_back( charbuf );
            }
            cin >> nQueryCount;
            cin.getline(charbuf, 10);//skip the first line
            for ( int i = 0; i < nQueryCount; i++ )
            {
                cin.getline(charbuf, 110);
                queryVector.push_back( charbuf );
            }
        }

        int nSwitch = 0;
        for ( int i = 0; i < nQueryCount; i ++ )
        {
            queryMap[queryVector[i]] = 1;
            if ( (int)queryMap.size() == nEngineCount )
            {
                nSwitch++;
                queryMap.clear();
                queryMap[queryVector[i]] = 1;
            }
        }

        stringstream sMsg;
        sMsg << "Case #" << nIndex << ": " << nSwitch;
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