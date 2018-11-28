#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int main()
{
    vector<int> v;
    int n,t,s,i,k,p,ans = 0;
    int count = 0;
    int caseno = 0;
    int flag = 1;
    int wq=0;
    cin>>t;
    while(t--){
        
               cin>>n>>s>>p;
                  for(i=0;i<n;i++){
                                   cin >> k;
                                   v.push_back(k);
                  }
                  caseno++;
                  if(p == 0){
                       wq=1;
                  }
                  if(wq!=1) {
                        for(i=0;i<n;i++){
                                   if(v[i]/p >= 3){
                                             ans++;
                                   }  else if(v[i]/p){
                                             if(v[i] >= (3*p)-2)ans++;
                                             else if(v[i] >= (3*p)-4 && s>0 && v[i] >= p){
                                                  ans++;
                                                  s--;
                                                  //cout<<"qwe"<<endl;
                                                  
                                             }
                                   }
                        }
                  }
                  if(wq==0)cout<<"Case #"<<caseno<<": "<<ans<<endl;
                  else cout<<"Case #"<<caseno<<": "<<n<<endl;
                  ans = 0;
                  v.clear();
                  flag = 1;
                  wq=0;
    }
    return 0;
}
    
