#include <iostream>
using namespace std;

int d[1005];
int n;

int in() {
    int c=0;
    for(int i=1;i<=n;i++) {
        if(d[i]!=i) c++;
    }
    return c;
}

int main() {
    int CASEN;
    cin>>CASEN;
    for(int ci=1;ci<=CASEN;ci++) {
        cin>>n;
        for(int i=1;i<=n;i++) cin>>d[i];
        int r = in();

        cout<<"Case #"<<ci<<": "<<r<<endl;;
    }

    return 0;
}

