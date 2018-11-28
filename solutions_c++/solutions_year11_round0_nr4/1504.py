#include<stdio.h>
#include<stdlib.h>
struct node
{
    int index;
    int value;   
}array[1100];
int data[1100];
int g[1100];
int isVisit[1100];
int index;
int sortfunc(const void *a,const void *b)
{
    node *x = (node*)a;
    node *y = (node*)b;
    return x->value - y->value; 
}
int bsearch(int l,int r,int v)
{
    int mid=(l+r)/2;
    if(array[mid].value==v)
        return mid;
    if(array[mid].value<v)
        return bsearch(mid+1,r,v);
    return bsearch(l,mid,v);   
}
int findAndCountLoop(int vertex,int root,int count)
{
    isVisit[vertex]=1;
    if(vertex==root)
        return count;
    return findAndCountLoop(g[vertex],root,count+1);
}
int main()
{
    int tcase,n,i,j,k;
    int result;
    int temp;
    freopen("D-large.in","rt",stdin);
    freopen("GoroSoft.out","wt",stdout);
    scanf("%d",&tcase);
    for(k=1;k<=tcase;k++)
    {
        scanf("%d",&n);
        for(i=1;i<=n;i++) 
        {
            scanf("%d",&data[i]);
            array[i].index=i;
            array[i].value=data[i];
        }
        for(i=1;i<=n;i++)
        {
            g[i]=0;
            isVisit[i]=0;
        }
        qsort(array+1,n,sizeof(node),sortfunc);
        for(i=1;i<=n;i++)
        {
            index=bsearch(1,n,data[i]);
            if(index!=i)
                g[i]=index;
            else
                isVisit[i]=1;
        }
        result=0;
        for(i=1;i<=n;i++)
            if(isVisit[i]==0)
            {
                temp=findAndCountLoop(g[i],i,1);
                result+=temp;
            }
        printf("Case #%d: %d.000000\n",k,result);
    }
    //system("pause");
    return 0;   
}
