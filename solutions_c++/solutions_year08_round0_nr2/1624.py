#include <iostream>
#include <fstream>

#define MAX 1600
using namespace std;

int cate[2][MAX], vin[2][MAX], pleaca[2][MAX];
int N, NA, NB, T, rezA, rezB;

ifstream fin ("train.in");
ofstream fout("train.out");

int datetomin(string str)
{
    int h = atoi( str.substr(0,2).c_str());
    str.erase(0,3);
    int min = atoi(str.c_str());
    return 60*h + min;
}

void calc()
{
    for (int i = 0; i < datetomin("23:59"); i++)
    {
        if ( i > 0)
        {
            cate[0][i] += cate[0][i-1];
            cate[1][i] += cate[1][i-1];
        }

        cate[0][i+T] += vin[0][i];
        cate[1][i+T] += vin[1][i];

        if ( pleaca[0][i])
        {
            if ( pleaca[0][i] > cate[0][i] )
            {
                rezA+= pleaca[0][i] - cate[0][i];
                cate[0][i] = 0;
            }
            else
                cate[0][i]-=pleaca[0][i];
        }

        if ( pleaca[1][i])
        {
            if ( pleaca[1][i] > cate[1][i] )
            {
                rezB+= pleaca[1][i] - cate[1][i];
                cate[1][i] = 0;
            }
            else
                cate[1][i] -= pleaca[1][i];
        }
    }
}


int main()
{
    fin>>N;
    for (int z = 1; z<=N; z++)
    {
        memset(pleaca,0, sizeof(pleaca));
        memset(vin,0,sizeof(vin));
        memset(cate,0, sizeof(cate));
        rezA = rezB = 0;

        fin>>T>>NA>>NB;
        for ( int i = 0; i<NA; i++)
        {
            string aux, aux2;
            fin>>aux>>aux2;
            pleaca[0][datetomin(aux)]++;
            vin[1][datetomin(aux2)]++;
        }
        for ( int i = 0; i<NB; i++)
        {
            string aux, aux2;
            fin>>aux>>aux2;
            pleaca[1][datetomin(aux)]++;
            vin[0][datetomin(aux2)]++;
        }

        calc();
        fout<<"Case #"<<z<<": "<<rezA<<" "<<rezB<<"\n";

    }

    return 0;
}
