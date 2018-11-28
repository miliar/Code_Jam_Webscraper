#include <cstdio>
#include <utility>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

char combinations[256][256];
bool opposings[256][256];

int main(int argc, char** argv)
{
    int T;
    scanf("%d", &T);
    
    for(int t = 1; t <= T; ++t)
    {
        printf("Case #%d: ", t);
        
        for(int i = 0; i < 256; ++i)
        {
            fill(combinations[i], combinations[i] + 256, 0);
            fill(opposings[i], opposings[i] + 256, false);
        }
        
        int C;
        scanf("%d", &C);
        for(int i = 0; i < C; ++i)
        {
            char a, b, c;
            scanf(" %c%c%c", &a, &b, &c);
            combinations[a][b] = c;
            combinations[b][a] = c;
        }
        
        int D;
        scanf("%d", &D);
        for(int i = 0; i < D; ++i)
        {
            char a, b;
            scanf(" %c%c", &a, &b);
            opposings[a][b] = true;
            opposings[b][a] = true;
        }
        
        vector<char> stuff;
        
        int N;
        scanf("%d ", &N);
        for(int i = 0; i < N; ++i)
        {
            char a;
            scanf("%c", &a);
            
            stuff.push_back(a);
            
            /// Invoke first
            while(stuff.size() >= 2)
            {   
                char back = stuff[stuff.size() - 1];
                char back2 = stuff[stuff.size() - 2];
                
                if(combinations[back][back2] != 0)
                {
                    stuff.pop_back();
                    stuff.pop_back();
                    stuff.push_back(combinations[back][back2]);
                }
                else
                {
                    break;
                }
            }
            
            /// Then oppose
            if(stuff.size() >= 2)
            {
                for(int i = 0; i < stuff.size(); ++i)
                    for(int j = i + 1; j < stuff.size(); ++j)
                        if(opposings[stuff[i]][stuff[j]])
                        {
                            stuff.clear();
                            goto doneloop;
                        }
                            
                doneloop:;
            }
        }
        
        if(stuff.size() == 0)
        {
            printf("[]\n");
        }
        else if(stuff.size() == 1)
        {
            printf("[%c]\n", stuff[0]);
        }
        else
        {
            printf("[%c", stuff[0]);
            for(int i = 1; i < stuff.size(); ++i)
                printf(", %c", stuff[i]);
            printf("]\n");
        }
    }
    
    return 0;
}