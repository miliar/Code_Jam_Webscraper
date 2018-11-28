#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  

// for size length iterator begin end push_back int char string vector stringstream

#define FOR(i,m,n) for(int i=(m);i<=(int)(n);i++)
#define rep(i,n) FOR(i,0,(n)-1)

using namespace std;


string readln()
{
    string s="";
    char buf[1000];
    cin.getline(buf,1000);
    s=buf;
    return s;
}

int main_fn()
{
    int retval=9999999;
    int s=0,q=0;
    char buf[1000];
    cin >> s;
    cin.getline(buf,1000);
    map<string,int> ses;

    rep(i,s)
    {
        string se=readln();
        ses[se]=i;
    }

    cin >> q;
    cin.getline(buf,1000);

    int dp[s][q];
    rep(i,s)
        rep(j,q)
            dp[i][j]=0;
    
    if(q==0)
        return 0;
    int queries[q];
    rep(i,q)
    {
        string se=readln();
        int senum=ses[se];
        queries[i]=senum;
        dp[senum][i]=9999999;
    }



    rep(i,s)
    {
        if(queries[0] != i)
            dp[i][0]=0;
    }


    for(int j=1;j<q;j++)
    {
        rep(i,s)
        {
            if(queries[j]==i)
                continue;
            int minc=9999999;
            rep(k,s)
            {
                if(i==k )
                {
                    if(minc > dp[i][j-1])
                        minc=dp[i][j-1];
                }
                else
                {
                    if(minc > (dp[k][j-1]+1) )
                        minc=(dp[k][j-1]+1);
                }
            }
            dp[i][j]=minc;
        }
    }
    rep(i,s)
    {
        if(retval > dp[i][q-1])
            retval=dp[i][q-1];
    }


    return retval;
}

int main()
{
    int N;
    char buf[1000];
    string s;
    cin >> N;
    cin.getline(buf,1000);
    rep(i,N)
    {
        cout << "Case #"<<i+1<<": "<<main_fn()<<"\n";
    }
} 
