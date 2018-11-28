#include<stdio.h>

#define M 10012

int an[10002][2],n[10002][2];
bool ud[10002][2];

inline int cc(int p,int v)
{
    if(ud[p][v])return an[p][v];
    int aa,l1,l0,r1,r0,a1,a2;
    l0=cc(p*2,0);
    r0=cc(p*2+1,0);
    l1=cc(p*2,1);
    r1=cc(p*2+1,1);
    
    //fprintf(stderr,"p=%d v=%d  l0=%d l1=%d  r0=%d r1=%d\n",p,v,l0,l1,r0,r1);    
    if(v==1)
    {
        if(l1!=-1 && r1!=-1)a1=l1+r1;
        else a1=-1;
        a2=M;
        if(l1!=-1 && r1!=-1)a2<?=l1+r1;
        if(l1!=-1 && r0!=-1)a2<?=l1+r0;
        if(l0!=-1 && r1!=-1)a2<?=l0+r1;
        if(a2==M)a2=-1;
    }
    else //if(v==0)
    {
        a1=M;
        if(l0!=-1 && r0!=-1)a1<?=l0+r0;
        if(l0!=-1 && r1!=-1)a1<?=l0+r1;
        if(l1!=-1 && r0!=-1)a1<?=l1+r0;
        if(a1==M)a1=-1;
        
        if(l0!=-1 && r0!=-1)a2=l0+r0;
        else a2=-1;
    }
    ///fprintf(stderr,"a1=%d a2=%d\n",a1,a2);
    if(n[p][0]==1)
    {
        if(n[p][1]==1 && a2!=-1 && (a1==-1 || a1>a2+1))aa=a2+1;
        else aa=a1;
    }
    else //if(n[p][0]==0)
    {
        if(n[p][1]==1 && a1!=-1 && (a2==-1 || a2>a1+1))aa=a1+1;
        else aa=a2;
    }
    
    ud[p][v]=1;
    an[p][v]=aa;
    return aa;
}

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int cases,ii,i,m,v,aa;
    
    scanf("%d",&cases);
    for(ii=1;ii<=cases;ii++)
    {
        scanf("%d%d",&m,&v);
        for(i=1;i<=(m-1)/2;i++)
        {
            scanf("%d%d",&n[i][0],&n[i][1]);
            ud[i][0]=ud[i][1]=0;
        }
        for(;i<=m;i++)
        {
            scanf("%d",&n[i][0]);
            an[i][n[i][0]]=0;
            an[i][1-n[i][0]]=-1;
            ud[i][0]=ud[i][1]=1;
        }
        aa=cc(1,v);
        if(aa==-1)printf("Case #%d: IMPOSSIBLE\n",ii);
        else printf("Case #%d: %d\n",ii,aa);
    }
    
    return 0;
}
