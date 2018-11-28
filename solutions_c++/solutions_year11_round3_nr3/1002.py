#include <iostream>
#include <vector>
#include <algorithm>
#include <stdlib.h>

using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int ii=0;ii<t;ii++){
        long long n,l,h;
        cin>>n>>l>>h;
        vector<long long> v;
        for(int i=0;i<n;i++){
            long long temp;
            cin>>temp;
            v.push_back(temp);
        }
        bool ans=false;
        int sol;
        for(long long i=l;i<=h;i++){
            bool flag=true;
            for(int j=0;j<v.size();j++){
                int x,y;
                if(v[j]<i){
                    x=v[j];
                    y=i;
                } else {
                    x=i;
                    y=v[j];
                }
                if(y%x!=0){
                    flag=false;
                }
            }
            if(flag==true){
                ans=true;
                sol=i;
                i=h+1;
            }
        }
        if(ans){
            cout<<"Case #"<<ii+1<<": "<<sol<<endl;
        } else {
            cout<<"Case #"<<ii+1<<": "<<"NO"<<endl;
        }
        
    }
}