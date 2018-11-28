#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

int T;
string translation_key = "yhesocvxduiglbkrztnwjpfmaq";

int main(){
freopen("A-small-attempt0.in", "r", stdin);
freopen("output.txt", "w", stdout);

cin >> T;
string str;

getline(cin,str);

for(int i=0;i<T;i++){
    getline(cin,str);
    cout << "Case #" << i+1 << ": ";
    for(int j=0;j<str.size();j++){
        if(str[j]==' ')
            cout << ' ';
        else
            cout << translation_key[str[j]-'a'];
    }
    if(i != T-1)
        cout << endl;
}

return 0;
}
