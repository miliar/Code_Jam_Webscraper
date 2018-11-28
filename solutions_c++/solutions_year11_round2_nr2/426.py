#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;

int i,j,k,t,n,c,d;
struct points
{
    int p,v;
}point[202];
double maxx;

double test(int i,int j)
{
    double temp=double(point[j].p-point[i].p);
    int k,totalv=0;
    for(k=i;k<=j;k++)
        totalv+=point[k].v;
    return max(0.0,((double(totalv-1)*double(d)-temp)*0.5));
}

bool cmp(points a,points b)
{
    return a.p<b.p;
}

int main()
{
    freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        maxx=0;
        scanf("%d%d",&c,&d);
        for(i=1;i<=c;i++)
            scanf("%d%d",&point[i].p,&point[i].v);
        sort(point+1,point+1+c,cmp);
        for(i=1;i<c;i++)
        {
            for(j=i+1;j<=c;j++)
            {
                double temp=test(i,j);
                //printf("%d %d %.8lf\n",i,j,temp);
                if(maxx<temp)
                    maxx=temp;
                if(point[i].v>1)
                    maxx=max(maxx,(double(point[i].v-1)*double(d)*0.5));
            }
        }
        maxx=max(maxx,(double(point[c].v-1)*double(d)*0.5));
        
        printf("Case #%d: %.8lf\n",k,maxx);
        
    }
    
    return 0;
}
