#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <vector>
using namespace std;

typedef long long Long;

Long der(int n)
{
    if(n<=1)return 1-n;
    return (n-1)*(der(n-1)+der(n-2));
}
Long fac(int n)
{
    if(n<=1)return 1;
    return n*fac(n-1);
}
vector<int> color;
int dfs(int u,int col,vector<int> perm)
{
    if(color[u]!=-1)return 0;
    color[u] = col;
    return 1 + dfs(perm[u],col,perm);
}
vector<int> paint(vector<int> perm)
{
    color = vector<int>(perm.size(),-1);
    vector<int> ret(1,1);
    int idx = 1;
    for(int i = 1; i < perm.size(); ++i)
        if(color[i]==-1)
            ret.push_back(dfs(i,idx++,perm));
    return ret;
}
void print(vector<int> v)
{
    cout<<"[ ";
    for(int i = 1; i < v.size(); ++i)
        cout<<v[i]<<" ";
    cout<<"]";
}
double memo[100];
bool cat[100];
double EXP(int n)
{
    if(n==1)return 0;
    if(cat[n])return memo[n];
    vector<int> perm;
    for(int i = 0; i <= n ; ++i)
        perm.push_back(i);
    double expected = 0;
    double r = 0;
    do
    {
        vector<int> p = paint(perm);
        
        //print(p);
        if(p.size() > 2)
        {
            double texp = 1;
            for(int i = 0; i < p.size(); ++i)
                texp += EXP(p[i]);
            expected += texp;
            //cout<<" "<<texp;
        }else{
            r += 1.0;
            expected += 1;
        }
        //cout<<endl;
    }while(next_permutation(perm.begin()+1,perm.end()));
    //cout<<expected<<endl;
    cat[n] = true;
    return memo[n] = (expected)/(fac(n)-r);
}


int main(int argc, char** argv)
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int TC;
    cin>>TC;
    for(int tc = 1; tc<=TC;++tc)
    {
        int N;
        cin>>N;
        int S = 0;
        for(int i = 1; i <= N; ++i)
        {
            int t;cin>>t;
            if(t!=i)S++;
        }
        printf("Case #%d: %0.6lf\n",tc,double(S));
    }
    return 0;
}



/* 
 * File:   D.cpp
 * Author: Carlos
 *
 * Created on May 7, 2011, 1:21 AM
 */

