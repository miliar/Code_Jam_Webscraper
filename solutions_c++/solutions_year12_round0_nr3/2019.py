#include <cstdio>
#include <cstring>
#include <memory.h>

char* split(int number);
int setIsSet(char* digits, int isSet[], int max);

int isSet[2000002];

int main() 
{
    int t;
    scanf("%d", &t);
    int cn2[10] = {0, 0, 1, 3, 6, 10, 15, 21, 28, 36};
    for (int caseNum = 1; caseNum <= t; ++caseNum)
    {
        memset(isSet, -1, sizeof(isSet));
        int result = 0;
        int a, b;
        scanf("%d %d", &a, &b);
        memset(isSet + a, 0, (b - a + 1) * sizeof(int));
        for (int idx = a; idx < b; ++idx)
        {
            if (isSet[idx] != 0)
                continue;
            isSet[idx] = 1;
            char* digits = split(idx);
            int validCount = setIsSet(digits, isSet, b);
            delete[] digits;
            result += cn2[validCount];
        }
        printf("Case #%d: %d\n", caseNum, result);
    }
    return 0;
}

char* split(int number)
{
    char* digits = new char[10];
    int idx = 0;
    while (number > 0)
    {
        digits[idx] = number % 10 + '0';
        number /= 10;
        ++idx;
    }
    digits[idx] = '\0';
    return digits;
}

int setIsSet(char* digits, int isSet[], int max) 
{
    int length = strlen(digits);
    int count = 1;
    for (int ptr = length - 2; ptr >= 0; --ptr)
    {
        if (digits[ptr] == '0')
            continue;
        int tmp = 0;
        for (int idx = 0; idx < length; ++idx)
        {
            tmp = tmp * 10 + digits[(ptr - idx + length) % length] - '0';
        }
        if (tmp > max)
            continue;
        if (isSet[tmp] == 0)
        {
            ++count;
            isSet[tmp] = 1;
        }
    }
    return count;
}
