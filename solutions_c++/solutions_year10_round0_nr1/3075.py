#include<iostream>
#include<cmath>
using namespace std;

int main()
{
    freopen("inA.txt","r",stdin);
    freopen("outA.txt","w",stdout);
    int Case;
    cin >> Case;
    for(int k = 1; k <=Case ; k++)
    {
        int N,K;
        cin >> N >> K;
        long  mod = (int)pow(2.0f,N);
        printf("Case #%d: ",k);
        if(K%mod == mod-1) printf("ON");
        else printf("OFF");
        putchar('\n');

    }
    return 0;
}
