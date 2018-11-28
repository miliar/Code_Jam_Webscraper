#include <iostream>
#include <string>
using namespace std;
int main(){
    char  p[100]="yhesocvxduiglbkrztnwjpfmaq";
    int ntc;
    cin >> ntc;
    string s,s2;
    getline(cin,s);
    for(int tc=1;tc<=ntc;tc++){
            getline(cin,s);
            for(int i=0;i<s.size();i++)
            if(s[i]>='a'&& s[i] <='z'){
                s[i]=p[s[i]-'a'];
            }
           cout << "Case #"<<tc << ": " << s << endl;
    }
 
}
