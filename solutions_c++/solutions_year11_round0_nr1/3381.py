#include <iostream>
using namespace std;
#include <stdio.h>
int MAX(int a,int b) { return a>b?a:b; }
int ABS(int a) { return a>0?a:-a; }
int main()
{
    int tmp,N;
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&tmp);
    for(int CA=1;CA<=tmp;CA++)
    {
        scanf("%d",&N);
        string op; int num;
        int Opre,Bpre,Otakes,Btakes;
        Otakes=0; Btakes=0;
        Opre = 1; Bpre = 1;
        cin>>op>>num;
         int ans=0;
        if(op=="O") { Otakes = num; Opre = num; ans+=num; }
        else { Btakes= num; Bpre=num; ans+=num; }
        N--;

        while(N--)
        {
            cin>>op>>num;
            if(op=="O")
            {
                if(Otakes!=0)
                {
                    Btakes=0;
                    Otakes+=ABS(num-Opre)+1;
                    ans+=ABS(num-Opre)+1;
                    Opre=num;
                }
                else
                {
                    int moment = ABS(num-Opre)+1;
                    if(moment<=Btakes) { Otakes = 1; ans+=1; }
                    else { ans+=moment-Btakes; Otakes=moment-Btakes; }
                    Btakes=0;
                    Opre = num;
                }
            }
            else
            {
                if(Btakes!=0)
                {
                    Otakes=0;
                    Btakes+=ABS(num-Bpre)+1;
                    ans+=ABS(num-Bpre)+1;
                    Bpre=num;
                }
                else
                {
                    int moment = ABS(num-Bpre)+1;
                    if(moment<=Otakes) { Btakes = 1; ans+=1; }
                    else { ans+=moment-Otakes; Btakes=moment-Otakes; }
                    Otakes=0;
                    Bpre = num;
                }
            }
        }
        printf("Case #%d: %d\n",CA,ans);
    }
    return 0;
}
