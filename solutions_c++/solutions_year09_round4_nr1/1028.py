#include <cstdlib>
#include <cstdio>
#include <string>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t,T,i,j,n;
    cin>>T;
    for (t=1; t<=T; t++) {
        cin>>n;
        vector<string> v(n);
        for (i=0; i<n; i++) {
            cin>>v[i];
            while (v[i].size()>0 && v[i][v[i].size()-1]=='0') {
                  v[i].erase(v[i].size()-1);
            }
            //cout<<"v["<<i<<"]="<<v[i]<<endl;
        }
        int ok=0;
        int cnt=0;
        for (j=1; j<n; j++) {
            for (i=0; i<n && v[i].size()>j; i++)
                ;
            cnt+=i;
            v.erase(v.begin()+i);
        }
        cout<<"Case #"<<t<<": "<<cnt<<endl;
    }
//    system("PAUSE");
    return 0;
}
