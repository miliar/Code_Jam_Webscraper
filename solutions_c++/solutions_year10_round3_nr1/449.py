#include <stdlib.h>
#include <time.h>
#include <fstream>
#include <iostream>

using namespace std;

int main(int argc, char* argv[])
{
    fstream fIn, fOut;
    fIn.open("A-large.in", fstream::in);
    fOut.open("Output.txt", fstream::out);

    int caseNum = 0;
    fIn >> caseNum;
    
    for(int cn = 0; cn < caseNum; cn++)
    {
        int n;
        fIn >> n;
        int wire[1000][2];
        int inter = 0;
        for(int i = 0; i < n; i++)
        {
            fIn >> wire[i][0] >> wire[i][1];
            for(int j = 0; j < i; j++)
            {
                if((wire[j][0] - wire[i][0]) * (wire[j][1] - wire[i][1]) < 0)
                    inter++;
            }
        }
        fOut << "Case #" << cn + 1 << ": " << inter << endl;

    }

    fIn.close();
    fOut.close();

    return 0;
}
