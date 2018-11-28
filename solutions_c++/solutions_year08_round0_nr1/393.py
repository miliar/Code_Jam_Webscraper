#include <iostream>
using namespace std;

char engs[128][128];
int queries[1024];

int table[1024][128];

int main()
{
    int T;
    cin >> T;
    
    while(T--)
    {
        int S;
        cin >> S;
        
        cin.getline(engs[0], 128);
        for(int i = 0; i < S; i++)
            cin.getline(engs[i], 128);
              
        char buf[128];
        int Q;
        cin >> Q;
        
        cin.getline(buf, 128);
        for(int i = 0; i < Q; i++)
        {
            queries[i] = -1;
            cin.getline(buf, 128);
            for(int j = 0; j < S; j++)
                if(!strcmp(buf, engs[j]))
                {
                    queries[i] = j;
                    break;
                }
            assert(queries[i] != -1);
        }
            
            
        memset(table, 0, sizeof(table));
        table[0][queries[0]] = INT_MAX;
        for(int i = 1; i < Q; i++)
            for(int j = 0; j < S; j++)
            {
                table[i][j] = INT_MAX;
                if(queries[i] != j)
                    for(int k = 0; k < S; k++)
                        if(table[i - 1][k] != INT_MAX)
                            table[i][j] = min(table[i][j], table[i - 1][k] + (j != k));
            }
                
        int ans = INT_MAX;
        for(int j = 0; j < S; j++)
            ans = min(ans, table[Q - 1][j]);
 
        static int times = 0;       
        cout << "Case #" << ++times << ": " << ans << '\n';
        /*
        for(int i = 0; i < Q; i++, cout << '\n')
        for(int j = 0; j < S; j++)
        cout << table[i][j] << ' ';*/
    }
    
    return 0;   
}
