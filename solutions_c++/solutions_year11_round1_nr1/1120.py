#include<iostream>
#include<cmath>
#include<cstdio>

using namespace std;
int main()
{
    float f;
    int d,g;
    long long n,i;
    int t;
    cin>>t;
    int counter=0;
    while(t>0)
    {
        counter++;
        cin>>n>>d>>g;
        int wins[10];
        int losses[10];
        int p=0;
        for(i=1;i<=n;i++)
        {
                int winss=d*i;
                if(winss%100==0)
                {    
                        p++;
                        break;
                }
        }
        string ans;
        if(p==0||(d!=100&&g==100)||(d!=0&&g==0))
            ans= "Broken";
        else
            ans= "Possible";
        cout<<"Case #"<<counter<<": "<<ans<<endl;
        t--;
    }
}
            
