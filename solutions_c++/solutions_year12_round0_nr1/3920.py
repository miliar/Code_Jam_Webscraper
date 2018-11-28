#include<iostream>
#include<cstdio>
using namespace std;

main(){
 int tc;
 string text, res;
 string decode = "yhesocvxduiglbkrztnwjpfmaq";
 freopen("A-small-attempt0.in","r",stdin);
 freopen("output.txt","w",stdout);
 cin>>tc;
 getline(cin, text);
 for(int i = 1; i <= tc; i++){
    getline(cin, text);
    res = "";
    for(int j = 0; j < text.length(); j++){
        if(text[j] != ' ')
            res += decode[text[j] - 97];
        else
            res += " ";
    }
    cout<<"Case #"<<i<<": "<<res<<endl;
 }
    fclose(stdin);
    fclose(stdout);
}
