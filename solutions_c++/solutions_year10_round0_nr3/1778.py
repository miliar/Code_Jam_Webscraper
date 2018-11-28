
#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    FILE* fin = fopen("C-large.in", "r");
    FILE* fout = fopen("C-large.out", "w");
 
    __int64 r, k, n;
    __int64 d[1001];
    __int64 v[1001];
    __int64 sum = 0;
      
    __int64 cnt = 0;
  
    __int64 pp[1001];
    __int64 f[1001];
    __int64 t;
    fscanf(fin, "%I64d", &t);
    for (__int64 i = 0; i < t; i++)
    {
        memset(f, 0, sizeof(f));
        sum = 0;
        cnt = 0;
        fprintf(fout, "Case #%I64d: ", i+1);
        fscanf(fin, "%I64d%I64d%I64d", &r, &k, &n); //
        for (__int64 j = 0; j < n; j++)
        {
            fscanf(fin, "%I64d", &d[j]); //
            sum += d[j];
        }
        if (sum <= k)
        {
           fprintf(fout, "%I64d\n", r*sum); //
           continue;
        }
        __int64 pos = 0;
        __int64 start;
        while (1)
        {
              if (f[pos])
              {
                 start = pp[pos];
                 break;
              }
              f[pos] = 1;
              pp[pos] = cnt;
              __int64 tmp = 0;
              while (tmp+d[pos] <= k)
              {
                    tmp += d[pos];
                    pos = (pos+1)%n;
              }
              v[cnt] = tmp;
              cnt++;
        }
        
        sum = 0;
        for (__int64 j = start; j < cnt; j++)
        {
            sum += v[j];
        }
        /*
        for (__int64 j = start; j < cnt; j++)
        {
            pr__int64f("%I64d ", v[j]);
        }
        pr__int64f("\n");
        */
        __int64 res = 0;
        __int64 j;
        for (j = 0; j < start && j < r; j++)
        {
            res += v[j];
        }
        if (j == r)
        {
           fprintf(fout, "%I64d\n", res);
           continue;
        }
        r -= j;
        res += sum*(r/(cnt-start));
        for (__int64 j = 0; j < r%(cnt-start); j++)
        {
            res += v[j+start];
        }
        fprintf(fout, "%I64d\n", res);
    }
    
  //  system("pause");
    return 0;
}

