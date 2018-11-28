#include<iostream>
#include<fstream>
#include<vector>
#include<cmath>

using namespace std;

int main(){
    freopen("c.in","rt",stdin);
    freopen("c.out","wt",stdout);
    int t,n,l,h;
    cin>>t;
    int freq[100];
    for (int i=1 ;i<=t ; i++){
        cin>>n>>l>>h;
        for (int j=0 ; j<n ; j++)cin>>freq[j];
        int target = -1;
        for (int k=l ; k<=h ; k++){
            bool ok = true;
            for (int j=0 ; j<n ; j++)
                if (!(freq[j] % k == 0 || k % freq[j] == 0)){
                              ok = false;
                              break;
                }
            if (ok){
                    target = k;
                    break;
            }
                   
        }
        cout<<"Case #"<<i<<": "; 
        if (target != -1){
                   cout<<target<<endl;
        }else{
              cout<<"NO\n";
              }
    }
    //system("pause");
    return 0;
}
