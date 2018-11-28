#include <iostream>
using namespace std;
int main(){
    int i ,j,ntc,n,l,h,a[10000];
     cin >> ntc;
     for(int tc=1;tc<=ntc;tc++){
             cin >> n >> l >> h;
             for(i=1;i<=n;i++)
                cin >> a[i];
              int yes=1;
             printf("Case #%d: ",tc);
             for(i=l;i<=h;i++){
                 yes=1;
                 for(j=1;j<=n;j++)
                 if(yes){
                     
                     if(i >= a[j])
                         if(i % a[j] == 0)
                            continue;
                         else
                             yes=0;
                     else
                        if(a[j] % i == 0)
                           continue;
                        else
                           yes=0;
                 }
                 if(yes){ cout <<  i << endl;
                       break;
                 }
             }
                            
             if(yes==0) cout << "NO" << endl;           
                
                   
             
                
     }
}
