#include <iostream>
#include <cstdio>
#include <map>
#include <string>
using namespace std;

bool usd[400];


int main(){

    freopen("sample.txt","r",stdin);
    freopen("a.out","w",stdout);

    map <char,char> dic;

    string st1,st2;

    dic['y']='a';usd['a']=1;
    dic['e']='o';usd['o']=1;
    dic['q']='z';usd['z']=1;

    for(int run=1;run<=3;run++){
        getline(cin,st1);
        getline(cin,st2);
        //cout<<st1<<" "<<st2<<endl;
        for(int i=0;i<st1.length();i++) dic[st1[i]]=st2[i], usd[st2[i]]=1;
    }

    for(int i=0;i<26;i++) if(!usd['a'+i]) dic['z']= 'a'+i;
    //for(int i=0;i<26;i++) cout<<(char) ('a'+i)<<":"<<dic['a'+i]<<endl;

    freopen("a.in","r",stdin);

    int tc;
    cin>>tc;
    getline(cin,st1);
    for(int run=1;run<=tc;run++){
        getline(cin,st1);
        cout<<"Case #"<<run<<": ";
        for(int i=0;i<st1.length();i++) cout<<(char) dic[st1[i]];
        cout<<endl;
    }



    return 0;
}
