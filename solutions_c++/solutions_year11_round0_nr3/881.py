#include <stdio.h>

int T;              // no of test cases
int N;              // no of candies
int candies[2000];  // value of the candies
int val;            // the value of candies sean got

bool splitCandies()
{
    int sum=0;
    int min = 10000000;
    int xor = 0;
    for(int i=1; i<=N;i++)
    {
        int curCandy = candies[i];
        sum+=curCandy;
        xor^=curCandy;
        min = (curCandy < min) ? curCandy : min;
    }

    val = sum - min;
    if(xor == 0)
        return true;
    else 
        return false;
}

int main()
{
    FILE *fp = fopen("c:\\inp.txt", "r+"); // get input data from file
    fscanf(fp, "%d", &T);

    FILE *fpo = fopen("c:\\op.txt", "w+"); // write op data to file

    for(int c=1;c<=T;c++)    // process each test case
    {
        fscanf(fp, "%d", &N);
        for(int i=1;i<=N;i++)
            fscanf(fp, "%d", &candies[i]);

        bool res = splitCandies();
        fprintf(fpo, "Case #%d: ", c);
        if(res)
            fprintf(fpo, "%d\n", val);
        else
            fprintf(fpo, "NO\n");
    }

    fclose(fp);
    fclose(fpo);
    return 0;
}

