#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <memory.h>
#include <string.h>
using namespace std;

int data[1000][2];
char str[1000][20];
int hmin,hmax;
int wmin,wmax;
bool ff[2][2];

int N,M,T;

bool judge()
{
     return hmin!=0x3f3f3f3f && hmax!=-0x3f3f3f3f && wmin!=0x3f3f3f3f &&wmax != -0x3f3f3f3f;
     }

void init()
{
     int i;
     char ss[20];
     scanf("%d",&N);
     for(i=0;i<N;i++)
     {
        scanf("%d%d%s",&data[i][0],&data[i][1],str[i]);
        if(!strcmp(str[i],"NOT"))
          scanf("%s",ss);
     }
     hmin=0x3f3f3f3f;
     hmax=-0x3f3f3f3f;
     wmin=0x3f3f3f3f;
     wmax=-0x3f3f3f3f;
     memset(ff,false,sizeof(ff));
     for(i=0;i<N;i++)
     {
         if(!strcmp(str[i],"BIRD"))
         {
             if(data[i][0]<hmin)
                hmin=data[i][0];
             if(data[i][0]>hmax)
               hmax=data[i][0];
             if(data[i][1]<wmin)
                wmin=data[i][1];
             if(data[i][1]>wmax)
                wmax=data[i][1];
         }    
     }
     //printf("%d %d %d %d\n",hmin,hmax,wmin,wmax);
     for(i=0;i<N;i++)
     {
        if(!strcmp(str[i],"NOT"))
        {
            int cnt=0;
            if((hmin !=0x3f3f3f3f &&data[i][0]< hmin) || (hmax!=-0x3f3f3f3f&&data[i][0]>hmax))
              cnt++;
            if((wmin!=0x3f3f3f3f&&data[i][1]<wmin) || (wmax!=-0x3f3f3f3f&&data[i][1]>wmax))
              cnt++;
            if(cnt==2)
               continue;
            //printf("OK\n");
            else if(cnt==1)
            {
                 if(hmin!=0x3f3f3f3f&&data[i][0]<hmin)
                   ff[0][0]=true;
                 else if(hmax!=-0x3f3f3f3f&&data[i][0]>hmax)
                   ff[0][1]=true;
                 else if(wmin!=0x3f3f3f3f&&data[i][1]<wmin)
                   ff[1][0]=true;
                 else if(wmax!=-0x3f3f3f3f&&data[i][1]>wmax)
                   ff[1][1]=true;
                   }
        }
     }
     //printf("%d %d %d %d\n",ff[0][0],ff[0][1],ff[1][0],ff[1][1]);
}

void solve()
{
     int i;
     bool kk;
     char ss[20];
     int a,b;
     scanf("%d",&M);
     for(i=0;i<M;i++)
     {
        scanf("%d%d",&a,&b);
        if(judge()&&a>=hmin && a<=hmax &&b>=wmin && b<=wmax)
           printf("BIRD\n");
        else
        {
             kk=false;
            if(hmin!=0x3f3f3f3f&&a<hmin)
              kk|=ff[0][0];
            else if(hmax!=-0x3f3f3f3f&&a>hmax)
               kk|=ff[0][1];
            else if(hmin!=0x3f3f3f3f&&b<wmin)
               kk|=ff[1][0];
            else if(hmax!=-0x3f3f3f3f&&b>wmax)
            {
               kk|=ff[1][1];
               }
        if(kk)
           printf("NOT BIRD\n");
        else
           printf("UNKNOWN\n");
           }
     }
}

int main()
{
    int i;
    //freopen("A.in","r",stdin);
    //freopen("A.txt","w",stdout);
    scanf("%d",&i);
    for(T=1;T<=i;T++)
    {
       init();
       printf("Case #%d:\n",T);
       solve();
    }
    return 0;
}




