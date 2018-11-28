
#include <vector>

#include <fstream>
#include <iostream>

using std::cin;
using std::cout;
using std::endl;

int main( int argc, char **argv )
{
    std::ifstream input(argv[1]);

    int cases = 0;

    input >> cases;

    for(int caseNum=0; caseNum<cases; ++caseNum)
    {
        int recycledNums = 0;
        int high = 0;
        int low = 0;

        input >> low;
        input >> high;

        cout << "Case #" << caseNum+1 << ": ";
        for( int a=low; a<=high-1; ++a )
        {
            for( int b=a+1; b<=high; ++b )
            {
                if( a == b )
                {
                    continue;
                }

                static const int bytes = 1024;
                char aBuf[bytes];
                char bBuf[bytes];

                snprintf( aBuf, bytes, "%d", a);
                snprintf( bBuf, bytes, "%d", b);

                if( strlen(aBuf) != strlen(bBuf) )
                {
                    continue;
                }
                else
                {
                    int len = strlen(aBuf);
                    char first = aBuf[0];
                    int matchPos = -1;

                    for(int bPos=0; bPos<len; ++bPos)
                    {
                        char bChar = bBuf[bPos];

                        if( first != bChar )
                        {
                            continue;
                        }

                        bool match = true;

                        for(int aPos=1; (aPos<len) && match; ++aPos)
                        {
                            int realBPos = (bPos + aPos) % len;

                            //cout << "  Checking char " << aBuf[aPos] << " " << bBuf[realBPos] << endl;

                            if( aBuf[aPos] != bBuf[realBPos] )
                            {
                                //cout << "    Fail\n";
                                match = false;
                                break;
                            }
                        }

                        if( match )
                        {
                            //cout << "Match! " << a << " " << b << endl;
                            recycledNums++;
                            break;
                        }
                    }
                }
            }
        }

        cout << recycledNums << endl;
    }


    return 0;
}

