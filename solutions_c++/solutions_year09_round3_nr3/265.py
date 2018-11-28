#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int mas[10001][10001];
int pris[128];

void read()
{
    int nt;
    int p,q;
    scanf("%d",&nt);
    for(int ii=1;ii<=nt;ii++)
    {
        memset(mas,0,sizeof(mas));
        memset(pris,0,sizeof(pris));
        scanf("%d %d",&p,&q);
        for(int i=0;i<q;i++)
        {
            scanf("%d",&pris[i]);
        }
        sort(pris,pris+q);

        for(int i=0;i<q;i++)
        {
            if(pris[i]>1)
            {
                mas[pris[i]-1][1]=1;
            }
            if(pris[i]<p)
            {
                mas[pris[i]][1]=1;
            }
        }
        int tmp;
        for(int i=2;i<p;i++)
        {
            for(int j=1;j+i<=p;j++)
            {
                for(int k=0;k<q;k++)
                {
                    if(pris[k]<j) continue;
                    if(pris[k]>j+i) break;
                    if(mas[j][i] == 0)
                    {
                        mas[j][i]=i;
                        if(pris[k]>j) mas[j][i]+=mas[j][pris[k]-j-1];
                        if(pris[k]<i+j) mas[j][i]+=mas[pris[k]+1][i+j-(pris[k]+1)];
                    }
                    else
                    {
                        tmp=0;
                        tmp=i;
                        if(pris[k]>j) tmp+=mas[j][pris[k]-j-1];
                        if(pris[k]<i+j) tmp+=mas[pris[k]+1][i+j-(pris[k]+1)];
                        mas[j][i]= min(mas[j][i],tmp);
                    }
                }
            }
        }
        printf("Case #%d: %d\n",ii,mas[1][p-1]);
    }
}

int main()
{
    read();
    return 0;
}
