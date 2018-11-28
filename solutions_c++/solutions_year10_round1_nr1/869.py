#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

// declaración de prototipo
string intToBinary(string);

int main()
{
    freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
    
    int T, N, K, k, pi, pj;
    char c;
    string l;
    bool R, B;
    
    cin >> T;
    
    for (int t = 0; t < T; t++) // Tests
    {
        cin >> N >> K;
        
        string cols[N];
        R = false;
        B = false;
        
        for (int n1 = 0; n1 < N; n1++)
        {
            l = "";
            for (int n2 = 0; n2 < N; n2++)
            {
                cin >> c;
                if (c != '.')
                   l += c;
                else
                   l = c + l; 
            }
            cols[N-1-n1] = l;
        }
    
        for (int i = N - 1; i > -1; i--)
        {
            for (int j = N - 1; j > -1; j--)
            {
                if (cols[i][j] == '.')
                   break;
                else
                {
                    if ((cols[i][j] == 'R' && !R) || (cols[i][j] == 'B' && !B))
                    {
                       k = 1;
                       pi = i;
                       pj = j-1;
                       // Comprobamos la columna
                       while ((k < K) && (pj > -1) && (cols[i][pj] == cols[i][j]))
                       { 
                             k += 1;
                             pj -= 1;
                       }
                       if (k == K)
                       {
                             if (cols[i][j] == 'R')
                                 R = true;
                             else
                                 B = true;
                       }
                       k = 1;
                       pi = i-1;
                       pj = j;
                       // Comprobamos la fila
                       while ((k < K) && (pi > -1) && (cols[pi][j] == cols[i][j]))
                       {
                             k += 1;
                             pi -= 1;
                       }
                       if (k == K)
                       {
                             if (cols[i][j] == 'R')
                                 R = true;
                             else
                                 B = true;
                       }
                       k = 1;
                       pi = i-1;
                       pj = j-1;
                       // Comprobamos la diagonal superior
                        while ((k < K) && (pi > -1) && (pj > -1) && (cols[pi][pj] == cols[i][j]))
                       {
                             k += 1;
                             pi -= 1;
                             pj -= 1;
                       }
                       if (k == K)
                       {
                             if (cols[i][j] == 'R')
                                 R = true;
                             else
                                 B = true;
                       }
                       k = 1;
                       pi = i-1;
                       pj = j+1;
                       // Comprobamos la diagonal inferior
                        while ((k < K) && (pi > -1) && (pj < N) && (cols[pi][pj] == cols[i][j]))
                       {
                             k += 1;
                             pi -= 1;
                             pj += 1;
                       }
                       if (k == K)
                       {
                             if (cols[i][j] == 'R')
                                 R = true;
                             else
                                 B = true;
                       }
                    }
                }
                
            }
            if (B && R)
               break;
        }
        
        cout << "Case #" << t + 1;
        if (B)
        {
           if (R)
               cout << ": Both" << endl;
           else
               cout << ": Blue" << endl;
        }
        else
        {
            if (R)
               cout << ": Red" << endl;
            else
               cout << ": Neither" << endl;
        }               
            
    }
    
    return 0;
    
}
