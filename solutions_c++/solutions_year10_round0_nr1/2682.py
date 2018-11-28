#include <cstdio>
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int t, n, kase;
    long long int k;

    cin >> t;

    for(int kase = 1; kase <= t; kase++)
    {
        cin >> n >> k;
        
        printf("Case #%d: ", kase);

        long long int mark = 1;

        for(int i = 0; i < n; i++)
            mark *= 2;

        if(((k%mark)+1) == mark)
            printf("ON\n");
        else
            printf("OFF\n");
    }

    return 0;
}
