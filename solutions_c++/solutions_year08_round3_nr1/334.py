#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
    int tc;
    cin>>tc;
    vector<int> ans;
    for(int i=0;i<tc;i++)
    {
            int p,k,l;
            cin>>p>>k>>l;
            vector<int> kp;
            int x;
            for(int j=0;j<l;j++)
            {
                    cin>>x;
                    kp.push_back(x);
            }
            sort(kp.begin(),kp.end());
            if(p*k < l)
            {
                   ans.push_back(-1);
                   continue;
            }
            int ansx=0,pr=1;
            for(int j=kp.size()-1;j>=0;j--)
            {
                    ansx+=kp[j]*pr;
                    if((kp.size()-j)%k==0)
                        pr++;
            }
            ans.push_back(ansx);
    }
    for(int i=0;i<ans.size();i++)
    {
        cout<<"Case #"<<i+1<<": ";
        if(ans[i]==-1)
            cout<<"Impossible"<<endl;
        else
            cout<<ans[i]<<endl;
    }
    return 0;
}
                    
            
