#include<iostream>
#include<vector>
#include<string>
#include<boost/lexical_cast.hpp>
using namespace std;

int main()
{
    int N,S,Q;
    string str;
    getline(cin,str);
    N = boost::lexical_cast<int>(str.substr(0,str.size()));
    for(int n=0;n < N;++n)
    {
        vector<string> engine;
        vector<string> queries;
        getline(cin,str);
        S = boost::lexical_cast<int>(str.substr(0,str.size()));
        for(int s=0;s<S;++s)
        {
            getline(cin,str);
            engine.push_back(str);
        }
        getline(cin,str);
        Q = boost::lexical_cast<int>(str.substr(0,str.size()));
        for(int q=0;q<Q;++q)
        {
            string str;
            getline(cin,str);
            queries.push_back(str);
        }
        uint32_t dp[Q+1][S];

        for(int i=0;i<=Q;++i)for(int j=0;j<S;++j)dp[i][j] = 12345678;
        for(int q=0;q<Q;++q)
        {
            for(int s=0;s<S;++s)
            {
                for(int s_=0;s_<S;++s_)
                {//s_ -> s
                    if(q==0)dp[q][s_]=0;
                    if(s==s_)
                    {
                        //if(queries[q]!=engine[s_])//nofind
                        if(queries[q].find(engine[s])==queries[q].npos)
                            dp[q+1][s] = min(dp[q+1][s],dp[q][s_]);
                    }
                    else dp[q+1][s] = min(dp[q+1][s],dp[q][s_]+1);
                }
            }
        }
        uint32_t ans = 12345678;

        for(int s=0;s<S;++s)
        {            
            ans = min(ans,dp[Q][s]);
        }
        printf("Case #%d: %u\n",n+1,ans==12345678?0:ans);
    }
}
