#include <iostream>
#include <stdio.h>
#include <unordered_map>
#include <string>
#include <algorithm>
using namespace std;
unordered_map <char,char> mapi({{' ',' '},{'a','y'},{'b','h'},{'c','e'},{'d','s'},{'e','o'},{'f','c'},{'g','v'},{'h','x'},{'i','d'},{'j','u'},{'k','i'},{'l','g'},{'m','l'},{'n','b'},{'o','k'},{'p','r'},{'q','z'},{'r','t'},{'s','n'},{'t','w'},{'u','j'},{'v','p'},{'w','f'},{'x','m'},{'y','a'},{'z','q'}});


void trans(char x){
    cout<< mapi[x];
}
int main(){
    long long x,z=0;
    string str;
    cin>>x;
    getchar();
    while(x--){

        getline(cin,str);
        cout<<"Case #"<<++z<<": ";
        for_each(str.begin(),str.end(),trans);
        cout<<endl;}
    return 0;
}
