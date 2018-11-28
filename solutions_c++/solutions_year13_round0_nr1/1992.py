#include<iostream>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<vector>
using namespace std;
int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int cases,n,i,j;
    bool t;
    char a[4][4],b[4][4],c[4][4];
    cin>>n;
    for(cases=1;cases<=n;cases++){
        t=true;
        cout<<"Case #"<<cases<<": ";
        cin>>a[0]>>a[1]>>a[2]>>a[3];
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                b[i][j]=c[i][j]=a[i][j];
                if(a[i][j]=='T'){
                    b[i][j]='X';
                    c[i][j]='O';
                    }
                if(a[i][j]=='.')
                    t=false;
                }
            }
        if(b[0][0]==b[0][1]&&b[0][1]==b[0][2]&&b[0][2]==b[0][3]&&b[0][0]!='.'){
            cout<<b[0][0]<<" won"<<endl;
            continue;
            }
        if(b[1][0]==b[1][1]&&b[1][1]==b[1][2]&&b[1][2]==b[1][3]&&b[1][0]!='.'){
            cout<<b[1][0]<<" won"<<endl;
            continue;
            }
        if(b[2][0]==b[2][1]&&b[2][1]==b[2][2]&&b[2][2]==b[2][3]&&b[2][0]!='.'){
            cout<<b[2][0]<<" won"<<endl;
            continue;
            }
        if(b[3][0]==b[3][1]&&b[3][1]==b[3][2]&&b[3][2]==b[3][3]&&b[3][0]!='.'){
            cout<<b[3][0]<<" won"<<endl;
            continue;
            }
        if(b[0][0]==b[1][0]&&b[1][0]==b[2][0]&&b[2][0]==b[3][0]&&b[0][0]!='.'){
            cout<<b[0][0]<<" won"<<endl;
            continue;
            }
        if(b[0][1]==b[1][1]&&b[1][1]==b[2][1]&&b[2][1]==b[3][1]&&b[0][1]!='.'){
            cout<<b[0][1]<<" won"<<endl;
            continue;
            }
        if(b[0][2]==b[1][2]&&b[1][2]==b[2][2]&&b[2][2]==b[3][2]&&b[0][2]!='.'){
            cout<<b[0][2]<<" won"<<endl;
            continue;
            }
        if(b[0][3]==b[1][3]&&b[1][3]==b[2][3]&&b[2][3]==b[3][3]&&b[0][3]!='.'){
            cout<<b[0][3]<<" won"<<endl;
            continue;
            }
        if(b[3][0]==b[2][1]&&b[2][1]==b[1][2]&&b[1][2]==b[0][3]&&b[3][0]!='.'){
            cout<<b[3][0]<<" won"<<endl;
            continue;
            }
        if(b[0][0]==b[1][1]&&b[1][1]==b[2][2]&&b[2][2]==b[3][3]&&b[0][0]!='.'){
            cout<<b[0][0]<<" won"<<endl;
            continue;
            }
        if(c[0][0]==c[0][1]&&c[0][1]==c[0][2]&&c[0][2]==c[0][3]&&c[0][0]!='.'){
            cout<<c[0][0]<<" won"<<endl;
            continue;
            }
        if(c[1][0]==c[1][1]&&c[1][1]==c[1][2]&&c[1][2]==c[1][3]&&c[1][0]!='.'){
            cout<<c[1][0]<<" won"<<endl;
            continue;
            }
        if(c[2][0]==c[2][1]&&c[2][1]==c[2][2]&&c[2][2]==c[2][3]&&c[2][0]!='.'){
            cout<<c[2][0]<<" won"<<endl;
            continue;
            }
        if(c[3][0]==c[3][1]&&c[3][1]==c[3][2]&&c[3][2]==c[3][3]&&c[3][0]!='.'){
            cout<<c[3][0]<<" won"<<endl;
            continue;
            }
        if(c[3][0]==c[2][1]&&c[2][1]==c[1][2]&&c[1][2]==c[0][3]&&c[3][0]!='.'){
            cout<<c[3][0]<<" won"<<endl;
            continue;
            }
        if(c[0][0]==c[1][1]&&c[1][1]==c[2][2]&&c[2][2]==c[3][3]&&c[0][0]!='.'){
            cout<<c[0][0]<<" won"<<endl;
            continue;
            }
        if(c[0][0]==c[1][0]&&c[1][0]==c[2][0]&&c[2][0]==c[3][0]&&c[0][0]!='.'){
            cout<<c[0][0]<<" won"<<endl;
            continue;
            }
        if(c[0][1]==c[1][1]&&c[1][1]==c[2][1]&&c[2][1]==c[3][1]&&c[0][1]!='.'){
            cout<<c[0][1]<<" won"<<endl;
            continue;
            }
        if(c[0][2]==c[1][2]&&c[1][2]==c[2][2]&&c[2][2]==c[3][2]&&c[0][2]!='.'){
            cout<<c[0][2]<<" won"<<endl;
            continue;
            }
        if(c[0][3]==c[1][3]&&c[1][3]==c[2][3]&&c[2][3]==c[3][3]&&c[0][3]!='.'){
            cout<<c[0][3]<<" won"<<endl;
            continue;
            }
        if(t){
            cout<<"Draw"<<endl;
            }
        else{
            cout<<"Game has not completed"<<endl;
            }
        }
    }
