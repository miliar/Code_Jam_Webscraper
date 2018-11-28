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

int tot,n,a[1100];
int main(){
      freopen("D-large.in","r",stdin);
      freopen("out.txt","w",stdout);
      cin>>tot;
      for (int ca=1;ca<=tot;ca++){
            cin>>n;
            for (int i=1;i<=n;i++) cin>>a[i];
            int k=0;
            for (int i=1;i<=n;i++) if (a[i]!=i) k++;
            cout<<"Case #"<<ca<<": "<<k<<".000000"<<endl;
      }
}
      
      
