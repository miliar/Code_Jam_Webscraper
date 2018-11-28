#include <iostream>
#include <functional>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;
int arr[107];
int tc,n,s,p;
bool prc(int x){
    int cur = arr[x];
    if( ceil(double(cur)/3)>=p ) return 1;

    cur-=2;
    if(cur<0) return 0;

    if( floor(double(cur)/3)+2>=p){
        if(s<=0) return 0;
        s--;
        return 1;
    }
    return 0;
}
int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);


    cin>>tc;
    for(int run=1;run<=tc;run++){
        memset(arr,0,sizeof(arr));
        cin>>n>>s>>p;
        for(int i=0;i<n;i++) cin>>arr[i];
        sort(arr,arr+n, greater<int>());
        int ret=0;
        for(int i=0;i<n;i++){
            ret+=prc(i);
        }
        cout<<"Case #"<<run<<": "<<ret<<endl;
    }
    return 0;
}
