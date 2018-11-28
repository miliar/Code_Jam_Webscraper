#include<iostream>
#include<vector>
using namespace std;
int main()
{
    int t,l=1;
    cin>>t;
    while(t--)
    {
    int n,s,p,k,i;
    cin>>n>>s>>p;
    int x,y;
    if(p>1){
    x=p+2*(p-1);
    y=p+2*(p-2);
}  else  if(p==1)
    {
    x=1;
    y=1;
}
else
{
    y=0;
    x=0;
}
    int ans=0;
    for(i=0;i<n;i++)
    {
                    cin>>k;
                    if(k>=x)
                    ans++;
                    else
                    { 
                        if(s>0)
                    {          if(k>=y)
                               { ans++;
                                 s--;
                               }
                    }
                        
                    }
    }
    cout<<"Case #"<<l<<": ";
    cout<<ans<<endl;
    l++;
}
}
