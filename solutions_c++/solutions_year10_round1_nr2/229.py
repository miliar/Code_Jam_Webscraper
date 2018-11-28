#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int D, I, M, N;

int ps[128];
int table[260][128][3];

int calc(int pre, int loc, int ad)
{

//    printf("%d %d\n", pre, loc);
    if(loc == N)
        return 0;
    else if(table[pre][loc][ad])
        return table[pre][loc][ad] - 1;
    else
    {
        int&v = table[pre][loc][ad];
        int prev = pre - 1;

        v = calc(prev + 1, loc + 1, 0) + D;
         if(!pre || abs(prev - ps[loc]) <= M)
            v = min(calc(ps[loc] + 1, loc + 1, 0), v);
 
         
        

        if(M)
        if(pre)
        {
            if(!ad || ad == 1)
                for(int d = prev + 1; d <= 255; d++)
                    if(abs(prev - d) <= M)
                        v = min(v, I + calc(d + 1, loc, 1));
            if(!ad || ad == 2)
                for(int d = prev - 1; d >= 0; d--)
                    if(abs(prev - d) <= M)
                        v = min(v, I + calc(d + 1, loc, 2));            
        }
//        if(v == 0)
  //           printf("!%d %d\n", pre, loc);
        
        for(int d = 0; d <= 255; d++)
            if(!pre || abs(prev - d) <= M)
                v = min(v, abs(ps[loc] - d) + calc(d + 1, loc + 1, 0));

        return v++;
    }
}

int main()
{
    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        memset(table, 0, sizeof(table));
        printf("Case #%d: ", t);


        scanf("%d%d%d%d", &D, &I, &M, &N);
        for(int i = 0; i < N; i++)
            scanf("%d", ps + i);
        
        printf("%d\n", calc(0, 0, 0));
    }

    return 0;
}
