#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<cmath>
#include<algorithm>
#include<sstream>
#define vi vector<int>
#define vvi vector<vector<int> >
#define pii pair<int,int> 
#define vs vector<string> 
 
using namespace std;
map<string,int> m;
int d[1000];
vs v;
vs se;
int s,q;
char buf[1000];
int dp[110][1010];
vector<int> queries;
int solve(int pos,int last)
{
    if(pos>=q)
    {
        return 0;
    }
    int &ret=dp[last][pos];
    
    if(ret!=-1)return ret;
    //cout<<"hi"<<endl;
    int i,j,k;
    ret=100000000;
    if(queries[pos]!=last)
    {
        
        ret=solve(pos+1,last);
        return ret;
    }
    for(i=0;i<s;i++)
    {
        if(i==last)continue;
        ret=min(ret,solve(pos+1,i)+1);
    }
    return ret;
}    
    
int main()
{
    int tes;
    scanf("%d\n",&tes);
    int testno=1;
    while(tes--)
    {
        memset(dp,-1,sizeof(dp));
        se.clear();
        v.clear();
        m.clear();
        queries.clear();
        memset(d,0,sizeof(d));
        int i,j,k;
        scanf("%d\n",&s);
        for(i=0;i<s;i++)
        {
            int c;
            fgets(buf,1000,stdin);
            string st(buf);
            //cout<<"this "<<st<<endl;
            se.push_back(st);
            m[st]=i;
        }
        cin>>q;
        getchar();
        if(q==0)
        {
            cout<<"Case #"<<testno<<": "<<0<<endl;
            testno++;
            continue;
        } 
        
        //cout<<q<< " this "<<endl;       
        for(i=0;i<q;i++)
        {
            int c;
            fgets(buf,1000,stdin);
            string st(buf);
            //cout<<"this "<<st<<endl;
            v.push_back(st);
            queries.push_back(m[st]);
        }
        /*for(i=0;i<q;i++)
        cout<<queries[i]<<" ";
        */
        cout<<"Case #"<<testno<<": ";
        int ret=100000000;
        for(i=0;i<s;i++)
        {
            int p;
            ret=min(ret,p=solve(0,i));
            //cout<<i<<" : "<<p<<endl;
        }
        cout<<ret<<endl;
        testno++;
    }
    return 0;
}
        
