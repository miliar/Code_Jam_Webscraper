#include <iostream>
#include <string>
using namespace std;

string a[100];

int main() {
    int T;
    cin>>T;
    for(int TT=1;TT<=T;TT++) {
        int n,m;
        cin>>n>>m;
        for (int i=0;i<n;i++) cin>>a[i];
        bool ok=true;
        for(int i=0;i<n;i++) for(int j=0;j<m;j++) if (a[i][j]=='#') {
            if (i==n-1 || a[i+1][j]!='#') ok=false;
            else if (j==m-1 || a[i][j+1]!='#') ok=false;
            else if (a[i+1][j+1]!='#') ok=false;
            else { a[i][j]=a[i+1][j+1]='/'; a[i+1][j]=a[i][j+1]='\\'; }
        }
        cout<<"Case #"<<TT<<": "<<endl;
        if (ok) {
            for (int i=0;i<n;i++) cout<<a[i]<<endl;
        } else cout<<"Impossible"<<endl;
    }
    return 0;
}
