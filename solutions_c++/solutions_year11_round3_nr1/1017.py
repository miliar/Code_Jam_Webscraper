#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;
string a[105];
int r,c;
bool check(){
    int sum=0,cnt=0;
    for (int i=0;i<r;i++) {
        for (int j=0;j<c;j++)
            if (a[i][j]=='#')
                sum++;
    }
    for (int i=0;i<r-1;i++){
        for (int j=0;j<c-1;j++) if (a[i][j]=='#'){
            if (a[i][j+1]=='#' && a[i+1][j]=='#' && a[i+1][j+1]=='#'){
                cnt+=4;
                a[i][j]='/';  a[i][j+1]='\\';
                a[i+1][j]='\\'; a[i+1][j+1]='/';
            }
            else
                return 0;
        }
    }
    if (cnt!=sum)
        return 0;
    return 1;
}
int main(){
    freopen("A-large.in","r",stdin );
    freopen("out.txt","w",stdout);
    int T; cin>>T;
    for (int t=1;t<=T;t++){
        cout<<"Case #"<<t<<":\n";
        cin>>r>>c;
        for (int i=0;i<r;i++)
            cin>>a[i];
        if (check()){
            for (int i=0;i<r;i++)
                cout<<a[i]<<endl;
        }else{
            cout<<"Impossible\n";
        }
    }
    return 0;
}