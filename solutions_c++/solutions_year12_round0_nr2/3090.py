#include<iostream>
#include<string.h>
#include<string>
#include<string.h>
#include<map>
#include<stdio.h>
#include<queue>

using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int ans=0;
    int n,s,p;
    int T;
    cin>>T;
    for(int l=1;l<=T;++l)
    {
        cin>>n>>s>>p;
        //cout<<n<<" "<<s<<" "<<p<<endl;
        int k=(p-1)*3;
        ans=0;
        for(int i=1;i<=n;++i)
        {
            int itemp;
            cin>>itemp;
            //cout<<itemp<<" ";
            if(itemp>k)
            {
                ++ans;
            }else
            if(s>0&&(itemp==k||itemp==(k-1))&&itemp>1)
            {
                --s;
                ++ans;
            }
        }//cout<<endl;
        printf("Case #%d: %d\n",l,ans);
    }

    return 0;
}
