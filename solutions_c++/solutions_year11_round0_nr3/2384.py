#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int addRemaining(int index);
void solveCase(FILE *fp, int index);
bool checkSplit(int partition);

#define MAX_CANDIES (1010)
int numberOfCandies;
int candies[MAX_CANDIES];

int main()
{
    FILE *fp = fopen("output.txt", "w");

    int numberOfCases;
    fscanf(stdin, "%d", &numberOfCases);
    for(int i=0; i < numberOfCases; i++)
    {
        solveCase(fp, i);
    }

    fclose(fp);
    return 0;
}

void solveCase(FILE *fp, int index)
{
    fprintf(fp, "Case #%d: ", (index + 1));

    fscanf(stdin, "%d", &numberOfCandies);
    for(int i=0; i < numberOfCandies; i++)
    {
        fscanf(stdin, "%d", &candies[i]);
    }

    int xorsum = 0;
    for(int i=1; i < numberOfCandies; i++)
    {
        xorsum ^= candies[i];

        /*
        if(checkSplit(i))
        {
            fprintf(fp, "%d\n", addRemaining(i));
            return;
        }*/
    }
    if(xorsum != candies[0])
        fprintf(fp, "NO\n");
    else
    {
        int min = candies[0];
        int sum = candies[0];
        for(int i=1; i < numberOfCandies; i++)
        {
            if(candies[i] < min) min = candies[i];
            sum += candies[i];
        }
        sum -= min;
        fprintf(fp, "%d\n", sum);
    }
}

bool checkSplit(int partition)
{
    int pattrickSum = 0;
    for(int i=0; i < partition; i++)
    {
        pattrickSum ^= candies[i];
    }

    int seanSum = 0;
    for(int i=partition; i < numberOfCandies; i++)
    {
        seanSum ^= candies[i];
    }

    if(pattrickSum == seanSum)
    {
        return true;
    }
    return false;
}

int addRemaining(int index)
{
    int sum = 0;
    for(int i=index; i < numberOfCandies; i++)
    {
        sum += candies[i];
    }
    return sum;
}
