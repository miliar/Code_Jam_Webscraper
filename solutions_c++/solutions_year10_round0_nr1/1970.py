/*
TASK: snapper
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>

int ans[10100]; //ans is 0,1 for off/on
int q[10100][3]; 

int stat[2][35]; //each switch is on or off?

int sf(const void *a, const void *b)
{
    int x = ((int*)a)[1]-((int*)b)[1];
    if(x!=0)
        return x;
    return ((int*)a)[0]-((int*)b)[0];
}

int main()
{
    int i,x,t,maxk,cur,j;
    
    scanf("%d", &t);
    
    for(x=0;x<t;x++)
    {
        scanf("%d%d", &q[x][0], &q[x][1]);
        q[x][2]=x+1;
    }
    
    qsort(&q[0],t,sizeof(q[0]),sf);
    
    maxk=q[t-1][1];
    cur = 0; //which question are we looking at
    
    for(cur=0;cur<t;cur++)
    {
        if(q[cur][1]==0)
            ans[ q[cur][2] ]=0;
        else
            break;
    }
    
    for(i=1;i<=30;i++)
        stat[0][i]=0; //start: all is off
    
    for(i=1;i<=maxk;i++)
    {
        for(j=1;j<=30;j++)
        {
            if(stat[!(i%2)][j]==0)
            {
                stat[i%2][j]=!stat[!(i%2)][j];
                break;
            }
            stat[i%2][j]=!stat[!(i%2)][j];
        }

        for(j++;j<=30;j++)
            stat[i%2][j]=stat[!(i%2)][j];
        
/*        for(j=1;j<=30;j++)
            printf("%d ", stat[i%2][j]);
        printf("\n");*/
        
//        printf("cur = %d | %d %d %d", cur, q[cur][0],q[cur][1],q[cur][2]);
        while(q[cur][1]==i) //answer current questions
        {
            for(j=1;j<= q[cur][0];j++)
                if(stat[i%2][j]==0) break;

            if(j>q[cur][0])
                ans[ q[cur][2] ]=1;
            else
                ans[ q[cur][2] ]=0;
            cur++;
        }
    }
    
    for(x=1;x<=t;x++)
    {
        printf("Case #%d: ",x);
        if(ans[x]==0)
            printf("OFF\n");
        else
            printf("ON\n");
    }    
    
//    scanf(" ");
    
    return 0;
}
