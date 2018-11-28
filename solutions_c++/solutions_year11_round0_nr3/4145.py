#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int cases;
    cin>>cases;
    for(int cnum=1;cnum<=cases;cnum++) {
        int n;
        int small=-1;
        int sum=0;
        int x=0;
        cin>>n;
        for(int i=0;i<n;i++) {
            int tmp;
            cin>>tmp;
            sum+=tmp;
            if(small==-1||tmp<small) small=tmp;
            x^=tmp;
        }
        cout<<"Case #"<<cnum<<": ";
        if(x>0) cout<<"NO";
        else cout<<sum-small;
        cout<<endl;
    }
}
