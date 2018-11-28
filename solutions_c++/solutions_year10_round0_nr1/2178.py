#include<iostream>
using namespace std;

const int a=1;

int main()
{
    int T;
    scanf("%d",&T);
    for(int TestNum=1;TestNum<=T;TestNum++)
    {
        int N,K;
        scanf("%d%d",&N,&K);
        int a2=(a<<N);

        if(((K+1)%a2)==0)
            printf("Case #%d: ON\n",TestNum);
        else
            printf("Case #%d: OFF\n",TestNum);
    }
}
