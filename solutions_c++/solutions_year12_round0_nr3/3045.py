#include<stdio.h>
#include<string.h>

int get_dig(int x)
{
    int sum=1;
    while(x!=0){
        x/=10;
        sum*=10;
    }
    return sum;
}
int convert(int x,int m)
{
    int i=10,sum=0,tmp,pre=-1;
    //static int cnt=0;
    while(x/i!=0){
        if(x%i>=i/10){
            tmp=x/i+(x%i)*get_dig(x/i);
            if(tmp>x&&tmp<=m&&tmp!=pre){
                pre=tmp;
                sum++;
                //printf("%4d:%d--%d\n",cnt++,x,tmp);
            }
        }
        i*=10;
    }
    return sum;
}

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int cases,cnt=0,a,b;
    scanf("%d",&cases);
    while(cases--){
        scanf("%d%d",&a,&b);
        int sum=0;
        while(a<b){
            sum+=convert(a,b);
            a++;
        }
        printf("Case #%d: %d\n",++cnt,sum);
    }
    return 0;
}
