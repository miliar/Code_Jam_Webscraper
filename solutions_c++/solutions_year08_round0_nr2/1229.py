#include <stdio.h>

long ans1,ans2,sth1[102],sth2[102],stmin1[102],stmin2[102],fh1[102],fh2[102],fmin1[102],fmin2[102];
long k,t,time,j,tn,na,nb;
char start[10],finish[10],c;
bool fix[102],fix2[102];
void swap(long *r1,long *r2)
{long r3;
 r3=*r1; *r1=*r2; *r2=r3;
}
void sort1()
{long o,p;
 for(o=0;o<na;o++)
 for(p=0;p<na-1;p++)
 if (sth1[p]>sth1[p+1]) {swap(&sth1[p],&sth1[p+1]); swap(&stmin1[p],&stmin1[p+1]);} else
 if ((sth1[p]==sth1[p+1])&&(stmin1[p]>stmin1[p+1])) {swap(&sth1[p],&sth1[p+1]); swap(&stmin1[p],&stmin1[p+1]);}
}
void sort2()
{long o,p;
 for(o=0;o<nb;o++)
 for(p=0;p<nb-1;p++)
 if (sth2[p]>sth2[p+1]) {swap(&sth2[p],&sth2[p+1]); swap(&stmin2[p],&stmin2[p+1]);}else
 if ((sth2[p]==sth2[p+1])&&(stmin2[p]>stmin2[p+1])) {swap(&sth2[p],&sth2[p+1]); swap(&stmin2[p],&stmin2[p+1]);}
}
main()
{
 freopen("sec.in","r",stdin);
 freopen("sec.out","w",stdout);
 scanf("%d\n",&tn);
 for(t=0;t<tn;t++)
 {
    scanf("%d\n",&time);
    scanf("%d%d\n",&na,&nb);
    for(k=0;k<na;k++)
    {
       scanf("%s",&start); scanf("%s",&finish);
       sscanf(start,"%d%c%d",&sth1[k],&c,&stmin1[k]);
       sscanf(finish,"%d%c%d",&fh1[k],&c,&fmin1[k]);
    }
    for(k=0;k<nb;k++)
    {
       scanf("%s",&start); scanf("%s",&finish);
       sscanf(start,"%d%c%d",&sth2[k],&c,&stmin2[k]);
       sscanf(finish,"%d%c%d",&fh2[k],&c,&fmin2[k]);
    }
    sort1(); sort2();
    for(k=0;k<nb;k++) fix[k]=false;
    for(k=0;k<na;k++) fix2[k]=false;
    ans1=na; ans2=nb;
    for(k=0;k<na;k++)
    for(j=0;j<nb;j++)
    if ((sth1[k]*60+stmin1[k]>=fh2[j]*60+fmin2[j]+time)&&(!fix[j])) {ans1--; fix[j]=true; break;}
    for(k=0;k<nb;k++)
    for(j=0;j<na;j++)
    if ((sth2[k]*60+stmin2[k]>=fh1[j]*60+fmin1[j]+time)&&(!fix2[j])) {ans2--; fix2[j]=true; break;}
    printf("Case #%d: ",t+1); printf("%d %d\n",ans1,ans2);
 }
}
