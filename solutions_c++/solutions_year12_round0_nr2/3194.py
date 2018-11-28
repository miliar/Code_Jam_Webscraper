#include<iostream>
#include<stdio.h>
#include<string>
#include<string.h>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;


int main()
{
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        int n,s,p;
        cin>>n>>s>>p;

        int ans=0;
        for(int i=0;i<n;i++)
        {
            int temp;
            cin>>temp;
            if(temp==0)
            {
                if(p==0)ans++;
                continue;
            }
            if(temp==1)
            {
                if(p<=1)ans++;
                continue;
            }
            if(temp==2)
            {
                if(p<=1)ans++;
                else if(s&&p==2){s--;ans++;}
                continue;
            }
            if(temp%3==0)
            {
                if(temp/3>=p)ans++;
                else if(s&&temp/3+1>=p){ans++;s--;}
            }
            else if(temp%3==1)
            {
                if(temp/3+1>=p)ans++;
                else if(s&&temp/3+1>=p){ans++;s--;}
            }
            else
            {
                if(temp/3+1>=p)ans++;
                else if(s&&temp/3+2>=p){ans++;s--;}
            }
        }
        printf("Case #%d: %d\n",tt,ans);
    }

    return 0;
}
