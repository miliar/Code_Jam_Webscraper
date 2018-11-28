#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("d.in");
ofstream fout("d.out");

#define MAX 105
#define MOD 10007

int T, H, W, R;
int rock[MAX][MAX], cnt[MAX][MAX];

void calc()
{
    for (int i = 1; i <H; i++)
        for ( int j = 1; j<W; j++)
        {
            if ( !rock[i+2][j+1] )
            {
                cnt[i+2][j+1] += cnt[i][j];
                cnt[i+2][j+1] %= MOD;
            }
            if ( !rock[i+1][j+2])
            {
            cnt[i+1][j+2] += cnt[i][j];
            cnt[i+1][j+2] %= MOD;
            }
        }
}


int main()
{
    fin>>T;
    for (int z = 1; z<=T; z++)
    {
        int rez;
        fin>>H>>W>>R;

        memset(rock, 0, sizeof(rock));
        memset(cnt,0, sizeof(cnt));

        for (int i = 0; i<R; i++)
        {
            int a,b;
            fin>>a>>b;
            rock[a][b] = 1;
        }

        cnt[1][1] = 1;

        calc();

        fout<<"Case #"<<z<<": "<<cnt[H][W]<<"\n";
    }

    return 0;
}
