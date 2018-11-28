/**************************************
HNL Theme pack - small
**************************************/
#include<iostream>
#include<vector>
#include<conio.h>

using namespace std;

int r,k,n;
vector<int> v;
vector<int> ride;
vector<int>::iterator ite;

int main(int argc,char** argv)
{
    int runs;
    int temp;
    int money;
    
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);
    
    cin>>runs;
    temp=0;
    money=0;
    for(int i=0;i<runs;i++)
    {
        cin>>r>>k>>n;
        v.clear();
        
        for(int j=0;j<n;j++)
        {
            cin>>temp;
            v.push_back(temp);
        }
        
        money=0;
        temp=0;
        
        ride.clear();
        for(int j=0;j<r;j++)
        {
            temp=0;
            ite=v.begin();
            ride.clear();
            int m=0;
            while(temp<=k && m<v.size())
            {
                temp+=*ite;
                ride.push_back(*ite);
                ite++;
                
                m++;
            }
            if(temp>k)
            {
                temp-=ride[ride.size()-1];
                ride.pop_back();
                ite--;
            }
            v.erase(v.begin(),ite);
            
            money+=temp;
            for(int index=0;index<ride.size();index++)
                v.push_back(ride[index]);
        }
        
        cout<<"Case #"<<i+1<<": "<<money;
        if(i!=runs-1)
            cout<<"\n";
    }
    
    return 0;
}
