
#include <list>
#include <iostream>

using namespace std;

typedef unsigned uT;

typedef list<uT> listT;

int main()
{
    uT t, R, K, N, g;

    scanf("%u" ,&t);

    for(int i = 0; i < t; ++i)
    {
        scanf("%u %u %u", &R, &K, &N);

        listT grps;

        uT sum = 0, rsum = 0, cnt = 0;
        
        for(int j = 0; j < N; ++j)
        {
            scanf("%u", &g);       
            grps.push_back(g);
            sum += g;
        }
    
        if (sum <= K) 
        {
            printf("Case #%u: %u\n", i+1, sum*R);
            continue;
        }
        
        sum = 0;

        for(listT::iterator it = grps.begin(); it != grps.end() && (cnt != R);)
        {
            if ((rsum  + *it) <= K) 
            {
                rsum += *it;

                grps.push_back(*it);

                ++it;
            }
            else 
            { 
                ++cnt; sum += rsum; 
                rsum = 0;
            }
        }

        printf("Case #%u: %u\n", i+1, sum);
    }
 return 0;   
}
