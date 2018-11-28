#include <fstream>
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

#define MAXN 1005
#define MAXM 15
ofstream out("output.txt");


int T, N, M[MAXN];

int t[MAXN][MAXM];
int O;


//char visited[MAXN];

int countPaths(int s, int e)
{
    if(s==e) return 1;
    if(M[s]==0 || e==O /*|| visited[s]*/) return 0;
    int found=0;
    for(int i=0; i < M[s]; i++)
    {
       // cout << "IN R: s: " << t[s][i] << " e: " << e << endl;
        //visited[t[s][i]]=true;
        found+=countPaths(t[s][i], e);
       // cout << "Res: "  << found << endl;
    }
    return found;

}

void solve()
{
    for(int i=0; i < N; i++)
        for(int j=0; j < N; j++)
        {
            if(i!=j)
            {
                O=i;
                int path=countPaths(i, j);
                //cout << "s: " << i << " e: " << j << " p: " << path << endl;
                if(path>1)
                {
                    out << "Yes" << endl;
                    return;
                }
            }
        }
    out << "No" << endl;
}

int main()
{
    #ifdef DEBUG
    ifstream cin("input.txt");
    #endif

    cin >> T;

    for(int i=0; i < T; i++)
    {
        cin >> N;
        for(int j=0; j < N; j++)
        {
            cin >> M[j];
            for(int k=0; k < M[j]; k++)
            {
                cin >> t[j][k];
                t[j][k]--;
            }

        }
        out << "Case #" << i+1 << ": ";
        solve();
    }



    return 0;
}
/*
int g[MAXN][MAXN];

int N, T, M[MAXN];

void solve()
{
    for(int i=0; i < N; i++)
        for(int j=0; j< N;j++)
            for(int k=0; k < N; k++)
                g[i][i]+=g[i][k] * g[k][j];

    for(int i=0; i < N; i++)
        for(int j=0; j < N; j++)
            if(g[i][j]>1)
            {
                out << "Yes" << endl;
                return;
            }
    cout << "No" << endl;
}

int main()
{
    #ifdef DEBUG
    ifstream cin("input.txt");
    #endif

    cin >> T;

    for(int i=0; i < T; i++)
    {
        cin >> N;
        for(int j=0; j < N; j++)
        {
            cin >> M[j];
            for(int k=0; k < M[j]; k++)
            {
                int ne;
                cin >> ne;
                g[j][ne-1]=1;
            }
        }

        for(int j=0; j < N; j++)
        {
            for(int k=0; k < N; k++)
            {
                cout << g[j][k] << " ";
            }
            cout << endl;
        }

        out << "Case #" << i+1 << ": ";
        solve();
        for(int j=0; j < N; j++)
        {
            for(int k=0; k < N; k++)
            {
                cout << g[j][k] << " ";
            }
            cout << endl;
        }
    }



    return 0;
}*/
