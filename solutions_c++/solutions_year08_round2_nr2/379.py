#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<cmath>
#include<queue>
#include<stack>
#include<algorithm>

#define VI vector<int>
#define VVI vector<vector<int> >
#define PII pair<int,int> 
#define VS vector<string> 

using namespace std;
long long a,b,p;
vector<long long> primes;



long long power(long long b,long long n,long long mod)
{
    long long x,y,z;
    x=b,y=n,z=mod;
    long long ret=1;
    while(y)
    {
        if(y%2==1)
        {
            ret=(ret*x)%z;
        }
        x=(x*x)%z;
        y>>=1;
    }
    return ret;
}
bool isprimemr(long long n)
{
    if(n==2)return true;
    if(n%2==0)return false;
    if(n==1 || n==0)return false;
    long long k=6LL;
    int i,j;
    long long d=n-1;
    long long t=n-1;
    while((d&1)==0)d>>=1;
    for(i=0;i<k;i++)
    {
        long long a=rand()%(n-1)+1;
        //cout<<a<<" "<<n<<endl;
        t=d;
        long long y=power(a,t,n);
        if(y==1)continue;
        while(t!=n-1)
        {
            if(y==1 || y==n-1)
            break;
            y=(y*y)%n;
            t<<=1;
        }
        if(y!=n-1 && (t&1)==0)return false;
    }
    return true;
}

map<int,vector<int> > m;
int d[1010];
int val=0;
void dfs(int num)
{
    
    if(d[num]!=-1)return;
    d[num]=val;
    int i,j,k;
    for(i=0;i<m[num].size();i++)
    {
        for(j=i+1;j<=b;j++)
        {
            for(k=0;k<m[j].size();k++)
            {
                if(m[j][k]==m[num][i])
                dfs(j);
            }
        }
    }
}
        
int main()
{
    int tes;
    cin>>tes;
    int count=1;
    int i,j,k;
    primes.push_back(2);
    for(i=3;i<1000000;i++)
    {
        if(isprimemr(i))
        primes.push_back(i);
    }
    while(tes--)
    {
        m.clear();
        memset(d,-1,sizeof(d));
        cin>>a>>b>>p;
        int st=0;
        for(st=0;primes[st]<p;st++);
        for(i=st;i<primes.size() && primes[i]<=b;i++)
        {
            for(j=primes[i];j<=b;j+=primes[i])
            {
                if(j<a || j>b)continue;
                m[j].push_back(primes[i]);
            }
        }
        /*for(i=a;i<=b;i++)
        {
            cout<<i<<" : ";
            for(j=0;j<m[i].size();j++)
            {
                cout<<m[i][j]<<" ";
            }
            cout<<endl;
        }*/
        val=0;
        for(i=a;i<=b;i++)
        {
            if(d[i]!=-1)continue;
            dfs(i);
            val++;
        }
        cout<<"Case #"<<count<<": "<<val<<endl;
        count++;
    }
    
    return 0;
}
        
