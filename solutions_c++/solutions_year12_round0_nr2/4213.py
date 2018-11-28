#include <iostream>
using namespace std;

void main()
{
    FILE *fp1,*fp2;
    fp1 = fopen("in.txt", "r");
    fp2 = fopen("out.txt", "w+");

    int t;
    fscanf(fp1, "%d", &t);
    for (int i=1; i<=t; i++)
    {
        int n;
        int s;
        int p;
        int result = 0;
        fscanf(fp1, "%d", &n);
        fscanf(fp1, "%d", &s);
        fscanf(fp1, "%d", &p);

        int ti[100] = {0};

        for (int j=0; j<n; j++)
        {
            fscanf(fp1, "%d", &ti[j]);

            if (ti[j] > (p-1) * 3)
            {
                result++;
            }
            else if ((p-1) * 3 -2 > 0 && ti[j] > (p-1) * 3 -2 && s > 0)
            {
                result++;
                s--;
            }
        }

        fprintf(fp2, "Case #%d: %d\n", i, result);
    }
}