/*
TASK: Bot Trust
LANG: C++
*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;
int N,M,T;
int seq[127][2];    // 0 ty [O1/B2] 1 po
int o[127],b[127];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k;
    int idx1=1,idx2=1;
    char str[5];
    scanf("%d",&T);
    for(int tt=1;tt<=T;tt++)
    {
        scanf("%d",&N);
        idx1=1;
        idx2=1;
        for(i=1;i<=N;i++)
        {
            scanf("%s%d",str,&k);
            if(str[0]=='O')
            {
                seq[i][0]=1;
                seq[i][1]=k;
                o[idx1]=k;
                idx1++;
            }
            else    // B
            {
                seq[i][0]=2;
                seq[i][1]=k;
                b[idx2]=k;
                idx2++;
            }
        }
        int ty=1;
        int ans=0,i=1;
        int poo=1,pob=1;
        int id1=1,id2=1;    // o b
        bool pe=true;
        while(true)
        {
//            printf("%d %d\n",poo,pob);
            if(ty>N)    break;
            ans++;
            pe=false;
            if(poo>o[id1])
            {
                poo--;
                if(seq[ty][0]==1)
                    pe=true;
            }
            else if(poo<o[id1])
            {
                if(seq[ty][0]==1)
                    pe=true;
                poo++;
            }
            if(pob>b[id2])
            {
                if(seq[ty][0]==2)
                    pe=true;
                pob--;
            }
            else if(pob<b[id2])
            {
                if(seq[ty][0]==2)
                    pe=true;
                pob++;
            }
            if(pe)
                continue;
            if(seq[ty][0]==1 && poo==seq[ty][1])
            {
                id1++;
                ty++;
            }
            else if(seq[ty][0]==2 && pob==seq[ty][1])
            {
                id2++;
                ty++;
            }
        }
        printf("Case #%d: %d\n",tt,ans);
    }
}
