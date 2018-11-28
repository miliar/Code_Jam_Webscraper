#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <cstring>
#include <cstdlib>
#include <set>

using namespace std;

struct ctr
{
    int St, Fin;
};

bool cmp(ctr a, ctr b)
{
    if (a.St!=b.St)
    return (a.St < b.St);
    return a.Fin < b.Fin;
}

int main()
{
    int T;
    scanf("%d", &T);
    
    for (int test=1; test<=T; test++)
    {
        int N;
        scanf("%d", &N);
        ctr Line[1005];
        
        for (int i=0; i<N; i++)
        {
            int a, b;
            scanf("%d%d", &a, &b);
            Line[i].St = a;
            Line[i].Fin = b;
        }
        
        sort(Line, Line+N, cmp);

        int Ans=0;
        for (int i=0; i<N; i++)
        {
            for (int j=i+1; j<N; j++)
            {
                if (Line[i].St<=Line[i].St && Line[i].Fin>=Line[j].Fin)
                    Ans++;
                
            }
        }
        printf("Case #%d: %d\n", test, Ans);
    }
    
    return 0;
}
