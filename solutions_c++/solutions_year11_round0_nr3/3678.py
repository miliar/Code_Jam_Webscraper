#include<iostream>
#include<vector>
using namespace std;

int calc(vector<int>,int,int,int,int,int);

int main()
{
    int T;
    cin>>T;
    
    for(int c=1;c<=T;c++)
    {
        int N;
        vector<int> C;
        int val,sum=0,tot_xor=0;
        int min=1000001;
        
        cin>>N;
        for(int i=0;i<N;i++)
        {
            cin>>val;
            C.push_back(val);
            if(val<min)
                min=val;
            sum+=val;
            tot_xor^=val;
        }
        
        int res=0;
        if(!tot_xor)
        {
            res=sum-min;
        }
        
        cout<<"Case #"<<c<<": ";
        if(res)
            cout<<res<<endl;
        else
            cout<<"NO\n";
    }
}
