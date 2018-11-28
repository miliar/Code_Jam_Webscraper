#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#define LEN  256
using namespace std;

char list[LEN] = {0};
char alien[70] = {0};
int base = 1;

unsigned __int64 res(unsigned __int64 a, unsigned __int64 base)
{

    unsigned __int64 res = base;
    if(a == 0)
    {
        return res = 1;
    }
    for(int i = 1;  i< a; i++)
    {
        res = base*res;
    }
    return res;
}

//sort(stick, stick+n, greater<int>());
int main()
{
    int T = 0;
    unsigned __int64 n = 0;
    scanf("%d", &T);
    for(int t=0; t<T; t++)
    {
        //scanf("%I64ud", &n);
        memset(list, -1, LEN);
        memset(alien, 0, 70);
        //sprintf(list, "%I64ud", n);
        scanf("%s", alien);
        int len = strlen(alien);
        base = 1;
        bool flag = false;
        list[alien[0]] = base;
        for(int i =1; i<len; i++ )
        {
            if(list[alien[i]] < 0)
            {
                if(flag)
                {
                    base++;
                    list[alien[i]] = base;
                }
                else
                {
                    flag = true;
                    list[alien[i]] = 0;
                }
            }
        }

        base++;


        unsigned __int64 r = 0;
        for(int j = 0; j<len; j++)
        {
            unsigned __int64 x = res( len-j-1, base);
            r += (unsigned __int64)list[alien[j]]*x;
        }

        printf("Case #%d: %I64u\n", t+1, r);
        
    }
    
    return 0;
}