#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

const int MAXN = 10000000;

long long powerOfTen[10] = {1};
long long sums[10];
bool used[MAXN];
long long a, b;

long long answer;

inline long long processNumber(int number, int numberOfDigits)
{
    if (used[number])
    {
        return 0;
    }

    used[number] = true;

    int nextNumberSuffix = number;
    int br = 0;
    while(nextNumberSuffix % 10 == 0)
    {
        br++;
        nextNumberSuffix /= 10;
    }

    int nextNumberPrefix = (nextNumberSuffix % 10) * powerOfTen[br];
    nextNumberSuffix /= 10;

    int nextNumber = nextNumberPrefix * powerOfTen[numberOfDigits - br - 1] + nextNumberSuffix;
    if (nextNumber >= a && nextNumber <= b)
    {
        return processNumber(nextNumber, numberOfDigits) + 1;
    }
    else
    {
        return processNumber(nextNumber, numberOfDigits);
    }
}

inline int calculateNumberOfDigits(int value)
{
    if (value == 0)
    {
        return 0;
    }

    return calculateNumberOfDigits(value / 10) + 1;
}

int main()
{
    for (int i = 1; i < 10; i++)
    {
        powerOfTen[i] = powerOfTen[i - 1] * 10;
        sums[i] = sums[i - 1] + i;
    }

    int t;
    scanf ("%d", &t);

    for (int currentTestCase = 1; currentTestCase <= t; currentTestCase++)
    {
        answer = 0;
        memset (used, 0, sizeof(used));

        scanf ("%d %d", &a, &b);

        for (int i = a; i <= b; i++)
        {
            if (!used[i])
            {
                int br = processNumber(i, calculateNumberOfDigits(i));
                if (br > 1)
                {
                    answer += sums[br - 1];
                }
            }
        }

        printf ("Case #%d: %lld\n", currentTestCase, answer);
    }

    return 0;
}
