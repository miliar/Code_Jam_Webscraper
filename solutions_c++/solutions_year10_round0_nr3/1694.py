#include <iostream>
#include <cstring>
using namespace std;
int t,r,k,n;
int g[1002];
int flag[1002];
struct SS
{
    int val;
    int id;
}stack[1002];
int stack_tp;
__int64 ans;
void solve(int a,int b)
{
    int i,tmp,dd,ff,ee;
    __int64  sum1,sum2;
    tmp = r - a;
    for(i=0;i<stack_tp;i++)
    {
        if(stack[i].id == b)
        {
            ff = i;
            break;
        }
    }
    dd = tmp/(stack_tp-ff);
    ee = tmp%(stack_tp-ff);
    sum1 = 0; sum2 = 0;
    for(i=ff;i<stack_tp;i++)
    {
        sum1 = (__int64)sum1 + stack[i].val;
        if(i<ff+ee)
            sum2 = (__int64)sum2 + stack[i].val;
    }
    ans = (__int64)sum1*dd+sum2;
    for(i=0;i<stack_tp;i++)
        ans =(__int64)ans + stack[i].val;
    return;
}
int main()
{
    int case_t;
    int sum;
    int tp,pre,cnt,i,j;
    int solve_flag;
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    while(scanf("%d",&t)!=EOF)
    {
        case_t = 1;
        while(t--)
        {
            solve_flag = 0;
            scanf("%d%d%d",&r,&k,&n);
            for(i=0;i<n;i++)
            {
                scanf("%d",&g[i]);
            }
            tp = 0;
            stack_tp = 0;
            memset(flag,0,sizeof(flag));
            for(i=0;i<r;i++)
            {
                sum = 0;
                pre = tp;
                if(flag[pre] == 1)
                {
                    solve(i,pre);
                    solve_flag = 1;
                    break;
                }
                cnt = 0;
                while(sum <= k)
                {
                    cnt++;
                    sum += g[tp];
                    if(sum > k)
                    {
                        sum -= g[tp];
                        stack[stack_tp].val = sum;
                        stack[stack_tp].id = pre;
                        flag[pre] = 1;
                        stack_tp++;
                        sum = 0;
                        pre = tp;
                        break;
                    }
                    if(cnt == n)
                    {
                       stack[stack_tp].val = sum;
                       stack[stack_tp].id = pre;
                       flag[pre] = 1;
                       stack_tp++;
                       sum = 0;
                       pre = tp;
                       break;
                    }
                    tp++;
                    if(tp == n)
                        tp = 0 ;
                }
            }
            printf("Case #%d: ",case_t++);
            if(solve_flag == 1){
                printf("%I64d\n",ans);
                }
            else
            {
            ans = 0;
            for(i=0;i<stack_tp;i++)
                    ans = (__int64)ans + stack[i].val;
            printf("%I64d\n",ans);
            }
        }
    }
    return 0;
}
