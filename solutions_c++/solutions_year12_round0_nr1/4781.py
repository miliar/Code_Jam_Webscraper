#include <iostream>
#include <map>

using namespace std;

int main(){
    string a = "ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv";
    string b = "our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up";
    map<char,char> conv;
    for(int i=0;i<a.size();i++) conv[a[i]] = b[i];
    conv['q'] = 'z';
    conv['z'] = 'q';
    int T;
    cin >> T;
    string s;
    getline(cin, s);
    for(int i=0;i<T;i++){
            getline(cin, s);
            for(int j=0;j<s.size();j++) s[j] = conv[s[j]];
            cout << "Case #" << i+1 << ": " << s << endl;
    }
}
