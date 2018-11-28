#include<iostream>
#include<algorithm>

using namespace std;

int main()
{
    int num;
    cin>>num;
    for(int round=1;round<=num;round++)
    {
        bool have=false;
        int ans=0;
        int n;
        cin>>n;
        int arr[n];
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }
        sort(arr,arr+n);
        for(int i=n-1;i>=0;i--)
        {
            int sp1=0,sp2=0;
            int s1=0,s2=0;
            int ls;
            for(int j=n-1;j>=i;j--)
            {
                s1^=arr[j];
                sp1+=arr[j];
                ls=j;
            }
            for(int j=ls-1;j>=0;j--)
            {
                s2^=arr[j];
                sp2+=arr[j];
            }
            if(sp1!=0&&sp2!=0&&s1==s2)
            {
                have=true;
                if(sp1>ans)
                    ans=sp1;
            }
        }
        if(have)
            cout<<"Case #"<<round<<": "<<ans<<endl;
        else
            cout<<"Case #"<<round<<": NO"<<endl;
    }
    return 0;
}
