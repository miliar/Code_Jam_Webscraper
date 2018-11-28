#include <iostream>
#include <vector>
using namespace std;
const int MAX=(1<<30);
int P;
int cnt[2048];
int dfs(int beg,vector <int> num)
{
    bool have=true;
    for (int i=0;i<num.size()&&have;i++)
    {
        if (num[i]==0)
            have=false;
    }
    int res=MAX;
    vector <int> t1;
    if (!have)
    {
        t1.clear();
        res=1;
        if (num.size()>2)
        {
            for (int i=0;i<num.size()>>1;i++)
            {
                t1.push_back(num[i]);
            }
            res+=dfs(beg,t1);
            t1.clear();
            for (int i=num.size()>>1;i<num.size();i++)
            {
                t1.push_back(num[i]);
            }
            res+=dfs(beg+num.size()>>1,t1);
        }
    }
    else
    {
        if (num.size()==2)
            res=0;
        else
        {
            t1.clear();
            int tmp=1;
            for (int i=0;i<num.size()>>1;i++)
            {
                t1.push_back(num[i]);
            }
            tmp+=dfs(beg,t1);
            t1.clear();
            for (int i=num.size()>>1;i<num.size();i++)
            {
                t1.push_back(num[i]);
            }
            tmp+=dfs(beg+num.size()>>1,t1);
            res=min(res,tmp);
            t1.clear();
            tmp=0;
            for (int i=0;i<num.size()>>1;i++)
            {
                t1.push_back(num[i]-1);
            }
            tmp+=dfs(beg,t1);
            t1.clear();
            for (int i=num.size()>>1;i<num.size();i++)
            {
                t1.push_back(num[i]-1);
            }
            tmp+=dfs(beg+num.size()>>1,t1);
            res=min(res,tmp);
        }
    }
    //printf("%d %d %d:",beg,num.size(),res);
   // for(int i=0;i<num.size();i++)
    //{
     //   printf("%d ",num[i]);
    //}
    //putchar('\n');
    return res;
}
int main()
{
    freopen("b1.txt","r",stdin);
    freopen("b1.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        scanf("%d",&P);
        vector <int> res;
        res.clear();
        for (int i=0;i<(1<<P);i++)
        {
            scanf("%d",&cnt[i]);
            res.push_back(cnt[i]);
        }
        for (int i=0;i<(1<<P)-1;i++)
            scanf("%*d");
        int ans=dfs(0,res);
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
