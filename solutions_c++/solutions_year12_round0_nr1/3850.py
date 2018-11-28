#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

string from = "abcdefghijklmnopqrstuvwxyz";
string to   = "yhesocvxduiglbkrztnwjpfmaq";


int main(){
    int n;
    string in;
    
    scanf("%d\n",&n);
    for(int j=1 ; j<=n ; ++j){
        getline(cin,in);
        cout << "Case #" << j << ": ";
        for(int i=0;i < in.size();++i){
            if(in.at(i)==' '){
                cout << ' ';
            }else{
                cout << to.at(from.find_first_of(in.at(i),0));
            }
        }
        cout << endl;
    }
}
