#include<fstream>
#include<iostream>
#include<string>
#include<vector>

using namespace std;

struct Cell
{
    int altitude;
    char basin;
};

class WaterSheds
{
    struct Cell cell[100][100];
    int noTestCases;
    int matchedWords;
    int height;
    int width;

    public:

    bool isValid( int i, int j )
    {
        if( i >= height || i < 0 || j >= width || j < 0 )
            return false;
        return true;
    }

    void calculateBasin()
    {
        int flag, i, j, k, min, posI, posJ, flag2 = 0, I, J, positionQueue[10000], queueLength, sinkLocation[10000], totalSinks = 0, currentSink, currentSinkIndex;
        //char currentBasin = 'a';
        //cell[0][0].basin = currentBasin;
        int di[]={-1, 0, 0, 1};
        int dj[]={0, -1, 1, 0};
        for( I = 0; I < height; ++I )
        {
            for( J = 0; J < width; ++J )
            {
                min = cell[I][J].altitude;
                flag = 1;
                i = I;
                j = J;
                queueLength = 1;
                positionQueue[0] = I * width + J;
                while(flag)
                {
                    flag = 0;
                    for( k = 0; k < 4; ++k )
                    {
                        if( min > cell[ i + di[k] ][ j + dj[k] ].altitude && isValid( i + di[k], j + dj[k] ) )
                        {
                            min = cell[ i + di[k] ][ j + dj[k] ].altitude;
                            posI = i + di[k];
                            posJ = j + dj[k];
                            flag = 1;
                        }
                    }
                    if(flag)
                    {
                        i = posI;
                        j = posJ;
                        positionQueue[queueLength++] = posI * width + posJ;
                    }
                 }
                if( min == cell[I][J].altitude )
                {
                        posI = I;
                        posJ = J;
                }
                currentSink = ( posI * width ) + posJ;
                for( k = 0; k < totalSinks; ++k )
                        if( sinkLocation[k] == currentSink )
                        {
                            currentSinkIndex = k;
                            break;
                        }
                if( k == totalSinks )
                {
                    currentSinkIndex = totalSinks;
                    sinkLocation[totalSinks++] = currentSink;
                }
                for( k = queueLength - 1; k >= 0; --k )
                {
                    posI = positionQueue[k] / width;
                    posJ = positionQueue[k] % width;
                    cell[posI][posJ].basin = currentSinkIndex + 'a';
                }
            }
        }
    }

    WaterSheds()
    {
        int i, j, k;
        ifstream inputFile;
        ofstream outputFile;
        inputFile.open ( "B-large.in" );
        outputFile.open ( "B-large.out" );
        inputFile>>noTestCases;
        for( i = 0 ;i < noTestCases; ++i )
        {
            inputFile>>height>>width;
            for( j = 0; j < height; ++j )
                for( k = 0; k < width; ++k )
                {
                    inputFile>>cell[j][k].altitude;
                    cell[j][k].basin = '0';
                }
            calculateBasin();
            cout<<"Case #"<<i+1<<":"<<endl;
            outputFile<<"Case #"<<i+1<<":"<<endl;
            for( j = 0; j < height; ++j )
            {
                for( k = 0; k < width; ++k )
                {
                    outputFile<<cell[j][k].basin<<" ";
                    cout<<cell[j][k].basin<<" ";
                }
                outputFile<<endl;
                cout<<endl;
            }
        }
         inputFile.close();
         outputFile.close();
    }
};

int main()
{
    WaterSheds waterSheds;
}
