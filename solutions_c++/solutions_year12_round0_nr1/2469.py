#include <iostream>
#include <string>
#include <map>
using namespace std;

int main(){
    string s="ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
    string d="our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
    map<char,char> t;
    for(int i=0;i<26;i++){
        for(int j=0;j<s.length();j++)
            if(s[j]==(97+i))
                t[97+i]=d[j];
    }
    t['z']='q';
    t['q']='z';
    t[' ']=' ';
    int T;
    cin>>T;
    getline(cin,s);
    for(int z=1;z<=T;z++){
        getline(cin,s);
        cout<<"Case #"<<z<<": ";
        for(int j=0;j<s.length();j++)
            cout<<t[s[j]];
        cout<<endl;
    }
    return 0;
}
