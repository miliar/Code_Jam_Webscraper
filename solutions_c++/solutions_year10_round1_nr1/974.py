#include <iostream>
#define REP(i,a,b) for(int i=a; i<b; i++)
#define dREP(i,a,b) for(int i=a; i>=b; i--)
#include <fstream>

using namespace std;

int main()
{
    int T, N, K, sameArrH, sameArrV, rowAt;
    char tab[50][50], tmp, lastH, lastV, tmpRow[50];
    bool red, blue;

    fstream plikIn ("large.in", fstream::in | fstream::out);
    fstream plikOut ("large.out", fstream::in | fstream::out);

    plikIn >> T;

    REP(i,0,T)
    {
        red=false;
        blue=false;
        plikIn >> N >> K;
        //plikIn >> tmp;
        //lastH = tmp;
        REP(x,0,N)          /////////ZERO
        {
            REP(y,0,N)
            tab[x][y] = '.';
            tmpRow[x] = '.';
        }





        REP(x,0,N)          ///////////READN
        {
            REP(y,0,N)
            {
                plikIn >> tmp;
                tmpRow[y] = tmp;
            }

            rowAt = N-1;
            dREP(y,N-1,0)
            {
                if(tmpRow[y] != '.')
                {
                    tab[x][rowAt] = tmpRow[y];
                    --rowAt;
                }
            }

        }


        /*REP(x,0,N)          ////////////////////COUT
        {
            REP(y,0,N)
            cout << tab[x][y];
            cout << endl;
        }*/



        REP(x,0,N)          /////////COUNTN  ROWC&COLS
        {
            lastH = '.';
            lastV = '.';
            sameArrH = 0;
            sameArrV = 0;
            REP(y,0,N)
            {

                if(tab[x][y] != '.' && tab[x][y] == lastH)
                sameArrH++; else sameArrH = 0;
                lastH = tab[x][y];

                if(tab[y][x] != '.' && tab[y][x] == lastV)
                sameArrV++; else sameArrV = 0;
                lastV = tab[y][x];

                if(sameArrH == K-1) if(lastH == 'R') red = true; else if(lastH == 'B') blue = true;
                if(sameArrV == K-1) if(lastV == 'R') red = true; else if(lastV == 'B') blue = true;

                if(red && blue)goto RET;
            }
        }

        //cout << red << " " << blue << endl;





        REP(x,0,N-K+1)          /////////COUNTN  DIAGONALS
        {
            REP(y,0,N-K+1)
            {
                lastH = '.';
                lastV = '.';
                sameArrH = 0;
                sameArrV = 0;
                REP(z, 0, K)
                {
                    if(tab[x+z][y+z] != '.' && tab[x+z][y+z] == lastH)
                    sameArrH++; else sameArrH = 0;
                    lastH = tab[x+z][y+z];
                }
                REP(z, 0, K)
                {
                    if(tab[N-x-1-z][y+z] != '.' && tab[N-x-1-z][y+z] == lastV)
                    sameArrV++; else sameArrV = 0;
                    lastV = tab[N-x-1-z][y+z];
                }

                if(sameArrH == K-1) if(lastH == 'R') red = true; else if(lastH == 'B') blue = true;
                if(sameArrV == K-1) if(lastV == 'R') red = true; else if(lastV == 'B') blue = true;

                if(red && blue)goto RET;


            }
        }





        ////////// ANSWER
        RET:
        //cout << red << " " << blue << endl;
        plikOut << "Case #" << i+1 << ": ";
        if(red)
        if(blue)
        plikOut << "Both" << endl;
        else plikOut << "Red" << endl;
        else if(blue)
        plikOut << "Blue" << endl;
        else plikOut << "Neither" << endl;


    }

    plikIn.close();
    plikOut.close();


    return 0;
}
