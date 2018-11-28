#include<cstdio>
#include<algorithm>
#define min(a,b) (a < b) ? (a) : (b)
#define max(a,b) (a > b) ? (a) : (b)
typedef double lint;
using namespace std;
lint v[500];
lint p[500];
lint c,d;
bool validate( lint mid)
{
    int i;
    lint prev;
    prev=p[0]-mid + ((v[0]-1)*d);
    //printf("%lf\n",prev);
    //printf("%lf\n",p[0]+mid);
    if(prev > (p[0]+mid))
    {
        //printf("here");
        return false;
    }
    for(i=1;i<c;i++)
    {
        prev+=d;
        //printf("%lf\n",p[i]);
        //printf("%lf\n",mid);
        //printf("%lf\n",2.0*mid);
        //printf("%lf\n",(v[i]-1)*d);
        lint temp=min(2.0*mid,((v[i]-1)*d));
        //printf("here1 %lf %lf\n",prev,(p[i]+mid - temp));
        if(prev > (p[i]+mid - temp))
            return false;
        prev=max(prev,p[i]-mid);
        prev+=((v[i]-1)*d);
        //printf("here 2%lf %lf\n",prev,p[i]+mid);
        if(prev > (p[i]+mid))
            return 0;
    }
    return true;

}
int main()
{
    lint j,k;
    int i,t,T;
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%lf %lf",&c,&d);
        for(i=0;i<c;i++)
        {
            scanf("%lf %lf",&p[i],&v[i]);
        }
        lint low,mid,high;
        low=0.0;
        high=1000000000001.0;
        //printf("%lf\n",high);
        bool check=false;
        for(i=1;i<c;i++)
        {
            if(v[i]>1 || (p[i]-p[i-1]<d))
            {
                check=true;
                break;
            }
        }
        //printf("check=%d\n",check);
        if(check|| v[0]>1)
        {
        while((high-low)>0.0000001)
        {
            //printf("here2");
            mid=(high+low)/2;
            //mid=2;
            //printf("%lf\n",mid);
            if(validate(mid))
                high=mid;
            else
                low=mid;
            //break;
        }
        }
        else
            high=0.0;
        printf("Case #%d: %lf\n",t,high);
    }
    return 0;
}
