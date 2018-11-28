#include<stdio.h>
#include<string.h>
#include<string>
#include<iostream>
#include<vector>
using namespace std;
int main (void)
{
    int i,j,k;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int tcase,ac;
    cin>>tcase;
    for (ac=0;ac<tcase;ac++)
    {
        int n,s,t;
        int r=0;
        int cerc=0;
        cin>>n>>s>>t;
        int a1;
        for(i=0;i<n;i++)
        {
            cin>>a1;
            if(a1%3==0)
            {
                if(a1/3>=t)
                    r++;
                else if (a1/3==t-1&&a1>0)
                    cerc++;
            }
            else if (a1%3==1)
            {
                if(a1/3>=t-1)
                    r++;
            }
            else
            {
                if(a1/3>=t-1)
                    r++;
                else if(a1/3==t-2)
                    cerc++;
            }

        }
     //   cout<<cerc<<" "<<r<<endl;
        cout<<"Case #"<<ac+1<<": "<<r+min(cerc,s)<<endl;
    }
}
