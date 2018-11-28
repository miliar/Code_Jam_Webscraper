#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORI(i,b) FOR(i,0,b)


int main()
{
    ifstream input("input.in",ifstream::in);
    ofstream output("output.out",ofstream::out);

    int t;
    input >> t;

    char ctmp;
    FORI(i,t)
    {
        char field[4][4];
        // Read Field
        FORI(j,4)
        {
            input.get(ctmp);
            FORI(k,4)
            {
                input.get(field[j][k]);
            }
        }
        input.getline(&ctmp,1);
        bool bCompleted = true;
        bool bWon = false;
        char c;

        // check lines
        FORI(j,4)
        {
            c = '\0';
            bool b=true;
            FORI(k,4)
            {
                if(field[j][k]=='.')
                {
                    bCompleted = false;
                    b = false;
                    break;
                }
                if(field[j][k]=='T')
                    continue;
                else if(c=='\0')
                    c = field[j][k];
                else if(c!=field[j][k])
                {
                    b = false;
                    break;
                }
            }
            if(b)
            {
                bWon = true;
                break;
            }
        }

        if(!bWon)
        {   // check columns
            FORI(k,4)
            {
                c = '\0';
                bool b=true;
                FORI(j,4)
                {
                    if(field[j][k]=='.')
                    {
                        bCompleted = false;
                        b = false;
                        break;
                    }
                    if(field[j][k]=='T')
                        continue;
                    else if(c=='\0')
                        c = field[j][k];
                    else if(c!=field[j][k])
                    {
                        b = false;
                        break;
                    }
                }
                if(b)
                {
                    bWon = true;
                    break;
                }
            }
        }

        if(!bWon)
        {   // check diagonals
            c = '\0';
            bool b=true;
            FORI(j,4)
            {
                    if(field[j][j]=='.')
                    {
                        bCompleted = false;
                        b = false;
                        break;
                    }
                    if(field[j][j]=='T')
                        continue;
                    else if(c=='\0')
                        c = field[j][j];
                    else if(c!=field[j][j])
                    {
                        b = false;
                        break;
                    }
            }
            if(!b)
            {
                c='\0';
                b = true;
                FORI(j,4)
                {
                    if(field[j][3-j]=='.')
                    {
                        bCompleted = false;
                        b = false;
                        break;
                    }
                    if(field[j][3-j]=='T')
                        continue;
                    else if(c=='\0')
                        c = field[j][3-j];
                    else if(c!=field[j][3-j])
                    {
                        b = false;
                        break;
                    }
                }
            }
            if(b)
                bWon = true;
        }

        if(bWon)
        {
            output << "Case #" << i+1 << ": " << c << " won"<<endl;
        }
        else if(bCompleted)
            output << "Case #" << i+1 << ": Draw" << endl;
        else
            output << "Case #" << i+1 << ": Game has not completed" << endl;

    }
    return 0;
}
