#include<stdio.h>

int main()
{
    int c,s,p,n,ans,ss,tmp1,tmp2,k1,k2,cant;
    int* total;
    bool flag;
    scanf("%d",&c);
    for(int cc = 1 ; cc <= c ; cc++)
    {
        ans = 0; ss = 0 , cant = 0;
        scanf("%d %d %d",&n,&s,&p);
        total = new int[n];
        for(int i = 0 ; i < n ; i++) scanf("%d",&total[i]);
        for(int i = 0 ; i < n ; i++)
        {
            flag = false;
            for(int j = 10 ; j >= p ; j--)
            {
                if(j*3 == total[i] || j*3-1 == total[i] || j*3-2 == total[i])
                {
                    flag = true;
                    //printf("***%d %d***\n",j,total[i]);
                    break;
                }
            }
            if(!flag)
            {
                for(int j = 10 ; j >= p && j > 1 ; j--)
                {
                    if(j*3-3 == total[i] || j*3-4 == total[i])
                    {
                        flag = true;
                        //printf("****%d %d****\n",j,total[i]);
                        break;
                    }
                }
                if(flag) ss++;
                else cant++;
            }
        }
        ans = n-cant;
        if(ss > s) ans -= ss-s;
        printf("Case #%d: %d\n",cc,ans);
    }
    return 0;
}
