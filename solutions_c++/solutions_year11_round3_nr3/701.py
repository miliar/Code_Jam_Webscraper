#include<iostream>
#include<algorithm>;

using namespace std;

int tot,l,r,n,ans,a[200];

int main(){
      freopen("D:\\C-small-attempt0.in","r",stdin);
      freopen("D:\\out.txt","w",stdout);
      cin>>tot;
      for (int ca=1;ca<=tot;ca++){
            cin>>n>>l>>r;
            for (int i=1;i<=n;i++) cin>>a[i];
            sort(a+1,a+n+1);
            bool can=1,have=0;
            if (can)            
            for (int i=l;i<=r;i++){
                  have=1;
                  for (int j=1;j<=n;j++) if (((a[j]%i)!=0)&&((i%a[j])!=0)){
                        have=0;
                        break;
                  }
                  if (have){
                        ans=i;
                        break;
                  }
            }
            cout<<"Case #"<<ca<<": ";
            if (have) cout<<ans<<endl; else cout<<"NO"<<endl;
      }
//      system("pause");
}
                  

      
