#include <iostream>
using namespace std;

bool W[500][15][26];
char Dict[5000][16];

int N, D, L;

int main()
{
    cin >> L >> D >> N;
    
    for (int i = 0; i < D; i++) cin >> Dict[i];
    
    for (int i = 0; i < N; i++)
    {
        string S;
        cin >> S;
        
        int pos = -1;
        bool inbr = 0;
        for (int k = 0; k < S.size(); k++)
        {
            if (S[k] == '(') inbr = 1, pos++;
            else if (S[k] == ')') inbr = 0;
            else
            {
                if (!inbr) pos++;
                W[i][pos][ S[k]-'a' ] = 1;
            }
        }
    }
    
    for (int i = 0; i < N; i++)
    {
        cout << "Case #" << i+1 <<": ";
        
        int ans = 0;
        for (int k = 0; k < D; k++)
        {
            ans++;
            for (int j = 0; j < strlen(Dict[k]); j++)
             if (!W[i][j][ Dict[k][j]-'a' ]) { ans--; break; }
        }
        
        cout << ans << endl;
    }
    return 0;
        
}
