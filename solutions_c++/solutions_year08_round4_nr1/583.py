#include<iostream>
using namespace std;
int g[10005],c[10005],va[10005];
int f0[10005],f1[10005]; 
int main()
{
    int casen,m,v;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout); 
    scanf("%d",&casen);
    for (int casei=1;casei<=casen;casei++)
    {
        scanf("%d%d",&m,&v);
        for (int i=1;i<=(m-1)/2;i++)
          scanf("%d%d",&g[i],&c[i]); 
        for (int i=(m-1)/2+1;i<=m;i++)
        {
            scanf("%d",&va[i]);
            if (va[i]==1)
            {
                         f1[i]=0;
                         f0[i]=20000;
            }
            else
            {
                f1[i]=20000;
                f0[i]=0;
            }
        }
        for (int i=(m-1)/2;i>=1;i--)
        {
            f1[i]=20000;
            f0[i]=20000; 
            if (g[i]==1)
            {
                        if (f1[i*2]+f1[i*2+1]<f1[i])f1[i]=f1[i*2]+f1[i*2+1];
                        if (f1[i*2]+f0[i*2+1]<f0[i])f0[i]=f1[i*2]+f0[i*2+1];
                        if (f0[i*2]+f1[i*2+1]<f0[i])f0[i]=f0[i*2]+f1[i*2+1];
                        if (f0[i*2]+f0[i*2+1]<f0[i])f0[i]=f0[i*2]+f0[i*2+1]; 
            }
            else
            {
                if (f0[i*2]+f0[i*2+1]<f0[i])f0[i]=f0[i*2]+f0[i*2+1];
                if (f1[i*2]+f0[i*2+1]<f1[i])f1[i]=f1[i*2]+f0[i*2+1];
                if (f0[i*2]+f1[i*2+1]<f1[i])f1[i]=f0[i*2]+f1[i*2+1];
                if (f1[i*2]+f1[i*2+1]<f1[i])f1[i]=f1[i*2]+f1[i*2+1]; 
            }
            if (c[i]==1)
            {
                        if (g[i]==1)
                        {
                                    if (f0[i*2]+f0[i*2+1]+1<f0[i])f0[i]=f0[i*2]+f0[i*2+1]+1;
                                    if (f1[i*2]+f0[i*2+1]+1<f1[i])f1[i]=f1[i*2]+f0[i*2+1]+1;
                                    if (f0[i*2]+f1[i*2+1]+1<f1[i])f1[i]=f0[i*2]+f1[i*2+1]+1;
                                    if (f1[i*2]+f1[i*2+1]+1<f1[i])f1[i]=f1[i*2]+f1[i*2+1]+1;
                        }
                        else
                        {
                            if (f1[i*2]+f1[i*2+1]+1<f1[i])f1[i]=f1[i*2]+f1[i*2+1]+1;
                            if (f1[i*2]+f0[i*2+1]+1<f0[i])f0[i]=f1[i*2]+f0[i*2+1]+1;
                            if (f0[i*2]+f1[i*2+1]+1<f0[i])f0[i]=f0[i*2]+f1[i*2+1]+1;
                            if (f0[i*2]+f0[i*2+1]+1<f0[i])f0[i]=f0[i*2]+f0[i*2+1]+1;
                        }
            }
        }
        printf("Case #%d: ",casei);
        if(v==1)
        {
                if (f1[1]==20000)printf("IMPOSSIBLE\n");
                else printf("%d\n",f1[1]);
        }
        else
        {
            if (f0[1]==20000)printf("IMPOSSIBLE\n");
            else printf("%d\n",f0[1]);
        }
    }
    return 0;
} 
