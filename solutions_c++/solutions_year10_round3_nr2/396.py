#include <math.h>
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
        int l,p,c;
        fIn >> l >> p >> c;
        //cout << l << p << c << endl;
        int i = 1;
        while(true)
        {
            //cout << i << endl;
            if((l * pow(1.0 * c, i)) >= p)
            {
                break;
            }
            i++;
        }
        cout << i << endl;

        int ret = 0;
        while(true)
        {
            if(pow(2.0 , ret) >= i)
                break;
            ret++;
        }

        fOut << "Case #" << cn + 1 << ": " << ret << endl;

    }

    fIn.close();
    fOut.close();

    return 0;
}
