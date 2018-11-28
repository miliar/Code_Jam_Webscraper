#include <stdio.h>
#include <string.h>
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++)
    {
        int a,b;
        scanf("%d%d",&a,&b);
        int ans=0;
        for (int i=a;i<=b;i++)
        {
            int num=i;
            int tnum=num;
            int cnt=0;
            while (num!=0) num/=10,cnt++;
            num=tnum;
            int wei=1;
            for (int j=0;j<cnt-1;j++)
                wei=wei*10;
            do
            {
                int tpos=tnum%10;
                int tnum2=(tnum-(tnum%10))/10;
                tnum=tpos*wei+tnum2;
                if (tpos!=0&&tnum>num&&tnum<=b) ans++;
            }while (tnum!=num);
        }
        printf("Case #%d: %d\n",ii,ans);
    }
    return 0;
}
