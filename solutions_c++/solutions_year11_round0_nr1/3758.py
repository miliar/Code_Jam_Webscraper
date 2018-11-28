#include <stdio.h>
#include <stdlib.h>

int main()
{
    freopen("/Users/Payut/Documents/Programming/Exercise/Code/Bot trust/Bot trust/A-large.in","r",stdin);
    freopen("/Users/Payut/Documents/Programming/Exercise/Code/Bot trust/Bot trust/A-large.out.txt","w",stdout);
    int C, N;
    int A = 0;
    char aa, bb;
    int count = 0;
    int O = 1, B = 1;
    int walk = 0;
    
    scanf("%d", &C);
    
    for(int i = 0; i<C; i++)
    {
        count = 0;
        walk =0;
        O = 1;
        B = 1;
        
        scanf("%d", &N);

        for(int j = 1; j<=N; j++)
        {
            scanf(" %c %d", &bb, &A);
            
            if ( (j == 1) || (bb == aa))
                {
                    if (bb == 'O')
                    {
                        count += (abs(A-O)+1);
                        walk += (abs(A-O)+1);
                        O = A;
                    }
                    
                    else if (bb =='B')
                    {
                        count += (abs(A-B)+1);
                        walk += (abs(A-B)+1);
                        B = A;
                    }
                    
                    aa = bb;
                }
                
            else if ( bb != aa)
                {
                    if (bb =='O')
                    {
                        if (walk >= (abs(A-O)))
                        {
                            count++;
                            walk = 1;
                        }
                        else if (walk < abs(A-O))
                        {
                            count+= (abs(A-O)-walk+1);
                            walk = (abs(A-O)-walk+1);
                        }
                        O = A;
                    }
                    
                    else if (bb == 'B')
                    {
                        if (walk >= (abs(A-B)))
                        {
                            count++;
                            walk = 1;
                        }
                        
                        else if (walk < abs(A-B))
                        {
                            count+= (abs(A-B)-walk+1);
                            walk = (abs(A-B)-walk+1);
                        }
                        B = A;
                    }
                    
                    aa = bb;
                }
        }
        
        printf("Case #%d: %d\n", i+1, count);
    }
    return 0;
}