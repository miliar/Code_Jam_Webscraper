#include <stdio.h>
#include <string.h>

bool tag[2000003]={0};
int gao(int a,int b)
{
    int ans,num[10],len,min,max,tmp,j,yy,sum=0,bit;
    if(a == b)
        return 0;
    int i;
    ans  = 0;
    for(i=a;i<=b;i++)
    if(!tag[i]){
        sum = 1;
        len  = 0;
        tmp = i;
        while(tmp)
        {
            num[len++] = tmp%10;
            tmp /= 10;
        }

        for(yy=1;yy<len;yy++)
        {
            tmp = 0;
            if(num[yy-1]>=num[len-1])
            for(j=0,bit=1;j<len;j++,bit *= 10)
                tmp += bit*num[(yy+j)%len];
            if(tmp>i&&tmp<=b){
                sum++;
                tag[tmp] = true;
            }
        }
        ans += sum*(sum-1)/2;
    }
    return ans;
}

int main()
{
    int t,cas=1,a,b,i;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        memset(tag,0,sizeof(tag));
        scanf("%d%d",&a,&b);
        printf("Case #%d: %d\n",i,gao(a,b));
    }
    return 0;
}
