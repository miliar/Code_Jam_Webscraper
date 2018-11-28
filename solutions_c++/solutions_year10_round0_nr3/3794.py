#include <iostream>
#include <stdio.h>

using namespace std;

const int MaxN = 10;

unsigned int T, R, K, N;
unsigned int G[MaxN];


int main()
{
//    #ifndef ONLINE_JUDGE
//    freopen("in.txt", "r", stdin);
//    freopen("out.txt", "w", stdout);
//   #endif
    unsigned int amount, counter, index =1, header, acum, maxGroups;

    cin>>T;
    while(T--)
    {
        header = amount = counter = 0;
        cin>>R>>K>>N;
        while(counter < N)
        {
            cin>>G[counter++];
        }

        while(R--)
        {
            maxGroups = N;
            acum = 0;
            while(acum + G[header] <=K && maxGroups-- > 0)
            {
                acum += G[header];
                header = (header + 1)%N;
            }
            amount += acum;
        }

        cout<<"Case #"<<index++<<": "<<amount<<endl;
    }
    return 0;
}
