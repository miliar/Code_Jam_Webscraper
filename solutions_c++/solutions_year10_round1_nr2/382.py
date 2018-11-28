#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("B-small.in");
ofstream fout("B-small.out");

int D, I, M, N;
int color[200];
int ins[256][256];



int insneed(int a, int b)
{
    if (abs(a-b)<=M) return 0;
    if (M == 0) return (a==b) ? 0: 100000000;
    return (abs(b-a)-1)/M*I;
}

void preprocess()
{
    for (int i=0; i<=255; ++i)
        for (int j=0; j<=255; ++j)
            ins[i][j]=insneed(i,j);
}

int calctwo(int a, int b)
{
    if (abs(a-b)<=M) return 0;
    int res = D;
    for (int i=0; i<=255; ++i)
        for (int j=0; j<=255; ++j)
        {
            int temp = abs(i-a)+abs(j-b)+ins[i][j];
            if (temp < res) res = temp;
        }
    return res;
}

int calcthree(int a, int b, int c)
{
    int res = a+b+c;
    if (D+calctwo(b,c)<res) res = D+calctwo(b,c);
    if (D+calctwo(a,c)<res) res = D+calctwo(a,c);
    if (D+calctwo(a,b)<res) res = D+calctwo(a,b);
    for (int x=0; x<=255; ++x)
        for (int y=0; y<=255; ++y)
            for (int z=0; z<=255; ++z)
            {
                int temp = abs(x-a)+abs(y-b)+abs(z-c);
                temp += ins[x][y]+ins[y][z];
                if (temp<res) res = temp;
            }
    return res;
}


void solve()
{
    fin >> D >> I >> M >> N;
    for (int i = 0; i < N; ++i) fin >> color[i];

    preprocess();

    int ans;

    if (N == 1)
        ans = 0;
    else if (N == 2)
        ans = calctwo(color[0], color[1]);
    else
        ans = calcthree(color[0], color[1], color[2]);

    fout << ans << endl;
}

int main()
{
    int T;
    fin >> T;
    for (int cas = 1; cas <= T; ++cas)
    {
        fout << "Case #" << cas << ": ";
        solve();
    }

    fin.close();
    fout.close();
    return 0;
}
