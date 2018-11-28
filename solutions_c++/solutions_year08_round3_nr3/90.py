#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int T, n,m,X, Y,Z;

#define MAX 1005
#define MOD 1000000007

int A[MAX], cnt[MAX][MAX];
vector <int> v;
ifstream fin("inc.in");
ofstream fout("inc.out");

int calc()
{
    memset(cnt, 0, sizeof(cnt));
    int N = v.size();
    for (int i = 0; i<N; i++)
        cnt[1][i] = 1;
    for (int i = 2; i<=N; i++)
        for (int j = i-1; j < N; j++)
        {
            long long rez = 0;
            for ( int k = 0; k < j; k++)
                if ( v[k] < v[j] )
                    rez = ( rez + (long long ) cnt[i-1][k] ) % MOD;
            cnt[i][j] = rez;
        }
    long long rez = 0;
    for ( int i = 1; i<=N; i++)
        for (int j = 0; j<N; j++)
            rez = ( rez + (long long) cnt[i][j] ) % MOD;
    return rez;

}

int main()
{
    fin>>T;
    for (int z=1; z<=T; z++)
    {
        fin>>n>>m>>X>>Y>>Z;
        for ( int i = 0; i<m; i++)
            fin>>A[i];
        v.clear();
        for (int i = 0; i<n; i++)
        {
            v.push_back(A[i % m]);
            A[i % m] = (long long) ( (long long) X * A[i % m] + (long long) Y * (i+1)) % (long long)Z;
        }
        for (int i = 0; i<v.size(); i++)
            cout<<v[i]<<" ";
        cout<<"\n";

        int rez = calc();
        fout<<"Case #"<<z<<": "<<rez<<"\n";
    }

    return 0;
}
