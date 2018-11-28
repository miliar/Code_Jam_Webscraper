#include <iostream>
#include <vector>

using namespace std;

bool valido (int i, int j, int N)
{
    return ((i < N && i >= 0) && (j < N && j >=0));
}

bool vertical (int i, int j, char c, vector <vector <char> > &V, int N, int K2)
{
    for (int k = 0; k < K2; k++)
    {
        if (!valido(i-k, j, N)) return 0;
        if (V[i-k][j] != c) return 0;
    }
    return 1;
}

bool horizontal (int i, int j, char c, vector <vector <char> > &V, int N, int K2)
{
    for (int k = 0; k < K2; k++)
    {
        if (!valido(i, j-k, N)) return 0;
        if (V[i][j-k] != c) return 0;
    }
    return 1;
}

bool diagonali (int i, int j, char c, vector <vector <char> > &V, int N,  int K2)
{
    for (int k = 0; k < K2; k++)
    {
        if (!valido(i+k, j+k, N)) return 0;
        if (V[i+k][j+k] != c) return 0;
    }
    return 1;
}

bool diagonald (int i, int j, char c, vector <vector <char> > &V, int N,  int K2)
{
    for (int k = 0; k < K2; k++)
    {
        if (!valido(i-k, j-k, N)) return 0;
        if (V[i-k][j-k] != c) return 0;
    }
    return 1;
}

int main ()
{
    int T, casos = 0;
    cin >> T;
    while (T--)
    {
        casos++;
        int K, N;
        cin >> N >> K;
        vector <vector <char> > V (N, vector <char> (N));
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                //rotado
                cin >> V[j][N-i-1];
            }
        }

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N;j++)
            {
                if (V[N-j-1][i] == '.')
                {

                    for (int k = N-j-2; k >= 0; k--)
                    {
                        if (V[k][i] != '.')
                        {
                            swap (V[N-j-1][i], V[k][i]);
                            break;
                        }
                    }
                }
            }
        }

        bool winR = 0, winB = 0;
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N;j++)
            {
                if (V[i][j] != '.')
                {
                    if (V[i][j] == 'R')
                    {
                        if (!winR)
                        {
                            if (horizontal (i, j, V[i][j], V, N, K) || vertical (i, j, V[i][j], V, N, K) || diagonald (i, j, V[i][j], V, N, K) || diagonali (i, j, V[i][j], V, N, K))
                            {
                                winR = 1;
                            }
                        }
                    }
                    else
                    {
                        if (!winB)
                        {
                            if (horizontal (i, j, V[i][j], V, N, K) || vertical (i, j, V[i][j], V, N, K) || diagonald (i, j, V[i][j], V, N, K) || diagonali (i, j, V[i][j], V, N, K))
                            {
                                winB = 1;
                            }
                        }
                    }
                }
            }
        }

        cout << "Case #" << casos << ": ";
        if (winR && winB)
        {
            cout << "Both";
        }
        if (!winR && winB)
        {
            cout << "Blue";
        }
        if (winR && !winB)
        {
            cout << "Red";
        }
        if (!winR && !winB)
        {
            cout << "Neither";
        }
        cout << endl;
/*
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                //rotado
                cout << V[i][j];
            }
            cout << endl;
        }
*/
    }
    return 0;
}
