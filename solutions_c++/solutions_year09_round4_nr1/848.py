#include <iostream>
#include <cstring>

using namespace std;

char mas[64];
int st[64];

int main()
{
    int n,k;
    scanf("%d",&n);
    int ans=0;
    for(int ii =1;ii<=n;ii++)
    {
        scanf("%d\n",&k);
        memset(st,0,sizeof(st));
        ans = 0;
        for(int i=1;i<=k;i++)
        {
            memset(mas,0,sizeof(mas));
            scanf("%s",mas);
            for(int j=k-1;j>=0;j--)
            {
                if(mas[j]=='1') {st[i] = j+1;break;}
            }
        }
        for(int j = 1;j<=k;j++)
        {
            if(st[j]>j)
            {
                for(int ij=j;ij<=k;ij++)
                {
                    if(st[ij]<=j)
                    {
                        for(int hm=ij-1;hm>=j;hm--)
                        {
                            int tmp=st[hm];
                            st[hm]=st[hm+1];
                            st[hm+1]=tmp;
                            ans++;
                        }
                        break;
                    }
                }
            }
        }
        printf("Case #%d: %d\n",ii,ans);
    }
    return 0;
}
