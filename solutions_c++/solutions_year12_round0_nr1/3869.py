/*
ID: zjshenn1
PROG:
LANG: C++
*/
#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
int main(){
    #if 0
    freopen("in.txt","r",stdin);
    #else
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    #endif
    string a="yhesocvxduiglbkrztnwjpfmaq";
    int ca;
    cin>>ca;
     getchar();
    for(int i=1;i<=ca;i++){

        string t;
        getline(cin,t,'\n');
        for(int j=0;j<t.size();j++){
            if(t[j]!=' '){
                t[j]=a[t[j]-97];
            }
        }
        cout<<"Case #"<<i<<": "<<t<<endl;
    }
    return 0;
}
