#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int check(vector<char> v1){
    int c1=0,c2=0,c3=0;
    for(int i=0;i<4;i++){
        if(v1[i] == '.') return 0;
        else{if (v1[i] == 'X')c1=c1 + 1;
             else{if (v1[i] == 'O') c2=c2+1;
                  else c3 =c3 +1;}}}
    if((c1 == 4)||((c1 == 3)&&(c3 == 1))) return 1;
    else{
        if ((c2 == 4)||((c2 == 3)&&(c3 == 1))) return 2;
        else return 3;}}   

int main() {
    int t;
    cin>>t;
    char next;
    for(int i=1;i<=t;i++){
        vector<char> v;
        int count=0;
        bool ans=false;
        for(int j=0;j<16;j++){
            cin>>next;
            if (next == '.')count=count+1;
            v.push_back(next);}
        for(int k=0;k<4;k++){
            vector<char>v1;
            for(int p=0;p<4;p++){
                v1.push_back(v[p+4*k]);}
            if (check(v1) == 1){
                cout<<"Case #"<<i<<": X won"<<"\n";
                ans=true;
                break;}
         if (check(v1) == 2){
                cout<<"Case #"<<i<<": O won"<<"\n";
                ans=true;
                break;}}
        if (ans) continue;
        else {
            for(int k=0;k<4;k++){
            vector<char>v1;
            for(int p=0;p<4;p++){
                v1.push_back(v[4*p+k]);}
            if (check(v1) == 1){
                cout<<"Case #"<<i<<": X won"<<"\n";
                ans=true;
                break;}
             if (check(v1) == 2){
                cout<<"Case #"<<i<<": O won"<<"\n";
                ans=true;
                break;}}}
        if (ans) continue;
        else {vector<char> v1;
              for(int s=0;s<4;s++){
                  v1.push_back(v[5*s]);}
              if (check(v1) == 1){
                cout<<"Case #"<<i<<": X won"<<"\n";
                ans=true;}
             if (check(v1) == 2){
                cout<<"Case #"<<i<<": O won"<<"\n";
                ans=true;}}
        if (ans) continue;
        else { vector<char> v1;
              for(int s=1;s<=4;s++){
                  v1.push_back(v[3*s]);}
              if (check(v1) == 1){
                cout<<"Case #"<<i<<": X won"<<"\n";
                ans=true;}
             if (check(v1) == 2){
                cout<<"Case #"<<i<<": O won"<<"\n";
                ans=true;}}
        if(!ans){if(count == 0)cout<<"Case #"<<i<<": Draw"<<"\n";
                 else cout<<"Case #"<<i<<": Game has not completed"<<"\n";}}
            
    return 0;
}
