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

int main()
{
    int tes;
    cin>>tes;
    int count=1;
    while(tes--)
    {
        map<PII,int> mp;
        long long n,a,b,c,d,x,y,m;
        cin>>n>>a>>b>>c>>d>>x>>y>>m;
        vector<long long> X,Y;
        X.push_back(x);
        Y.push_back(y);
        int i,j,k;
        mp[make_pair(3*x,3*y)]=1;
        for(i=0;i<n-1;i++)
        {
            x=(a*x+b)%m;
            y=(c*y+d)%m;
            mp[make_pair(3*x,3*y)]=1;
            X.push_back(x);
            Y.push_back(y);
        }
        long long val=0;
        /*for(i=0;i<n;i++)
        {
            cout<<X[i]<<" "<<Y[i]<<endl;
        }*/
        for(i=0;i<n;i++)
        {
            for(j=i+1;j<n;j++)
            {
                for(k=j+1;k<n;k++)
                {
                    //if(mp.count(make_pair(X[i]+X[j]+X[k],Y[i]+Y[j]+Y[k]))!=0)
                    if(((X[i]+X[j]+X[k])%3==0) && ((Y[i]+Y[j]+Y[k])%3==0))
                    val++;
                }
            }
        }
        cout<<"Case #"<<count<<": "<<val<<endl;
        count++;
    }
    return 0;
}
