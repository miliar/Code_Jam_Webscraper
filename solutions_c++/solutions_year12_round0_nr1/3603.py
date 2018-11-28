#include<iostream>
#include<string>
#include<cstring>
using namespace std;

string plain = "";
string cipher = "";
string str;
int n;

void pre(){
    plain += "our language is impossible to understand";
    plain += "there are twenty six factorial possibilities";
    plain += "so it is okay if you want to just give up";
    plain += "zq";
    cipher += "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    cipher += "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    cipher += "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    cipher += "qz";
}

void solve(){
    getline(cin, str);
    int t = 0;
    while(getline(cin, str)){
        t++;
        cout<<"Case #"<<t<<": ";
        for(int i = 0; i < str.length(); i++){
            for(int j = 0; j < plain.length(); j++){
                if(str[i] == cipher[j]){
                    cout<<plain[j];
                    break;
                }
            }
        }
        cout<<endl;
    }
    
}

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    pre();
    solve();
    return 0;
}