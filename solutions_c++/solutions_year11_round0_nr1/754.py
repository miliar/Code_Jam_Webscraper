#include <iostream>
#include <cstdio>
using namespace std;

int T, N;
int who[128], btn[128];

int solve()
{
    int posB = 1, posO = 1, res = 0;
    for (int i = 0; i < N; i++)
    {
        if (who[i] == 0)
        {
           int dist = abs(posB - btn[i]);           
           res += (dist + 1); //+1 for pushing
           posB = btn[i];
           
           for (int j = i + 1; j < N; j++)
           {
               if (who[j] == 1)
               {
                   int tmpD = abs(posO - btn[j]);       
                   int have = dist + 1;
                   if (posO < btn[j])
                   {
                      posO += have;
                      if (posO > btn[j]) posO = btn[j];         
                   }
                   else
                   if (posO > btn[j])
                   {
                      posO -= have;
                      if (posO < btn[j]) posO = btn[j];         
                   }
                   
                   break;      
               }    
           }           
        }
        else
        {
           int dist = abs(posO - btn[i]);           
           res += (dist + 1); //+1 for pushing
           posO = btn[i]; 
           
           for (int j = i + 1; j < N; j++)
           {
               if (who[j] == 0)
               {
                   int tmpD = abs(posB - btn[j]);       
                   int have = dist + 1;
                   if (posB < btn[j])
                   {
                      posB += have;
                      if (posB > btn[j]) posB = btn[j];         
                   }
                   else
                   if (posB > btn[j])
                   {
                      posB -= have;
                      if (posB < btn[j]) posB = btn[j];         
                   }
                   
                   break;      
               }    
           }         
        }
    }
    
    return res;     
}

int main()
{
    cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        cin >> N;
        
        char ch; int pos;
        for (int i = 0; i < N; i++)
        {
            cin >> ch >> pos;
            who[i] = (ch == 'B') ? 0 : 1;
            btn[i] = pos;
        }
        
        int res = solve();
        cout << "Case #" << t << ": " << res << endl;
    }
    
    return 0;
}
