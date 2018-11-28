
#include<string>
#include<iostream>
#include<sstream>
#include<set>
using namespace std;
#define ni(x) scanf("%d",&x)

int P,Q;
int lp[108], dp[108][108];

int dfs(int lt,int rt)
{
    int & res = dp[lt][rt];
    if(res != 0x0f0f0f0f) return res;
    int l_lt = (lp[lt] - lp[lt-1] - 1);
    int r_lt = (rt==Q) ? (P-lp[rt]) : (lp[lt+1] - lp[lt] - 1);

    
    if(lt == rt) 
        return (res =  l_lt+r_lt  );
    /*if(lt+1 == rt) 
        return (res = l_lt + r_lt + l_rt
                      max(lp[rt+1] - lp[rt], 0) + (lp[rt] - lp[rt-1]) +
                      min((lp[lt] - lp[lt-1]), max(lp[rt+1] - lp[rt], 0)) );
    */
    for(int p = lt; p<=rt; p++)
    {
        int cur = (rt==Q) ? (P - lp[lt-1] - 1) : (lp[rt+1]-lp[lt-1]-2);
        int lsum = (p==lt)? 0 : dfs(lt,p-1);
        int rsum = (p==rt)? 0 : dfs(p+1,rt);
        res = min(res, cur + lsum + rsum);
    }
    return res;
}

int main()
{
	
    int nks;
	ni(nks);
    //
    for(int k=1;k<=nks;k++)
    {
    	ni(P);
        ni(Q);
        for(int i=1;i<=Q;i++)
            ni(lp[i]);
    	
		memset(dp, 0x0f, sizeof(dp));

        printf("Case #%d: %d\n", k, dfs(1,Q));

	}
}
