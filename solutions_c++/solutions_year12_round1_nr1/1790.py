#include<algorithm>
#include<cstdlib>
#include<cstdio>

#include<cstring>

using namespace std;
int main()
{
        long long int i,j,ca=0,k,l,a,b,t;
        long double tmp1,azz; 
        scanf("%lld",&t);
        while(t--)
        {       
                ca++;
                long double parr[1007]={0.0},qrr[1007]={0.0},srr[1007]={0.0};
                scanf("%lld %lld",&a,&b);
                qrr[0]=1.0;
                tmp1=b+2.0;
                for(i=1;i<=a;i++)
                {
                        scanf("%llf",&parr[i]);
                        qrr[i]=qrr[i-1]*parr[i];
                }
                srr[a+1]=qrr[a]*(b-a+1.0)+(1.0-qrr[a])*(b-a+2.0+b);
                for(i=0;i<=a;i++)
                {
                        srr[i]=qrr[i]*(a+b+1-2.0*i)+(1.0-qrr[i])*(a+2*b+2.0-2.0*i);
                        tmp1=tmp1<srr[i]?tmp1:srr[i];
                }
                printf("Case #%lld: %llf\n",ca,tmp1);
        }
        return 0;
}