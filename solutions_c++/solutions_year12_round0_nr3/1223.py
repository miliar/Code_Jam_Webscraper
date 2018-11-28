#include <iostream>
#include <cstdio>
#include <set>
using namespace std;

int A, B;
int digits[16];

int lenA;

int getLen(int num)
{
    if (num == 0) return 1;
    
    int len = 0;
    
    while (num > 0)
    {
        len++;  
        num /= 10;  
    }
    
    return len;
}

int how_many(int leftNum)
{
    int len = lenA;
    int tmpLen = lenA - 1;
    
    int tmp = leftNum;
    while (tmp > 0)
    {
        int dig = tmp % 10;
        digits[tmpLen] = dig;
        tmpLen--;
        
        tmp /= 10;
    }
    
    int ans = 0;
    
    set<int> used;
    for (int i = 0; i < len - 1; i++)
    {
        int rightNum = 0;
        for (int j = i + 1; j < len; j++)
            rightNum = rightNum * 10 + digits[j];
            
        for (int j = 0; j <= i; j++)
            rightNum = rightNum * 10 + digits[j];
            
        if (leftNum < rightNum && rightNum <= B && used.count(rightNum) == 0) 
        { 
            used.insert(rightNum); 
            ans++; 
        }
    }    
    
    return ans;
}

int solve()
{
    int result = 0;
    
    for (int i = A; i < B; i++)
        result += how_many(i);    
    
    return result;
}

int main()
{
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++)
    {
        cin >> A >> B;
        lenA = getLen(A);
        
        int result = solve();
        printf("Case #%d: %d\n", t, result);
    }
    
    return 0;
}
