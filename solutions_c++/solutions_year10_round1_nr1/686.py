#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char map[55][55];
char rotate[55][55];
char resmap[55][55];
int T,N,K;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int  i;
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        scanf("%d %d ",&N,&K);
        //getchar();
        for(int j=0;j<N;j++)
        {
            scanf("%s",map[j]);
        }

        for(int j=0;j<N;j++)
        {
            for(int k=0;k<N;k++)
            {
                rotate[j][k] = map[N-k-1][j];
            }
        }

        for(int j=0;j<N;j++)
        {
            for(int k=0;k<N;k++) resmap[j][k]='.';
        }
/*
        for(int j=0;j<N;j++)
        {
            for(int k=0;k<N;k++)
            {
                printf("%c",rotate[j][k]);
            }
            printf("\n");
        }
*/

        for(int j=0;j<N;j++)
        {//col
            int p=N-1;
            for(int k=N-1;k>=0;k--)
            {
                if(rotate[k][j]!='.')
                {
                    resmap[p--][j]=rotate[k][j];
                }
            }
        }
/*
        for(int j=0;j<N;j++)
        {
            for(int k=0;k<N;k++)
            {
                printf("%c",resmap[j][k]);
            }
            printf("\n");
        }
*/
        //resmap
        bool rf=false,bf=false;
        for(int j=0;j<N;j++)
        {//hang
            for(int k=0;k<N;k++)
            {
                if(!bf&&resmap[j][k]=='B')
                {
                    int cnt=0;
                    for(int p=k;p<N;p++)
                    {
                        if(resmap[j][p]!='B') break;
                        cnt++;
                    }
                    if(cnt==K) bf=true;
                }//heng
                if(!bf&&resmap[j][k]=='B')
                {
                    int cnt=0;
                    for(int q=j;q<N;q++)
                    {
                        if(resmap[q][k]!='B') break;
                        cnt++;
                    }
                    if(cnt==K) bf=true;
                }//heng
                if(!bf&&resmap[j][k]=='B')
                {
                    int cnt=0;
                    int dx=1,dy=1;
                    int p=j,q=k;
                    while(p<N&&q<N&&resmap[p][q]=='B')
                    {
                        p+=dx;q+=dy;
                        cnt++;
                    }
                    if(cnt==K) bf=true;
                }//heng
                if(!bf&&resmap[j][k]=='B')
                {
                    int cnt=0;
                    int dx=1,dy=-1;
                    int p=j,q=k;
                    while(p<N&&q>=0&&resmap[p][q]=='B')
                    {
                        p+=dx;q+=dy;
                        cnt++;
                    }
                    if(cnt==K) bf=true;
                }//heng

                if(!rf&&resmap[j][k]=='R')
                {
                    int cnt=0;
                    for(int p=k;p<N;p++)
                    {
                        if(resmap[j][p]!='R') break;
                        cnt++;
                    }
                    if(cnt==K) rf=true;
                }
                if(!rf&&resmap[j][k]=='R')
                {
                    int cnt=0;
                    for(int q=j;q<N;q++)
                    {
                        if(resmap[q][k]!='R') break;
                        cnt++;
                    }
                    if(cnt==K) rf=true;
                }
                if(!rf&&resmap[j][k]=='R')
                {
                    int cnt=0;
                    int dx=1,dy=1;
                    int p=j,q=k;
                    while(p<N&&q<N&&resmap[p][q]=='R')
                    {
                        p+=dx;q+=dy;
                        cnt++;
                    }
                    if(cnt==K) rf=true;
                }
                if(!rf&&resmap[j][k]=='R')
                {
                    int cnt=0;
                    int dx=1,dy=-1;
                    int p=j,q=k;
                    while(p<N&&q>=0&&resmap[p][q]=='R')
                    {
                        p+=dx;q+=dy;
                        cnt++;
                    }
                    if(cnt==K) rf=true;
                }
            }
        }

        printf("Case #%d: ",i);
        if(rf&&bf) printf("Both\n");
        else if(!rf&&!bf) printf("Neither\n");
        else if(rf) printf("Red\n");
        else if(bf) printf("Blue\n");
    }
    return 0;
}
