#include<iostream>
#include<stdio.h>
#include<stdlib.h>

using namespace std;
const int MAX_LEN = 10;
int main(){
    int t;
        freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
    cin >> t;
    int i;
    for(i=0;i<t;i++){
       char a[MAX_LEN][MAX_LEN];
       int j, k;
       for(j=0;j<4;j++){
           for(k=0;k<4;k++){
                cin >> a[j][k];
           }
       }
       //check row
       int flag;
        for(j=0;j<4;j++){
            flag = 1;
            if(a[j][0]=='.'){flag=0;continue;}
            else{
                if(a[j][0]!='T'){
                    for(k=1;k<4;k++){
                        if(a[j][0]!=a[j][k]&&a[j][k]!='T'){
                            flag = 0;
                        }
                    }
                    if(flag == 1){
                        if(a[j][0]=='X'){
                            cout << "Case #"<<i+1<<": X won"<<endl;
                            break;
                        }
                        else {
                            cout<< "Case #"<<i+1<<": O won"<<endl;
                            break;
                        }
                    }
                }else{
                    if(a[j][1]!='.'){
                    for(k=1;k<4;k++){
                        if(a[j][1]!=a[j][k]){
                            flag = 0;
                        }
                    }
                    if(flag == 1){
                        if(a[j][1]=='X'){
                            cout << "Case #"<<i+1<<": X won"<<endl;
                            break;
                        }
                        else {
                            cout<< "Case #"<<i+1<<": O won"<<endl;
                            break;
                        }
                    }
                }else flag=0;
                }
            }
        }
        //check colums
        if(flag == 0){
            int flag1;
            for(j=0;j<4;j++){
                flag1 = 1;
                if(a[0][j]=='.') {flag1=0; continue;}
                else{
                if(a[0][j]!='T'){
                    for(k=1;k<4;k++){
                        if(a[0][j]!=a[k][j]&&a[k][j]!='T'){
                            flag1 = 0;
                        }
                    }
                    if(flag1 == 1){
                        if(a[0][j]=='X'){
                            cout<<"Case #"<<i+1<<": X won"<<endl;
                            break;
                        }
                        else {cout<< "Case #"<<i+1<<": O won"<<endl;
                            break;
                        }
                    }
                    }else{
                        if(a[1][j]!='.'){
                        for(k=0;k<4;k++){
                            if(a[1][j]!=a[k][j]){
                                flag1 = 0;
                            }
                        }
                        if(flag1 == 1){
                            if(a[1][j]=='X'){
                                cout<<"Case #"<<i+1<<": X won"<<endl;
                                break;
                            }
                            else {cout<< "Case #"<<i+1<<": O won"<<endl;
                                break;
                            }
                        }
                        }else flag1 = 0;
                    }
                }
            }
            //check diagonal
            if(flag1 == 0){
                int flag2 = 1;
                if(a[0][0]!='.'){
               if(a[0][0]!='T'){
                    for(j=0;j<4;j++){
                        if(a[0][0]!=a[j][j]&&a[j][j]!='T'){
                            flag2 = 0;
                        }
                    }
                if(flag2==1){
                    if(a[0][0]=='X'){
                        cout << "Case #"<<i+1<<": X won"<<endl;
                    }
                    else{
                        cout << "Case #"<<i+1<<": O won"<<endl;
                    }
                    }
               }
               else{
                   if(a[1][1]!='.'){
                    for(j=1;j<4;j++){
                        if(a[1][1]!=a[j][j]) flag2 = 0;
                    }
                    if(flag2==1){
                        if(a[1][1]=='X'){
                            cout << "Case #"<<i+1<<": X won"<<endl;
                        }
                        else{
                            cout << "Case #"<<i+1<<": O won"<<endl;
                        }
                    }
                   }else flag2 = 0;
               }
               }else flag2=0;
                if(flag2==0){
                    int flag3 = 1;
                    if(a[0][3]!='.'){
                    if(a[0][3]!='T'){
                        for(j=0;j<4;j++){
                            if(a[0][3]!=a[j][3-j]&&a[j][3-j]!='T'){
                                flag3 = 0;
                            }
                        }
                        if(flag3==1){
                            if(a[0][3]=='X'){
                                cout<<"Case #"<<i+1<<": X won"<<endl;
                            }
                            else{
                                cout<<"Case #"<<i+1<<": O won"<<endl;
                            }
                        }
                    }
                    else{
                        if(a[1][2]!='.'){
                        for(j=1;j<4;j++){
                            if(a[1][2]!=a[j][3-j]) flag3=0;
                        }
                        if(flag3==1){
                            if(a[1][2]=='X'){
                                cout<<"Case #"<<i+1<<": X won"<<endl;
                            }
                            else{
                                cout<<"Case #"<<i+1<<": O won"<<endl;
                            }
                        }
                        }else flag3 = 0;
                    }
                    }else flag3=0;
            if(flag3==0){
                int flag4 = 1;
                for(j=0;j<4;j++){
                    for(k=0;k<4;k++){
                        if(a[j][k]=='.') flag4=0;
                    }
                }
                if(flag4==0) cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
                else cout<<"Case #"<<i+1<<": Draw"<<endl;
            }
        }
            }
        }
    }
}

