#include <iostream>
#include <cstdio>
using namespace std;

#define MAXN 1000

typedef long long LL;

bool used[MAXN];
LL groups[MAXN], seq[2 * MAXN];
LL TIMES, LIMIT, N, large[2 * MAXN];

LL solve()
{
    memset(used, 0, sizeof(used)); 
    memset(seq, -1, sizeof(seq));
    memset(large, 0, sizeof(large));
          
    LL sum = 0;
    for (int i = 0; i < N; i++)
        sum += groups[i];      
          
    int ind = 0, start = 0;   
    LL cur = 0, res = 0, take = 0; 
          
    for (;;)
    {
        if (cur + groups[ind] > LIMIT || cur == sum)
        {
           used[start] = true;
           
           seq[take] = start;
           large[take] = cur;
           take++;
           
           res += cur;     
           cur = 0;
           
           if (take == TIMES)
              break;
                
           start = ind;
           if (used[start])
           {
               LL one = 0, size = 0, save = -1;            
               for (int i = take - 1; i >= 0; i--)
               {
                   size++;
                   one += large[i];                
                   if (seq[i] == start)
                   {
                      save = i;        
                      break;
                   }
               }
               
               LL rem = TIMES - take;
               LL full = rem / size;
               LL mod = rem % size;
               
               LL temp = 0;
               for (int i = save; i < save + mod; i++)
                   temp += large[i];
                               
               return res + (full * one) + temp;       
           }
        }
        
        cur += groups[ind];
        ind++;
        
        if (ind == N)
           ind = 0;
    }      
    
    return res;
} 

int main()
{
    int T;
    cin >> T;
    
    for (int TT = 1; TT <= T; TT++)
    {
        cin >> TIMES >> LIMIT >> N;
        
        for (int i = 0; i < N; i++)
            cin >> groups[i];
            
        cout << "Case #" << TT << ": " << solve() << endl;
    }
    
    return 0;
}
