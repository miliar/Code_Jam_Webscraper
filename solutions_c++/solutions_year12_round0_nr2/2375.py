#include<stdio.h>
#include<stdlib.h>

using namespace std;

struct score
{
    int a,b,c;
    score(){}
    score(int aa,int bb,int cc)
    {
        a = aa;
        b = bb;
        c = cc;
    }
};

score norm[35],sur[35];

int main()
{
    int i,j,k;
    for(i=0;i<=10;i++)
        for(j=i;j<=i+2 && j<=10;j++)
            for(k=j;k<=i+2 && k<=10;k++)
            {
                if(j-i==2 || k-j==2 || k-i==2)
                    sur[i+j+k] = score(i,j,k);
                else
                    norm[i+j+k] = score(i,j,k);
            }
    /*for(i=2;i<=28;i++)
    {
        printf("-----Triplet %d-----\n",i);
        printf("%d %d %d : %d %d %d\n",norm[i].a,norm[i].b,norm[i].c,sur[i].a,sur[i].b,sur[i].c);
    }*/
    freopen("B-large.in","rt",stdin);
    freopen("B-large.out","wt",stdout);
    int t,n,s,p,result,temp,data;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        result = 0;
        temp = 0;
        scanf("%d %d %d",&n,&s,&p);
        for(j=1;j<=n;j++)
        {
            scanf("%d",&data);
            if(norm[data].c >= p)
                result++;
            else if(sur[data].c >= p)
                temp++;
        }
        if(s < temp)
            temp = s;
        printf("Case #%d: %d\n",i,result+temp);
    }
    return 0;
}
