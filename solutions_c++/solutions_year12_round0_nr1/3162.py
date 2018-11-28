#include <iostream>
#include <string>
using namespace std;

char conv[26] = {
    'y', //a
    'h', //b
    'e', //c
    's', //d
    'o', //e
    'c', //f
    'v', //g
    'x', //h
    'd', //i
    'u', //j
    'i', //k
    'g', //l
    'l', //m
    'b', //n
    'k', //o
    'r', //p
    'z', //q
    't', //r
    'n', //s
    'w', //t
    'j', //u
    'p', //v
    'f', //w
    'm', //x
    'a', //y
    'q',  //z
};

int main(){
    int n;
    cin >> n;
    cin.ignore();
    for(int i=0;i<n;i++){
        string str;
        getline(cin,str);
        cout << "Case #" << i+1 << ": "; 
        for(int j=0;j<str.size();++j){
            if(str[j] == ' '){
                cout << str[j];
            }else{
                cout << (char)conv[str[j] - 'a'];
            }
        }
        cout << endl;
    }
}
