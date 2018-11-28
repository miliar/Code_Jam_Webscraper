#include<iostream>
#include<string>
#include<set>
#include<sstream>
#include<limits>
#include<stdlib.h>
#include<algorithm>

//#define DEBUGNAP

#define MAXBASES 9

using namespace std;

typedef unsigned long ulong;

string numstr;
int digitcount[10];

int main(int argc, char *argv[])
{
    int T;
    cin>>T;
    //cin.ignore(numeric_limits<streamsize>::max(), '\n'); //cin.get();
    for(int mycase=1; mycase<=T; mycase++)
    {
        cin>>numstr;
        
        if(!next_permutation(numstr.begin(), numstr.end()))
        {
            // Shift the zeroes at the begining inwards & insert a zero at the left-most available position...
            int lastZero = numstr.find_last_of('0');
            if(lastZero != string::npos)
            {
                //cout<<"Zeores from 0 to "<<lastZero<<endl;
                string zeroes = numstr.substr(0, lastZero+1);
                numstr = numstr.substr(lastZero+1);
                numstr.insert(1,zeroes);
            }
            numstr.insert(1, "0");
        }

        cout<<"Case #"<<mycase<<": "<<numstr<<endl;
    }

#ifdef DEBUGNAP
system("pause");
#endif
    return 0;
}