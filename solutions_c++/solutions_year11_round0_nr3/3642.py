#include<iostream>

using namespace std;

int N;
int sum=0;
#define MIN -1000000001

int main() {
    int T;
    cin>>T;
    for (int t=1;t<=T;t++) {
        cin>>N;
        int xr=0;
        sum = 0;
        int smallest = -MIN;
        for (int i=0;i<N;i++) {
            int k;
            cin>>k;
            sum += k;
            xr = xr ^ k;
            smallest = min(smallest, k);
        }
        int ret = (sum - smallest);
        if (xr != 0) ret = -1;
        if (ret > 0) {
            cout<<"Case #"<<t<<": "<<ret<<endl;
        } else {
            cout<<"Case #"<<t<<": NO"<<endl;
        }
    }
}
