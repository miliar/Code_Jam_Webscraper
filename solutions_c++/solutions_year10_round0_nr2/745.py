#include<iostream>
#include<algorithm>
using namespace std;

int t[1005];
int gcd(int a,int b)
{
    if(a%b==0)
        return b;
    else 
        return gcd(b,a%b);

}
int main()
{
    int T;
    scanf("%d",&T);
    for(int TestNum=1;TestNum<=T;TestNum++)
    {
        int N;
        scanf("%d",&N);
        for(int i=0;i<N;i++)
            scanf("%d",&t[i]);
        int ret,cd;
        sort(t,t+N);
        int cnt=0;
        while(t[cnt++]==0);
        
        if(N==2) 
            cd=abs(t[1]-t[0]);
        else
        {
            if((t[2]-t[1])==0)
                cd=t[1]-t[0];
            else if((t[1]-t[0])==0)
                cd=t[2]-t[1]; 
            else
                cd=gcd(t[2]-t[1],t[1]-t[0]);
        }
        if(cd==0)
            ret=0;
        else
            ret=(cd-(t[1]%cd))%cd;
        printf("Case #%d: %d\n",TestNum,ret);
    }

}
