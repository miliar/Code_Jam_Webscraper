#include<iostream>
#include<cstring>

using namespace std;

int a[105],n,s,p;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int test;
    cin>>test;
    for (int t=1;t<=test;t++){
        int ans=0;
        cin>>n>>s>>p;
        for (int i=0;i<n;i++) cin>>a[i];
    sort(a,a+n);
    for (int i=n-1;i>=0;i--){
        if (a[i]%3==0){
           if (a[i]/3>=p) ans++; else
           if ((a[i]/3+1>=p && a[i]>0) && s>0){
              s--;
              ans++;
              }
           }
           else
           {
               if (a[i]%3==1){
                  if (a[i]/3+1>=p) ans++;
                  }
                  else
                  {
                      if (a[i]/3+1>=p) ans++;
                      else 
                      if (a[i]/3+2>=p && s>0){
                         s--;
                         ans++;
                         }
                  }
           }
        //cout<<i<<" is no "<<a[i]<<"     "<<ans<<endl;
        }
    cout<<"Case #"<<t<<": "<<ans<<endl;
    }
}
