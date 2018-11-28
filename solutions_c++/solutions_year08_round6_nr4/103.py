#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<cmath>
#include<queue>
#include<map>
#include<stack>
#include<deque>
#include<algorithm>
#include<sstream>
#include<fstream>
using namespace std;
int g1[10][10];
int g2[10][10];
int n,m;
int solve()
{
    int i,j,k;
    for(i=0;i<(1<<n);i++)
    {
        if(__builtin_popcount(i)!=m)
        continue;
        int g3[10][10];
        memset(g3,0,sizeof(g3));
        vector<int> v,v1;
        map<int,int> mp;
        for(j=0;j<n;j++)
        {
            if(i&(1<<j))v1.push_back(j);
        }
        for(j=0;j<m;j++)
        {
            v.push_back(j);
        }
        do
        {
            int flag=0;
            for(j=0;j<m;j++)
            {
                for(k=0;k<m;k++)
                {
                    if(g2[j][k]!=1)continue;
                    if(g1[v1[v[j]]][v1[v[k]]]!=1)
                    {
                        flag=1;
                        break;
                    }
                }
                if(flag==1)break;
            }
            if(flag==0)
            {
                /*for(j=0;j<m;j++)
                {
                    cout<<v[j]<<" ";
                }
                cout<<endl;
                for(j=0;j<n;j++)
                {
                    if(i&(1<<j))cout<<j<<" ";
                }
                cout<<endl;*/
                return 1;
            }
        }while(next_permutation(v.begin(),v.end()));
        
    }
    return 0;
}
        
                    
        
int main()
{
    int tes;
    int count=1;
    cin>>tes;
    while(tes--)
    {
        memset(g1,0,sizeof(g1));
        memset(g2,0,sizeof(g2));

        int i,j,k;
        cin>>n;
        for(i=0;i<n-1;i++)
        {
            cin>>j>>k;
            g1[j-1][k-1]=g1[k-1][j-1]=1;
        }
        cin>>m;
        for(i=0;i<m-1;i++)
        {
            cin>>j>>k;
            g2[j-1][k-1]=g2[k-1][j-1]=1;
        }
        int ans=solve();
        string s;
        if(ans==1)
        s="YES";
        else
        s="NO";
        cout<<"Case #"<<count<<": "<<s<<endl;
        count++;
    }
    return 0;
}
