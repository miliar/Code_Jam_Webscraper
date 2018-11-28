#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>

using namespace std;

//          0 1  2   3    4     5      6       7
long big[]={1,10,100,1000,10000,100000,1000000,10000000};

int getCount(long x, long up)
{
     long now=x;
     int n=0;
     while (now>0)
     {
           now/=10;
           n++;
     }
     n--;
     now=x;
     int out=0;
     do
     {
          now=((now%big[n])*10)+now/big[n];
          if ((now>x)&&(now<=up))
             out++;
     } while (now!=x);
     return out;    
}

int main()
{
    int T;
    cin >> T;
    for (int test=1;test<=T;test++)
    {
        long count=0;
        long A,B;
        cin >> A >> B;
        for (long n=A;n<B;n++)
        {
            count+=getCount(n,B);
        }
        cout << "Case #" << test << ": " << count << endl;
    }
    return 0;
}
