#include <stdio.h>
#include <map>
#include <string>
#include <iostream>
using namespace std;

int main()
{
    int N; scanf("%d", &N);
    
    for (int q = 0; q < N; q++)
    {
        map<string, int> T;
        
        int S;
        scanf("%d\n", &S);
        for (int i = 0; i < S; i++)
        {
            char a[101];
            gets(a);
            string s = a;

            T[s] = -5;
        }
        int Q;
        scanf("%d\n", &Q);
        int swit = 0, prev = -1;
        int cnt = 0;
        
        for (int i = 0; i < Q; i++)
        {
            char a[101];
            gets(a);
            string s = a;
            
            if (T.count(s) == 0) continue;
            if (T[s] >= prev) continue;
            
            if (T[s] < prev) T[s] = i, cnt++;
            if (cnt == S)
            {
                    cnt = 1;
                    swit++;
                    prev = i;
            }
        }
        printf("Case #%d: %d\n", q+1, swit);
    }
    return 0;
}
