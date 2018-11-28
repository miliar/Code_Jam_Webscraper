#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int test=0;
    int n=0,s=0,p=0,i=0;
    int count=0,ans=0,suprise=0;
    int t[101];
    cin>>test;
    while(test--)
    {
        ans=0,suprise=0;
        cin>>n>>s>>p;
        for(i=0;i<n;i++)
        cin>>t[i];
        for(i=0;i<n;i++)
        {
            if(t[i]>=3*p)
            ans++;
            else if((t[i]==3*p-1)&&(p>=1))
            ans++;
            else if((t[i]==3*p-2)&&(p>=1))
            ans++;
            else if((t[i]==3*p-3)&&(p>=2))
            {
            ans++;
            suprise++;
            }
            else if((t[i]==3*p-4)&&(p>=2))
            {
            ans++;
            suprise++;
            }
        }
        if((suprise-s)>0)
        ans=ans-(suprise-s);
        cout<<"Case #"<<++count<<": "<<ans<<endl;
    }

return 0;
}
