#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <math.h>

using namespace std;

int b[105],o[105];

int main()
{
    int i,j,k,t,T,ans1,ans2,n,lstb,tb,lstn,tn;
    string str;

    freopen("a.in","r",stdin);
    freopen("aout.txt","w",stdout);


    scanf("%d",&T);

    for(t=1;t<=T;t++)
    {
        scanf("%d",&n);
        lstb=lstn=1;
        tb=tn=0;

        for(i=0;i<n;i++)
        {
             cin>>str>>k;

             if(str=="B")
             {
                 tb+=abs(k-lstb)+1;
                 lstb=k;

                 tb=max(tb,tn+1);
             }

             else
             {
                 tn+=abs(k-lstn)+1;
                 lstn=k;

                 tn=max(tn,tb+1);
            }
        }



        printf("Case #%d: %d\n",t,max(tn,tb));
    }

    return 0;
}

