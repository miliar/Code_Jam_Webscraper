#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;
int t,r,c;
bool flag,fail;
int contador;
int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>t;
    for (int z=0;z<t;z++){
        cin>>c>>r;
        contador=0;
        flag=0;
        fail=0;
        char pepe[r][c];
        for (int i=0;i<c;i++){
            for (int j=0;j<r;j++){
                cin>>pepe[j][i];
                if (pepe[j][i]=='#') contador++;}}
        if (contador%4!=0) cout<<"Case #"<<z+1<<":"<<endl<<"Impossible"<<endl;
        else{
            contador/=4;
            while (flag==0){
                int m=0;
                for (int k=0;m<contador && flag==0;k++){
                    for (int i=0;i<c-1 && flag==0;i++){
                        for (int j=0;j<r-1 && flag==0;j++){
                            if (pepe[j][i]=='#'){
                                if (pepe[j+1][i]=='#' && pepe[j][i+1]=='#'&& pepe[j+1][i+1]=='#'){
                                    pepe[j][i]='/';
                                    pepe[j+1][i]='\\';
                                    pepe[j][i+1]='\\';
                                    pepe[j+1][i+1]='/';
                                    m++;}
                                else{
                                    cout<<"Case #"<<z+1<<":"<<endl<<"Impossible"<<endl;
                                    flag=1;
                                    fail=1;}}}}}
                flag=1;}
            if(fail==0){
                cout<<"Case #"<<z+1<<":"<<endl;
                for (int i=0;i<c;i++){
                    for (int j=0;j<r;j++){
                        cout<<pepe[j][i];}
                    cout<<endl;}}}}}
