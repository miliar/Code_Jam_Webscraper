#include <cstdlib>
#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <math.h>

using namespace std;

int norm[31];
int surprised[31];
int scores[200];

void update(int *ar, int i, int j, int k)
{
    ar[i + j + k] = max(ar[i + j + k], max(i, max(j, k)));
}

int is_norm(int i, int j, int k)
{
    return abs(i - j) <= 1 && abs(i - k) <= 1 && abs(k - j) <= 1;
}

int is_surp(int i, int j, int k)
{
    return abs(i - j) <= 2 && abs(i - k) <= 2 && abs(k - j) <= 2;
}

int main(int argc, char *argv[])
{
     //FILE* fp = fopen("D:\\Dev-Cpp\\Projects\\Code Jam\\B.txt", "r");
     FILE* fp = fopen("D:\\Dev-Cpp\\Projects\\Code Jam\\B1.in", "r");
     FILE* o_fp = fopen("D:\\Dev-Cpp\\Projects\\Code Jam\\B_out.txt", "w");
    for (int i = 0; i <= 10; ++i)
            for (int j = 0; j <= 10; ++j)
                    for (int k = 0; k <=10; ++k)
                    {
                        if (is_norm(i, j, k))
                           update(norm, i, j, k);
                        if (is_surp(i, j, k))
                             update(surprised, i, j, k);
                    }
    
    /*for (int i = 0; i < 31; ++i)
        printf("i = %d, norm = %d, surp = %d \n", i, norm[i], surprised[i]);*/
    int t;
    fscanf(fp, "%d", &t);
    //printf("%d\n", n);
    //system("PAUSE");
    for (int i = 1; i <=t; ++i)
    {
        int n, s, p;
        fscanf(fp, "%d%d%d", &n, &s, &p);
        for (int j = 0; j < n; ++j)
            fscanf(fp, "%d", &scores[j]);
        
        int counter = 0;
        for (int j = 0; j < n; ++j)
            {
                 if (norm[scores[j]] >= p)
                    ++counter;
                    else if (surprised[scores[j]] >= p && s)
                    {
                         s--;
                         ++counter;
                     }
             }
         printf("%d %d\n", i, counter);    
        fprintf(o_fp, "Case #%d: %d\n", i, counter);
        //system("PAUSE");
    }
    fclose(o_fp);
    
    
    system("PAUSE");
    return 0;
}
