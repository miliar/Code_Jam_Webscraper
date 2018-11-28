#include <iostream>
using namespace std;

int main() {
    int CASEN;
    cin>>CASEN;
    for(int ci=1;ci<=CASEN;ci++) {
        int n,k;
        cin>>n>>k;
        int t = (1<<n);
        if(k%t == t-1) {
            cout<<"Case #"<<ci<<": ON"<<endl;
        } else {
            cout<<"Case #"<<ci<<": OFF"<<endl;
        }
    }

    return 0;
}

