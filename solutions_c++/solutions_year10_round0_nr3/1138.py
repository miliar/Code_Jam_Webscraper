#include<iostream>
#include<queue>
#include<map>
#include<algorithm>
using namespace std;
int g[1009];
long long cst[1009];
map<int,int>mp;
queue<int>q1,q2;
int main()
{

    int t,i,j,k,n,m,r,a;
    //freopen("C-small.in","r",stdin);
    //freopen("C.smallout","w",stdout);
    freopen("C-large.in","r",stdin);
    freopen("Cout.txt","w",stdout);
    cin>>t;
    for(a=1;a<=t;a++)
    {
        cin>>r>>k>>n;
        for(j=0;j<n;j++)
            cin>>g[j];


        mp.clear();

        while(!q1.empty())
            q1.pop();
        while(!q2.empty())
            q2.pop();
        for(i=0;i<n;i++)
            q1.push(i);
        int p,start,end,looplen;
        long long loopcost,totalcost;

        for(i=1;i<=r;i++)
        {
            p=0;

            while((!q1.empty()) && (p+g[q1.front()]<=k) )
            {
                p+=g[q1.front()];
                q2.push(q1.front());
                q1.pop();
            }
            cst[i]=cst[i-1]+p;
            if(!mp[q2.front()])
                mp[q2.front()]=i;
            else
            {
                start=mp[q2.front()];
                end=i;
                looplen=end-start;
                loopcost=cst[end]-cst[start];
                break;
            }
            while(!q2.empty())
            {
                q1.push(q2.front());
               // cout<<g[q2.front()]<<" ";
                q2.pop();
            }
            //cout<<endl;
        }
        if(i<r)
        {
            totalcost=cst[i]+((r-i)/looplen)*loopcost + cst[start+((r-i)%looplen)]-cst[start];
        }
        else
            totalcost=cst[r];
        cout<<"Case #"<<a<<": "<<totalcost<<endl;
    }
    return 0;
}
