//prob2
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
long long dist(int x0,int y0,int x1,int y1)
{
    return (long long)abs(x0-x1)*(long long)abs(x0-x1)+(long long)abs(y0-y1)*(long long)abs(y0-y1);
}
int main()
{
    int tes;
    cin>>tes;
    int count=1;
    while(tes--)
    {
        long long n,m,a;
        cin>>n>>m>>a;
        int i,j,k,l;
        int flag=0;
        for(i=0;i<=n;i++)
        {
            for(j=0;j<=m;j++)
            {
                for(k=0;k<=n;k++)
                {
                    for(l=0;l<=m;l++)
                    {
                        long long a1,a2,a3,a4;
                        a1=(k-0)*(j-0);
                        a2=(i-0)*(l-0);
                        long long A=abs(a1-a2);
                        if(A==a)
                        {
                            cout<<"Case #"<<count<<": "<<0<<" "<<0<<" "<<i<<" "<<j<<" "<<k<<" "<<l<<endl;
                            flag=1;
                            goto lbl;
                        }
                    }
                }
            }
        }
        lbl:
            if(flag==0)
            cout<<"Case #"<<count<<": "<<"IMPOSSIBLE"<<endl;
            count++;
    
    }
    return 0;
}
                        
