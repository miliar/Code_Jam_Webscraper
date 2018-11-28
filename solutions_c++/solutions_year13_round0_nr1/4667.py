#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream infile("q1.in");
    ofstream outfile("q1.out");
    unsigned int T;
    char table[5][5];
    char responses[4][200] = {"X won" , "O won" , "Draw" , "Game has not completed"};
    infile >> T;
    infile.getline(table[0],5);
    cout << T << "\n";
    for (unsigned short i = 0; i<T; i++)
    {
        for (unsigned short j=0;j<4;j++)
        {
            infile.getline(table[j],5);
            cout <<table[j] << "\n";
        }
        cout << "\n";
        signed short resp = -1;
        signed short incomp = 0;
                    unsigned short hx,vx,ho,vo;
        for (unsigned short j=0;j<4;j++)
            for (unsigned short k=0;k<4;k++)
                incomp |= (table[j][k]=='.');
        for (unsigned short j=0;j<4;j++)
        {
            hx=1, vx=1,ho=1,vo=1;
            for (unsigned short k=0;k<4 ;k++)
            {
                hx &= ((table[j][k] == 'X') || ((table[j][k] == 'T')));
                ho &= ((table[j][k] == 'O') || ((table[j][k] == 'T')));
                vx &= ((table[k][j] == 'X') || ((table[k][j] == 'T')));
                vo &= ((table[k][j] == 'O') || ((table[k][j] == 'T')));
            }
            if (hx || vx || ho || vo) break;
        }



        unsigned short x = hx || vx || (((table[0][0] == 'X') || (table[0][0] == 'T')) &&
                                  ((table[1][1] == 'X') || (table[1][1] == 'T')) &&
                                  ((table[2][2] == 'X') || (table[2][2] == 'T')) &&
                                  ((table[3][3] == 'X') || (table[3][3] == 'T'))) ||
                                 (((table[3][0] == 'X') || (table[3][0] == 'T')) &&
                                  ((table[2][1] == 'X') || (table[2][1] == 'T')) &&
                                  ((table[1][2] == 'X') || (table[1][2] == 'T')) &&
                                  ((table[0][3] == 'X') || (table[0][3] == 'T')));

        unsigned short o = ho || vo || (((table[0][0] == 'O') || (table[0][0] == 'T')) &&
                                  ((table[1][1] == 'O') || (table[1][1] == 'T')) &&
                                  ((table[2][2] == 'O') || (table[2][2] == 'T')) &&
                                  ((table[3][3] == 'O') || (table[3][3] == 'T'))) ||
                                 (((table[3][0] == 'O') || (table[3][0] == 'T')) &&
                                  ((table[2][1] == 'O') || (table[2][1] == 'T')) &&
                                  ((table[1][2] == 'O') || (table[1][2] == 'T')) &&
                                  ((table[0][3] == 'O') || (table[0][3] == 'T')));
        if (x)
            resp = 0;
        else if (o)
            resp = 1;
        else if (incomp)
            resp = 3;
        else resp = 2;
        outfile << "Case #" << i+1 << ": " <<responses[resp] << "\n";
        infile.getline(table[0],4);
    }
    infile.close();
    outfile.close();
    return 0;
}
