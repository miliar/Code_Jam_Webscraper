#include<iostream>
#include<string>
using namespace std;

int main(){
    int T;
    cin>>T;
    string s;
    char map[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    getline(cin,s);
    for(int i=1;i<=T;i++){
            cout<<"Case #"<<i<<": ";
            getline(cin,s);
            for(int j=0;j<s.length();j++)
                    (s[j]!=' ') ? cout<<map[s[j]-'a'] : cout<<" ";
            cout<<endl;
    }
    return 0;
}
