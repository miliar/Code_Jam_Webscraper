#include <stdio.h>
#include <iostream>
#include <time.h>
#include <string>

using namespace std;

char str[1024];
char s[20] = "welcome to code jam";
int f[510][20];

unsigned int solve(int start, int pos)
{
    unsigned int result = 0;
    if (pos > 18)
        return 1;

    for(int i=start; i<strlen(str); i++)
    {
        if (str[i] == s[pos])
        {
            if (f[i+1][pos+1] == -1)
            {
                f[i+1][pos+1] = solve(i+1, pos+1);
            }

            result = (result + f[i+1][pos+1]) % 10000;
        }
    }

    return result;
}

void main()
{
    int i,n;
    FILE *fp1,*fp2;

    clock_t t1 = clock();


    fp1 = fopen("in.txt", "r");
    fp2 = fopen("out.txt", "w+");
    fscanf(fp1, "%d", &n);
    fgets(str, 1024, fp1);
    
    for(i=0; i<n; i++)
    {
        memset(f, -1, sizeof(f));
        unsigned int sum = 0;
       
        fgets(str, 1024, fp1);
        sum = solve(0, 0);
        sum = sum % 10000;

        if (sum < 10)
        {
            fprintf(fp2, "Case #%d: 000%d\n",i+1, sum);
            continue;
        }

        if (sum < 100)
        {
            fprintf(fp2, "Case #%d: 00%d\n",i+1, sum);
            continue;
        }

        if (sum < 1000)
        {
            fprintf(fp2, "Case #%d: 0%d\n",i+1, sum);
            continue;
        }

        if (sum < 10000)
        {
            fprintf(fp2, "Case #%d: %d\n",i+1, sum);
            continue;
        }

        cout << i+1 << " " << sum << endl;
    }

    clock_t t2 = clock();
    cout << t2 - t1 << endl;
}