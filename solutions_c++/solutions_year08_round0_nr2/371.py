
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <math.h>
#include <vector>
#include <map>

using namespace std;

int stringTimeToMinutes(const string & time)
{
    int nValue = 0;
    string hour = time.substr(0, 2);
    string min = time.substr(3, 2);
    int nHour = atoi(hour.c_str());
    int nMin = atoi(min.c_str());
    nValue = nHour * 60 + nMin;
    return nValue;
}

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

        int nTurnaroundTime = 0;
        int nATripCount = 0, nBTripCount = 0;

        //string strTemp;
        char charbuf[13];
        stringstream streamTemp;
        string strStart;
        string strEnd;

        typedef multimap<int, int> TRIP_MAP;
        TRIP_MAP AMapSortByStart, AMapSortByEnd, BMapSortByStart, BMapSortByEnd;
        if ( bFromFile )
        {
            fsInput >> nTurnaroundTime;
            fsInput >> nATripCount >> nBTripCount;
            fsInput.getline(charbuf, 10);//skip the first line
            //Read A Trips
            for ( int i = 0; i < nATripCount; i++ )
            {
                fsInput.getline(charbuf, 13);
                streamTemp.clear();
                streamTemp << charbuf;
                streamTemp.flush();
                streamTemp >> strStart >> strEnd;
                int nStart = stringTimeToMinutes(strStart);
                int nEnd = stringTimeToMinutes(strEnd);
                AMapSortByStart.insert(make_pair(nStart, nEnd));
                AMapSortByEnd.insert(make_pair(nEnd, nStart));
            }
            //Read B Trips
            for ( int i = 0; i < nBTripCount; i++ )
            {
                fsInput.getline(charbuf, 13);
                streamTemp.clear();
                streamTemp << charbuf;
                streamTemp.flush();
                streamTemp >> strStart >> strEnd;
                int nStart = stringTimeToMinutes(strStart);
                int nEnd = stringTimeToMinutes(strEnd);
                BMapSortByStart.insert(make_pair(nStart, nEnd));
                BMapSortByEnd.insert(make_pair(nEnd, nStart));
            }
        }
        else
        {
            cin >> nTurnaroundTime;
            cin >> nATripCount >> nBTripCount;
            cin.getline(charbuf, 10);//skip the first line
            //Read A Trips
            for ( int i = 0; i < nATripCount; i++ )
            {
                cin.getline(charbuf, 13);
                streamTemp.clear();
                streamTemp << charbuf;
                streamTemp.flush();
                streamTemp >> strStart >> strEnd;
                int nStart = stringTimeToMinutes(strStart);
                int nEnd = stringTimeToMinutes(strEnd);
                AMapSortByStart.insert(make_pair(nStart, nEnd));
                AMapSortByEnd.insert(make_pair(nEnd, nStart));
            }
            //Read B Trips
            for ( int i = 0; i < nBTripCount; i++ )
            {
                cin.getline(charbuf, 13);
                streamTemp.clear();
                streamTemp << charbuf;
                streamTemp.flush();
                streamTemp >> strStart >> strEnd;
                int nStart = stringTimeToMinutes(strStart);
                int nEnd = stringTimeToMinutes(strEnd);
                BMapSortByStart.insert(make_pair(nStart, nEnd));
                BMapSortByEnd.insert(make_pair(nEnd, nStart));

            }
        }

        int nLessCounter = 0;
        int nALines = 0, nBLines = 0;

        {
            TRIP_MAP::const_iterator AStartItor = AMapSortByStart.begin();
            TRIP_MAP::const_iterator BEndItor = BMapSortByEnd.begin();
            while( AStartItor != AMapSortByStart.end() &&
                BEndItor != BMapSortByEnd.end() )
            {
                int nCurAStart = AStartItor->first;
                int nCurBEnd = BEndItor->first;
                if (nCurAStart < nCurBEnd + nTurnaroundTime)
                    AStartItor++;
                else
                {
                    nLessCounter++;
                    AStartItor++;
                    BEndItor++;
                }
            }
        }
        nALines = nATripCount - nLessCounter;

        nLessCounter = 0;
        {
            TRIP_MAP::const_iterator BStartItor = BMapSortByStart.begin();
            TRIP_MAP::const_iterator AEndItor = AMapSortByEnd.begin();
            while( BStartItor != BMapSortByStart.end() &&
                AEndItor != AMapSortByEnd.end() )
            {
                int nCurBStart = BStartItor->first;
                int nCurAEnd = AEndItor->first;
                if (nCurBStart < nCurAEnd + nTurnaroundTime)
                    BStartItor++;
                else
                {
                    nLessCounter++;
                    BStartItor++;
                    AEndItor++;
                }
            }
        }
        nBLines = nBTripCount - nLessCounter;

        stringstream sMsg;
        sMsg << "Case #" << nIndex << ": " << nALines << ' ' << nBLines;
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