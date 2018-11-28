#include<stdio.h>

int main()
{
    int t;
    int n;
    int o[105][2];
    int b[105][2];
    int ro,rb;
    int oc,bc;
    int oc2,bc2;
    char h[2];
    int ct;
    int te1,te2;
    
    freopen("xxx2.in","r",stdin);
    freopen("xxx2.out","w",stdout);
    
    scanf("%d",&t);
    
    for(int r=1;r<=t;r++)
    {
        ro=1;
        rb=1;
        oc=0;
        oc2=0;
        bc=0;
        bc2=0;
        ct=0;
        
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
        {
            scanf("%s",&h);
            if(h[0]=='O')
            {
                scanf("%d",&o[oc][0]);
                o[oc][1]=i;
                oc++;
            }
            if(h[0]=='B')
            {
                scanf("%d",&b[bc][0]);
                b[bc][1]=i;
                bc++;
            }
        }
        
        for(int i=1;i<=n;i++)
        {
            if(b[bc2][1]==i && bc2<bc)
            {
                te1=b[bc2][0]-rb;
                te2=o[oc2][0]-ro;
                
                if(te1<0)te1*=-1;
                if(te2<0)te2*=-1;
                
                te1+=1;
                
                if(te1<te2)
                {
                    if(o[oc2][0]<ro)ro-=te1;
                    else ro+=te1;
                }
                else
                {
                    ro=o[oc2][0];
                }
                
                ct+=te1;
                rb=b[bc2][0];
                bc2++;
            }
            else if(o[oc2][1]==i && oc2<oc)
            {
                te1=o[oc2][0]-ro;
                te2=b[bc2][0]-rb;
                
                if(te1<0)te1*=-1;
                if(te2<0)te2*=-1;
                
                te1+=1;
                
                if(te1<te2)
                {
                    if(b[bc2][0]<rb)rb-=te1;
                    else rb+=te1;
                }
                else
                {
                    rb=b[bc2][0];
                }
                
                ct+=te1;
                ro=o[oc2][0];
                oc2++; 
            }
           
        }
        
        printf("Case #%d: %d\n",r,ct);
    }

}
