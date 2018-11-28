#include <iostream>
#include <map>
#include <cstdio>

using namespace std;

typedef long long LL;

void process(void)
{
    int n;
    scanf("%d",&n);
    int smallest = 99999999;
    int rrrrr = 0;
    LL sum = 0;
    for(int i=0;i<n;i++)
    {
        int tmp;
        scanf("%d",&tmp);
        rrrrr ^= tmp;
        smallest = min(smallest, tmp);
        sum += tmp;
    }

    if(rrrrr)
    {
        cout << "NO" << endl;
    }
    else
    {
        cout << sum - smallest << endl;
    }
}

int main(void)
{
    int T;
    scanf("%d",&T);
    for(int i=0;i<T;i++)
    {
        printf("Case #%d: ",i+1);
        process();
    }
}
