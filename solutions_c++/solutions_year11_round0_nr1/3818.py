#include<stdio.h>


char seq[150];
int orange[150],blue[150];



int main()
{
    freopen("A-large.in","r",stdin);
    freopen("bot.out","w",stdout);
    int n,c1,c2,val,i,j,p1,p2,w,s,time,m;


    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        scanf(" %d",&m);
        c1=0;
        c2=0;
        for(j=0;j<m;j++)
        {
            scanf(" %c",&seq[j]);
            scanf(" %d",&val);
            if(seq[j]=='O') orange[c1++]=val;
            else blue[c2++]=val;
        }
        j=0;
        time=0;
        p1=1;
        p2=1;
        w=0;
        s=0;

        while(j<m)
        {
            if(seq[j]=='O')
            {
                if(p1<orange[w])
                {
                    time++;   p1++;
                }
                else if(p1>orange[w])
                {
                    time++;  p1--;
                }
                else if(p1==orange[w])
                {

                    time++;
                    w++;
                    j++;
                }

                if(p2<blue[s])   p2++;

                else if(p2>blue[s]) p2--;

            }
            else if(seq[j]=='B')
            {

                if(p2<blue[s]) { time++;  p2++;}
                else if(p2>blue[s])  {time++; p2--;}
                else if(p2==blue[s])
                {
                    time++;
                    s++;
                    j++;
                }
                if(p1<orange[w])    p1++;
                else if(p1>orange[w])   p1--;
            }
        }
        printf("Case #%d: %d\n",i+1,time);
    }
    return 0;
}



