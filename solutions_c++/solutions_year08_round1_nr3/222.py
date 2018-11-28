#include <cstdio>
#include <iostream>
#define MAXN 30
using namespace std;

const int table[MAXN+1]={1,5,27,143,751,935,607,903,991,335,47,943,471,55,447,
463,991,95,607,263,151,855,527,743,351,135,407,903,791,135,647};
int n;

int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    int i,t;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        scanf("%d",&n);
        printf("Case #%d: %03d\n",i+1,table[n]);
    }
    return 0;
}
