#include <iostream>
#include <queue>
using namespace std;
__int64 sss[10005];
int wz[10005];
int main()
{
    //freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
    int T,R,k,N,cas=0,i,j,M;
    scanf("%d",&T);
    while(T--)
    {
        cas++;
        scanf("%d%d%d",&R,&k,&N);
        queue <int> Q;
        __int64 sum=0;
        for(i=1;i<=N;i++)
        {
            scanf("%d",&M);
            sum+=M;
            Q.push(M);
        }
        if(sum<=k)
        {
            printf("Case #%d: %I64d\n",cas,sum*R);
            continue;
        }
        sum=0;
        int r=R,cnt=1,u,v;
        wz[1]=1;sss[1]=0;
        bool flag=0;
        while(1)
        {
            __int64 s=0;
            for(i=1;;i++)
            {
                if(s+Q.front()>k) break;
                int temp=Q.front();
                s+=temp;
                Q.pop();
                Q.push(temp);

            }
            cnt++;i-=2;
            //cout<<i<<endl;
            wz[cnt]=(wz[cnt-1]+i)%N+1;
            //printf("WZ[%d]=%d\n",cnt,wz[cnt]);
            //printf("wa[%d]=%d\n",cnt,wz[cnt]);
            for(j=1;j<cnt;j++)
            {
                if(wz[j]==wz[cnt])
                {u=j;v=cnt-j;flag=1;break;}
            }
            sum+=s;
            sss[cnt]=sum;
            if(flag) break;
        }
        //for(i=1;i<=5;i++) cout<<sss[i]<<endl;
        //cout<<u<<" "<<v<<endl;
        sss[0]=0;
        __int64 res=sss[u];R-=(u-1);
        res+=R/v*(sss[u+v]-sss[u]);R%=v;
        res+=sss[u+R]-sss[u];
        printf("Case #%d: %I64d\n",cas,res);
    }
    return 0;
}

