#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int a[107];
int n,s,p;
int main(){
    int t,i,j,k;
    int b,c;
  //  freopen("B-large.in","r",stdin);
  //freopen("out.txt","w",stdout);
    cin>>t;
    for(k=1;k<=t;k++){
        cout<<"Case #"<<k<<": ";
        cin>>n>>s>>p;
        for(i=0;i<n;i++) cin>>a[i];
        if(p==0) {
            cout<<n<<endl;
            continue;
        }else if(p==1){
            b=0;
            for(i=0;i<n;i++)
                if(a[i]>=1) b++;
                cout<<b<<endl;
                continue;
        }
        sort(a,a+n);
        b=c=0;
        i=0;
        while(a[i]<3*p-4 && i<n) i++;
       // cout<<i<<endl;
        while(a[i]<3*p-2 && i<n){
            i++;
            b++;
    }//cout<<i<<' '<<b<<endl;
        while(i<n){
            i++;
            c++;
        }
        c+=b>=s?s:b;
        cout<<c<<endl;
    }
}
