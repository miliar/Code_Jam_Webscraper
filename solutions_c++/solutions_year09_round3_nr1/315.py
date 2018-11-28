#include <stdio.h>
#include <map>
#include <string.h>

using namespace std;

int main()
{
    int T, test;
    scanf("%d", &T);
    for (test=1;test<=T;test++)
    {
        char str[256], c;
        int i, len, last = 0;
        map<char, int> M;
        scanf("%s", str);
        len = strlen(str);
        c = str[0];
        M[c] = 1;

        for (i=1;i<len;i++)
        {
            c = str[i];
            if (M.find(c) == M.end() )
            {
                M[c] = last;
                if (last==0) last = 2;
                else last++;
            }
        }
        //last++;
        if (last==0) last = 2;

        long long res = 0, k;
        for (i=0;i<len;i++)
        {
            c = str[i];
            k = M[c];
            res = res*((long long)last) + k;
        }
        printf("Case #%d: %I64d\n", test, res);
    }
    return 0;
}
