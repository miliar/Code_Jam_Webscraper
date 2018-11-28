#include <string>
#include <iostream>
#include <vector>

using namespace std;

int main(){
    vector<char> M(128);
    M['z'] = 'q';
    M['q'] = 'z';
    string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    string b = "our language is impossible to understand";
    for(int i = 0; i < (int)a.size(); ++i) M[a[i]] = b[i];
    
    a = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    b = "there are twenty six factorial possibilities";
    for(int i = 0; i < (int)a.size(); ++i) M[a[i]] = b[i];
    
    a = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    b = "so it is okay if you want to just give up";
    for(int i = 0; i < (int)a.size(); ++i) M[a[i]] = b[i];
    
    int n;
    cin >> n;
    string str;
    
    getline(cin, str);
    for(int i = 1; i <= n; ++i){
        getline(cin, str);
        cout << "Case #" << i << ": ";
        for(int i = 0; i < (int)str.size(); ++i) cout << M[str[i]];
        cout << endl;
    }
    
    return 0;
}
