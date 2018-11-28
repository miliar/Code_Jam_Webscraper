#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <fstream>
using namespace std;

long long dp[1005][3];
int L,N,C;
long long T;
long long arr[1005];

long long solve (int ind , int spd , long long tim)
{
    if (ind == N) return 0LL;
    if (dp[ind][spd] != -1LL) return dp[ind][spd];

    long long dist = arr[ind % C];
    long long add;

    if (tim >= T) add = dist;
    else
    {
        long long diff = T - tim;
        diff /= 2LL;
        diff = min (diff , dist);
        long long d = dist - diff;
        add = (diff * 2LL) + d;
    }

    long long a = 1LL<<40;
    long long b;

    if (spd+1 <= L) a = solve (ind+1 , spd+1 , tim+add) + add;
    b = solve (ind+1 , spd , tim+(dist*2LL)) + (dist * 2LL);

    return dp[ind][spd] = min (a,b);
}

int main ()
{
    ifstream fin ("B.in");
    ofstream fout ("B.out");

    int t;

    fin >> t;

    for (int ID=1; ID<=t; ID++)
    {
        fin >> L >> T >> N >> C;

        for (int i=0; i<C; i++)
            fin >> arr[i];

        fout << "Case #" << ID << ": ";

        memset (dp,-1LL,sizeof(dp));
        long long ret = solve (0,0,0LL);
        fout << ret << '\n';
    }
}
