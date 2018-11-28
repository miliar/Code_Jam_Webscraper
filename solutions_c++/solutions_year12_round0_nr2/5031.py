#include<vector>
#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,c=0;
    int n,s,p,sc;
    cin>>t;
    while(t--)
    {
        c++;
        cin>>n>>s>>p;
        vector<int> sums,surs;
        vector<int> v;
        int start=p-2;
        if(start<0&&(p-1)>=0) start=(p-1);
        else if(start<0)start=p;
        for(int i=start;i<=p+1;i++)
        {
            for(int j=0;j<2;j++) v.push_back(i);
        }
        int nnn=v.size();
        for(int ii=1;ii<(1<<(nnn));ii++)
        {
            if(__builtin_popcount(ii)!=3) continue;
            int ll=ii,mx=-1,mn=1000000000,ss=0;
            for(int h=0;ll;ll>>=1,h++)
            {
                if(!(ii&(1<<h))) continue;
                mx=max(mx,v[h]);
                mn=min(mn,v[h]);
                ss+=v[h];
            }
            if((mx-mn)<=1&&mx>=p) sums.push_back(ss);
            if(mx-mn==2&&mx>=p) surs.push_back(ss);
        }
        int cnt=0,r=0,ans;
        for(int i=0;i<n;i++)
        {
            cin>>sc;
            int k=3*p;
            if(sc>=k) cnt++;
            else
            {
                int nn=sums.size();
                bool fl=0;
                for(int i=0;i<nn;i++)
                {
                    if(sc==sums[i]) fl=1;
                }
                if(fl) {cnt++; continue;}
                nn=surs.size();
                fl=0;
                for(int i=0;i<nn;i++)
                {
                    if(sc==surs[i]) fl=1;
                }
                if(fl) {r++;}
            }
        }
        ans=cnt+min(r,s);
        cout<<"Case #"<<c<<": "<<ans<<endl;
    }
    return 0;
}
