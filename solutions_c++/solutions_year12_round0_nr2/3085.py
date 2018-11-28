#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

main()
{
    freopen("B-large.in","r",stdin);
    freopen("op.txt","w",stdout);

    int t,tc,i,n,s,p,cnt,rem,avg;
    int total[110];

    scanf("%d",&t);
    for(tc=1; tc<=t; tc++)
    {
        scanf("%d %d %d",&n,&s,&p);
        for(i=0; i<n; i++)
            scanf("%d",&total[i]);

        cnt=0;

        for(i=0; i<n; i++)
        {
            avg=(total[i]/3);
            rem=total[i]-(avg*3);

            if(rem==0)
            {
                if(avg>=p)
                    cnt++;
                else if(s>0 && avg>0 && avg+1>=p)
                {
                    cnt++;
                    s--;
                }
            }
            else if(rem==1)
            {
                if(avg+1>=p)
                    cnt++;
            }
            else if(rem==2)
            {
                if(avg+1>=p)
                    cnt++;
                else if(s>0 && avg+2>=p)
                {
                    cnt++;
                    s--;
                }
            }
        }

        printf("Case #%d: %d\n",tc,cnt);
    }

    return 0;
}
