#include <stdlib.h>
#include <time.h>
#include <fstream>
#include <iostream>

using namespace std;

int main(int argc, char* argv[])
{
    fstream fIn, fOut;
    fIn.open("B-large.in", fstream::in);
    fOut.open("Output.txt", fstream::out);

    int caseNum = 0;
    fIn >> caseNum;
    
    for(int cn = 0; cn < caseNum; cn++)
    {
        int n,k,b,t;
        fIn >> n >> k >> b >> t;

        int able = 0;
        int swap = 0;
        int chick[50][3];
        for(int i = 0; i < n; i++)
        {
            fIn >> chick[i][0];
        }
        for(int i = 0; i < n; i++)
        {
            fIn >> chick[i][1];
            if(chick[i][1] * t + chick[i][0] >= b)
            {
                chick[i][2] = 1;
                able++;
            }
            else
                chick[i][2] = 0;
        }
/*
        for(int i = 0; i < n; i++)
        {
            cout << chick[i][0] << " " << chick[i][1] << " " << chick[i][2] << endl;
        }
*/
        if(able >= k)
        {
            int unable = 0;
            int pass = 0;
            
            int i = n - 1;
            while(pass < k)
            {
                if(chick[i][2] == 1)
                {
                    swap += unable;
                    pass++;
                }
                else
                {
                    unable++;
                }
                i--;
            }
        }
        else
        {
            fOut << "Case #" << cn + 1 << ": IMPOSSIBLE" << endl;
            continue;
        }

        fOut << "Case #" << cn + 1 << ": " << swap << endl;

    }

    fIn.close();
    fOut.close();

    return 0;
}
