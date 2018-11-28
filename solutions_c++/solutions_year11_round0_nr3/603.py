#include <iostream>
using namespace std;


int main() {
    int CASEN;
    cin>>CASEN;
    for(int ci=1;ci<=CASEN;ci++) {
        int N;
        int mini = 1000000001;
        cin>>N;
        int sum=0, psum=0;
        for(int i=0;i<N;i++) {
            int p;
            cin>>p;
            sum += p;
            psum ^= p;
            mini = min(mini,p);
        }
        int res = -1;
        if(psum==0) {
            res = sum-mini;
        } 
        cout<<"Case #"<<ci<<": ";
        if(res<0) cout<<"NO"<<endl;
        else cout<<res<<endl;
    }

    return 0;
}

