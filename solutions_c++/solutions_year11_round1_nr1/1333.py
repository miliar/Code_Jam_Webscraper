#include<iostream>

using namespace std;

int f(int N,int D,int G)
{
    if( G==100  &&  D!=100)
        return 0;
    if( G==0    &&  D!=0  )
        return 0;
    for(int i=1;i<=N;i++)
        if((i*D)%100 == 0)
            return 1;
    return 0;
}


int main()
{
    int T,N,D,G;
    scanf("%d",&T);
    for(int i=0;i<T;i++)
    {
        scanf("%d%d%d",&N,&D,&G);
        printf("Case #%d: %s\n",i+1,f(N,D,G)?"Possible":"Broken");
    }
    return 0;
}
