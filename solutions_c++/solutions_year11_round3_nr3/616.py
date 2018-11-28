#include <iostream>
#include <stdio.h>

using namespace std;

int l,h,n;
int inp[107];


bool mypos(int x)
{
    for(int i=0;i<n;i++)
    {
        int a=max(inp[i],x);
        int b=min(inp[i],x);
        if(a%b!=0) return false;
    }
    return true;



}



int main()
{
freopen("c.in","r",stdin);
freopen("c.out","w",stdout);

int t,ti;

cin>>t;
for(ti= 1;ti<=t;ti++)
{
    cin>>n>>l>>h;
    for(int i=0;i<n;i++) cin>>inp[i];

    bool flg=0;int res;
    for(int i=l;i<=h;i++)
    {
        if(mypos(i)) {  res=i;flg=1;break;}

    }

    cout<<"Case #"<<ti<<": ";
    if(!flg) cout<<"NO\n";
    else cout<<res<<endl;


}




return 0;

}
