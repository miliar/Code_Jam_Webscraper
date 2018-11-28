#include <iostream>
#include <string>
#include <vector>

using namespace std;

int i,j,k,l,m,n,t,tt,cc,dd,ii,jj;
int sum, jami, minn,a;


int main(){
    freopen("c:/input.txt","r",stdin);
    freopen("c:/output.txt","w",stdout);
    cin>>t;
    while (t--){
          tt++;
          cout<<"Case #"<<tt<<": ";
          cin>>n;
          minn=1000000000;
          sum=0;
          jami=0;
          for (i=0;i<n;i++){
              cin>>a;
              if (minn>a) minn=a;
              sum+=a;
              jami^=a;    
          }
          if (jami>0) cout<<"NO"<<endl; else
          cout<<sum-minn<<endl;
    }
    //system("pause");
    return 0;    
}
