#include<iostream>
#include<cstdio>
#include<fstream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<math.h>
#include<string>

using namespace std;

int a[1100];
int n,tot;

int main(){
      freopen("C-large.in","r",stdin);
      freopen("out.txt","w",stdout);
      cin>>tot;
      for (int ca=1;ca<=tot;ca++){
            memset(a,0,sizeof(a));
            cin>>n;
            int m=2000000000,s=0,k=0;
            for (int i=1;i<=n;i++){
                  cin>>a[i];
                  if (a[i]<m) m=a[i];
                  s+=a[i];
                  k^=a[i];
            }
            cout<<"Case #"<<ca<<": ";
            if (k) cout<<"NO"<<endl; else cout<<s-m<<endl;
      }
}
            
      
