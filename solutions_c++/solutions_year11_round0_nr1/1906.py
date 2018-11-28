#include <iostream>
#include <string>
#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <vector>

using namespace std;

int Orange[300],Blue[300],store[300],now[300];

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);

    int i,j,n,test,Case=1,cost,O,B,r1,r2,ind,cnt1,cnt2,cnt,diff;
    char ch;

    scanf("%d",&test);

    while(test--)
    {
        //Clear(Orange,0);
        memset(Orange,0,sizeof(Orange));
        memset(Blue,0,sizeof(Blue));

        scanf("%d",&n);
        cnt1=cnt2=cnt=0;
        for(i=0;i<n;i++)
        {
            scanf(" %c %d",&ch,&ind);
            store[i]=ind;
            if(ch=='O')
            {
                Orange[cnt1++]=ind;
                now[i]=1;
            }
            else
            {
                Blue[cnt2++]=ind;
                now[i]=0;
            }
        }
        O=B=1;
        r1=r2=0;
        cost=0;
        for(i=0;i<n;i++)
        {
            if(now[i]==1)
            {
                diff=abs(O-Orange[r1])+1;
                //printf("%d\n",diff);
                O=Orange[r1];
                r1++;
                cost+=diff;
                if(r2<cnt2)
                {
                    if(Blue[r2]>B)
                    {
                        B=min(B+diff,Blue[r2]);
                    }
                    else
                    {
                        B=max(B-diff,Blue[r2]);
                    }
                }
            }
            else
            {
                diff=abs(B-Blue[r2])+1;
                //printf("%d\n",diff);
                B=Blue[r2];
                r2++;
                cost+=diff;
                if(r1<cnt1)
                {
                    if(Orange[r1]>O)
                    {
                        O=min(O+diff,Orange[r1]);
                    }
                    else
                    {
                        O=max(O-diff,Orange[r1]);
                    }
                }
            }
        }
        printf("Case #%d: %d\n",Case++,cost);
    }

    return 0;
}
