#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <list>
#include <sstream>

#include <algorithm>

using namespace std;

#define FORN(i,n) for((i)=0;(i)<(n);(i)++)

int main(int argc, char *argv[])
{

    ifstream inputFile(argv[1]);
    ofstream outputFile("output.txt");

    int noTests;

    inputFile>>noTests;

    int i;

    FORN(i, noTests)
    {
        int R,C,j,k;

        char tiles[55][55];

        inputFile>>R>>C;

        FORN(j,R)
        {
            FORN(k,C)
            {
                char temp;

                inputFile>>temp;
                tiles[j][k] = temp;
            }
        }

        bool possible = true;

        FORN(j,R)
        {
            if (!possible)
            {
                break;
            }
            FORN(k,C)
            {
                if (tiles[j][k] == '#')
                {
                    if (j==R-1)
                    {
                        possible = false;
                        break;
                    }

                    if (k==C-1)
                    {
                        possible = false;
                        break;
                    }

                    if ((tiles[j+1][k] == '#') && (tiles[j+1][k+1] == '#') && (tiles[j][k+1] == '#') )
                    {
                        tiles[j][k]='/';
                        tiles[j+1][k]='\\';
                        tiles[j+1][k+1] = '/';
                        tiles[j][k+1] = '\\';
                    } else {
                        possible = false;
                        break;
                    }

                }
            }
        }

        outputFile<<"Case #"<<i+1<<":"<<endl;

        if (possible)
        {
            FORN(j,R)
            {
                FORN(k,C)
                {
                    outputFile<<tiles[j][k];

                }
                outputFile<<endl;
            }
        }
            else {
            outputFile<<"Impossible"<<endl;
        }

    }


}
