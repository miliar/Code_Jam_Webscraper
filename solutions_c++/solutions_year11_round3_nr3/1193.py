#include<iostream>
using namespace std;
int main()
{
    int i,t,n,l,h,player[100],j,tcase=1;
    cin>>t;
    while(tcase<=t)
    {
        cin>>n>>l>>h;
        for(i=0;i<n;i++)
        cin>>player[i];
        for(i=l;i<=h;i++)
        {
            for(j=0;j<n;j++)
            {
                if((i%player[j]==0) || (player[j]%i==0))
                continue;
                else
                break;
            }
            if(j==n)
            break;
        }
        cout<<"Case #"<<tcase<<": ";
        if(i<=h)
        cout<<i<<endl;
        else
        cout<<"NO"<<endl;
        tcase++;
    }

}
