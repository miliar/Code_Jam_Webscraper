#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int kasus,jml,coba,ar[20],a,b,aa,bb;

int main()
{
    scanf("%d",&kasus);
    for (int z=1;z<=kasus;z++)
    {
        scanf("%d",&jml);
        for (int i=1;i<=jml;i++) scanf("%d",&ar[i]);
        coba = -1;
        for (int i=0;i<(1<<jml);i++)
        {
            aa = bb = 0;
            a = b = -1;
            for (int j=1;j<=jml;j++)
            {
                if (i&(1<<(j-1)))
                {
                    (a!=-1) ? a ^= ar[j] : a=ar[j];
                    aa += ar[j];
                }
                else
                {
                    (b!=-1) ? b ^= ar[j] : b=ar[j];
                    bb += ar[j];
                }
            }
            if (a==b) coba = max(coba,max(aa,bb));
        }
        if (coba==-1) printf("Case #%d: NO\n",z);
        else printf("Case #%d: %d\n",z,coba);
    }
//    system("PAUSE");
    return 0;
}
