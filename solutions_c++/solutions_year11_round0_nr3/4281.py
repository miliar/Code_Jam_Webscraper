#include <iostream>

using namespace std;

int main(){
    freopen("C-large.in","r",stdin);
    freopen("outputfilecl.out","w",stdout);
    int t, n,  i, j;
    long c[1000], value, min, sum;
    cin>>t;
    for(j=1; j<=t; j++){
             cin>>n;
             for(i=0; i<n; i++)
                      cin>>c[i];
             value=c[0];
             for(i=1; i<n; i++)
                      value=value^c[i];
             if(value!=0)
                         cout<<"Case #"<<j<<": NO\n";
             else
             {
                 min=c[0];
                 sum=c[0];
                 for(i=1; i<n; i++){
                          if(c[i]<min)
                                      min=c[i];
                          sum+=c[i];
                 }
                 cout<<"Case #"<<j<<": "<<sum-min<<"\n";
             }
    }
    return 0;
}
