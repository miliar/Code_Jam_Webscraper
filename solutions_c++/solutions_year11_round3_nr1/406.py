#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;
char s[100][100];
int main(){
    int T,n,m;
    freopen ("A-large.in","r",stdin);
    freopen ("acl.out","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++){
        cin>>n>>m;
        for(int i=0;i<n;i++)
            cin>>s[i];
        int flag=1;
        for(int i=0;i<n;i++){
            if(flag==0)break;
            for(int j=0;j<m;j++){
                if(s[i][j]=='#'){
                    if(i+1<n&&j+1<m){
                        if(s[i+1][j]=='#'&&s[i+1][j+1]=='#'&&s[i][j+1]=='#'){
                            s[i][j]='/';
                            s[i][j+1]='\\';
                            s[i+1][j]='\\';
                            s[i+1][j+1]='/';
                        }
                        else {
                            flag=0;
                            break;
                        }
                    }
                    else {
                        flag=0;
                        break;
                    }
                    
                }
            }
        } 
        cout<<"Case #"<<cas<<":"<<endl;
        if(flag==0){
            cout<<"Impossible"<<endl;
        }
        else {
            for(int i=0;i<n;i++){
                cout<<s[i]<<endl;
            }
        }
    }
}
        
                    
