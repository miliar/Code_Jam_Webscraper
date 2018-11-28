#include <iostream>
#include <algorithm>
using namespace std;

int main(){

    int tcases;
    cin>>tcases;

    for(int tcase=1;tcase<=tcases;tcase++){

        cout<<"Case #"<<tcase<<": ";

        int n,k,b,T;
        cin>>n>>k>>b>>T;
        int x[n];
        for(int i=0;i<n;i++){
            cin>>x[i];
        }

        int v[n];
        for(int i=0;i<n;i++){
            cin>>v[i];
        }

        double t[n];
        int cnt=0;
        for(int i=0;i<n;i++){
            t[i]=double(b-x[i])/double(v[i]);
            if(t[i]<=T){
                ++cnt;
            }
        }
        if(cnt<k){
            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }

        reverse(t,t+n);

        cnt=0;
        int nsw=0;
        for(int i=0;i<n;i++){
            if(t[i]<=T){
                for(int j=i-1;j>=0;j--){
                    if(t[j]>T){
                        swap(t[j],t[j+1]);
                        ++nsw;
                    }
                    else{
                        break;
                    }
                }
                ++cnt;
            }
            if(cnt==k){
                break;
            }
        }

        cout<<nsw<<endl;




    }


    return 0;
}
