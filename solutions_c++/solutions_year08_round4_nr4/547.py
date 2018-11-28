#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

//inline int abs(int x){return x<0 ? -x : x;}

int main()
{
    FILE *in = fopen("input.txt", "r");
    FILE *out=fopen("output.txt", "w");
    int T, test;
    fscanf(in, "%ld", &T);
    for (test = 1;test<=T;test++)
    {
        char str[10000], str2[10000];
        int len, k, x[5]={0,1,2,3,4}, i, res = 10000;
        fscanf(in, "%ld", &k);
        fscanf(in, "%s", str);
        len = strlen(str);
        while(next_permutation(x, x+k) )
        {
            for (i=0;i<len;i++)
                str2[i] = str[x[i%k] + (i/k)*k];

            char prev='-';
            int count = 0;
            for (i=0;i<len;i++)
            {
                if (str2[i]!=prev)
                {
                    count++;
                    prev = str2[i];
                }
            }
            if (count < res) res = count;
        }
        fprintf(out, "Case #%ld: %ld\n", test, res);
    }


    fclose(in);
    fclose(out);
    return 0;
}
