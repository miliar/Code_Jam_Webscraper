#include <iostream>
using namespace std;

/*
    Returns the digit of a number
    digit(12345) = 5;
*/
int get_digit(int number)
{
    int digit = 1;
    while(number/=10) digit++;
    return digit;
}

/*
    mod(3) = 1000
*/
int get_mod(int digit)
{
    int number = 1;
    while(digit--) number *= 10;
    return number;
}

/*
    recycle(12345, 2) = 45123
*/
int recycle(int number, int size)
{
    int result;
    int mod = get_mod(size);        // mod = 100
    int reminder = number % mod;    // reminder = 45
    result = number / mod;          // result = 123
    result += reminder * get_mod(get_digit(result));    // result = 45123
    return result;
}

void solveCase(int iCase)
{
    int low, high, ans=0;
    scanf("%d %d", &low, &high);
    for(int i=low; i<=high; i++){
        int digit_i = get_digit(i);
        for(int j=1; j<digit_i; j++){
            int recycle_i = recycle(i, j);
            if(i < recycle_i && recycle_i <= high) ans++;
        }
    }
    printf("Case #%d: %d\n", iCase, ans);
}

int main()
{
    freopen("c-small.in", "r", stdin);
    freopen("c-small.out", "w", stdout);
    int iCase,nCase;
    scanf("%d", &nCase);
    for(iCase = 1; iCase <= nCase; iCase++)
    {
        solveCase(iCase);
    }
}