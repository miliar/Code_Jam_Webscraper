#include <iostream>
using namespace std;

int q[1001], r, k, n,endp[1001];
long long sum[1001];
void init()
{
    int a=0,i,j;
    for(i=0;i!=n;++i)scanf("%d",q+i);
    for(i=0;i!=n;++i)
    {
        sum[i]=0;
        for(j=i;j!=i+n;++j){ if(sum[i]+q[j%n]<=k)sum[i]+=q[j%n]; else{ endp[i]=(j%n); break; } }
        if(j==i+n)endp[i]=0;
    }

}
long long solve()
{
    long long ret=0;
    int cpos=0;
    scanf("%d%d%d",&r,&k,&n);
    init();
    for(int i=0;i!=r;++i)
    {
        ret+=sum[cpos];
        cpos=endp[cpos];
    }
    return ret;
}
int main()
{
    int cases;
    scanf("%d",&cases);
    for(int i=0;i!=cases;++i)
    {
        printf("Case #%d: ",i+1);
        cout<<solve()<<endl;
    }
    return 0;
}
