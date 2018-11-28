#include <stdio.h>

inline int abs(int x){return x<0 ? -x : x;}

int main()
{
    FILE *in = fopen("input.txt", "r");
    FILE *out=fopen("output.txt", "w");
    int x1, y1, x2, y2, x3, y3, N, M, A, test, T;
    bool f;
    fscanf(in, "%ld", &T);
    for (test = 1;test<=T;test++)
    {
        f = true;
        fscanf(in, "%ld %ld %ld", &N, &M, &A);
        /*for (x1=0;f && x1<=N;x1++)
          for (y1=0;f && y1<=N;y1++)*/
        x1 = 0; y1 = 0;
            for (x2=0;f && x2<=N;x2++)
              for (y2=0;f && y2<=M;y2++)
                for (x3=0;f && x3<=N;x3++)
                  for (y3=0;f && y3<=M;y3++)
                  {
                      int S = abs((x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1));
                      if (S == A)
                      {
                          f = false;
                          fprintf(out, "Case #%ld: %ld %ld %ld %ld %ld %ld\n", test, x1, y1, x2, y2, x3, y3);
                      }
                  }
        if (f) fprintf(out, "Case #%ld: IMPOSSIBLE\n", test);
        printf("Test %ld\n", test);
    }

    fclose (in);
    fclose(out);
    return 0;
}
