#include<iostream>
using namespace std;
int a[100];
char ch;
int i,j,k,ans;
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tt,n;
    cin>>tt;
    for(int ii=1;ii<=tt;ii++){
        cin>>n;
        for(i=1;i<=n;i++){
            a[i]=0;
            for(j=1;j<=n;j++){
                cin>>ch;
                if(ch=='1')a[i]=j;
            }
        }
        ans=0;
        for(i=1;i<=n;i++){
            for(j=i;j<=n;j++){
                if(a[j]<=i)break;
                ans++;
            }
            for(;j>i;j--)
                a[j]=a[j-1];

        }
        cout<<"Case #"<<ii<<": "<<ans<<endl;
    }
    return(0);
}
