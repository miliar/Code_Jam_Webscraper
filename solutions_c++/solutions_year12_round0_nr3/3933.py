#include <iostream>
#include <cstring>
#include <cmath>
#include <cstdio>
using namespace std;

int mem[10];

int calc(int a, int b)
{
    int cnt = 0;

    for(int i = a; i <= b; i++)
    {
        int temp = i, tot = 1;

        while( temp )
        {
            temp/=10;
            tot *= 10;
        }

        int k = 10, kk = 0;

        while(1)
        {
            int p,q;

            p = i%k;
            q = i/k;

            if( p == i ) break;

            int j = p*( tot/k ) + q;

            if(j > i && p >= (k/10) && j >= a && j <= b)
            {
                bool flag = 0;
                for(int ii = 0; ii < kk; ii++)
                {
                    if( mem[ii] == j)flag = 1;
                }
                if(!flag){
                    cnt ++;
                    mem[kk++] = j;
                }
            }

            k *= 10;
        }
    }

    return cnt;
}

int main()
{
    freopen("i.txt","r",stdin);
    freopen("o.txt","w",stdout);

    int t;
    cin >> t;

    for(int i = 1; i <= t; i++)
    {
        int a, b;

        cin >> a >> b;

        cout << "Case #"<< i <<": ";
        cout << calc(a, b) << endl;

    }

    return 0;
}
