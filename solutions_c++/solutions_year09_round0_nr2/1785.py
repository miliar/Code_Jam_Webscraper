// Usage: rename input file -> input.txt
// output file with the solution is output.txt
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

#define MAX_T 100
#define MAX_H 100
#define MAX_W 100
#define MAX_A 10000
#define MAX_B 26

using namespace std;


struct val
{
    int x;
    int c;
}map[MAX_H][MAX_W];

void reset (int * v, int max, int value)
{
    for (int i=0;i<max;i++)
    {
        v[i] = value;
    }
}

int check ( int j, int k, int H, int W, int b)
{
    int min = map[j][k].x;
    int jmin, kmin;
    int dir = 0;
    if (j > 0)
        if (map[j-1][k].x < min)
        {
            min = map[j-1][k].x;
            jmin = j-1;
            kmin = k;
            dir = 1;
        }

    if (k > 0)
        if (map[j][k-1].x < min)
        {
            min = map[j][k-1].x;
            jmin = j;
            kmin = k-1;
            dir = 2;
        }

    if (k < W-1)
        if (map[j][k+1].x < min)
        {
            min = map[j][k+1].x;
            jmin = j;
            kmin = k+1;
            dir = 3;
        }

    if (j < H-1)
        if (map[j+1][k].x < min)
        {
            min = map[j+1][k].x;
            jmin = j+1;
            kmin = k;
            dir = 4;
        }


    if (dir > 0)
    {
        if (map[jmin][kmin].c > 0)
        {
            b = map[jmin][kmin].c;
            map[j][k].c = b;
        }
        else
        {
            map[j][k].c = check(jmin, kmin, H, W,b );
            b = map[j][k].c;
        }
    }
    else
        map[j][k].c = b;

    return b;

}

char numtoalpha(int num)
{
    switch (num)
    {
    case 1:
        return 'a';
        break;
    case 2:
        return 'b';
        break;
    case 3:
        return 'c';
        break;
    case 4:
        return 'd';
        break;
    case 5:
        return 'e';
        break;
    case 6:
        return 'f';
        break;
    case 7:
        return 'g';
        break;
    case 8:
        return 'h';
        break;
    case 9:
        return 'i';
        break;
    case 10:
        return 'j';
        break;
    case 11:
        return 'k';
        break;
    case 12:
        return 'l';
        break;
    case 13:
        return 'm';
        break;
    case 14:
        return 'n';
        break;
    case 15:
        return 'o';
        break;
    case 16:
        return 'p';
        break;
    case 17:
        return 'q';
        break;
    case 18:
        return 'r';
        break;
    case 19:
        return 's';
        break;
    case 20:
        return 't';
        break;
    case 21:
        return 'u';
        break;
    case 22:
        return 'v';
        break;
    case 23:
        return 'w';
        break;
    case 24:
        return 'x';
        break;
    case 25:
        return 'y';
        break;
    case 26:
        return 'z';
        break;
    }
}


int main()
{
    int i,j,k;
    int T, H, W;
    int b;
    bool islast;
    string line;
    char ch;

    ifstream infile("input.txt");
    ofstream outfile("output.txt");

    if (!infile)
    {
        cout << "There was a problem opening the file for reading."
             << endl;
        return 0;
    }

    infile >> T;
    for (i=0;i<T;i++)
    {
        infile >> H >> W;
        outfile << "Case #" << i+1 <<":"<< endl;

        for (j=0;j<H;j++)
        {
            for (k=0;k<W;k++)
            {
                infile >> map[j][k].x;
                map[j][k].c = 0;
            }
        }

        b = 1;

        for (j=0;j<H;j++)
        {
            for (k=0;k<W;k++)
            {
                if (map[j][k].c == 0)
                {
                    map[j][k].c = check (j,k,H,W,b);
                    if (map[j][k].c == b)
                        b++;
                }

                outfile << numtoalpha(map[j][k].c) << " ";
            }
            outfile << endl;
        }

    }

    infile.close();
    outfile.close();

    return 0;
}
