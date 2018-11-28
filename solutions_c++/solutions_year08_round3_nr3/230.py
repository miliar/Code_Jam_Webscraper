#include<iostream>
#include<vector>
#include<string>
using namespace std;
int main()
{
    int tc;
    cin>>tc;
    vector<long long> ans;
    for(int i=0;i<tc;i++)
    {
            long long n,m,x,y,z,a;
            cin>>n>>m>>x>>y>>z;
            vector<long long> spd,avec;
            for(int j=0;j<m;j++)
            {
                cin>>a;
                avec.push_back(a);
            }
            for(int j=0;j<n;j++)
            {
                    spd.push_back(avec[j%m]);
                    avec[j%m] = ((x*avec[j%m]+y*(j+1))%z);
                    if(avec[j%m]<0)
                        avec[j%m]+=z;
            }
            vector<long long> seq;
            seq.push_back(1);
            for(int j=1;j<spd.size();j++)
            {
                seq.push_back(1);
                for(int k=j-1;k>=0;k--)
                {
                        if(spd[j]>spd[k])
                        {
                            seq[j]+=seq[k];
                            if(seq[j]>100000007)
                            {
                               seq[j]%=1000000007;                    
                               if(seq[j] < 0)
                                  seq[j]+=1000000007;
                            }  
                        }                      
                }
            }
            long long ansx=0;
            for(int j=0;j<seq.size();j++)
            {
                ansx+=seq[j];
                if(ansx>100000007)
                {
                    ansx%=1000000007;
                    if(ansx < 0)
                        ansx+=1000000007;
                }                    
            }
            ans.push_back(ansx);
    }
    for(int i=0;i<ans.size();i++)
    {
        cout<<"Case #"<<i+1<<": ";
        cout<<ans[i]<<endl;
    }
    return 0;
}    
