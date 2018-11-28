#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main(){
    int n;
    string a;
    string trans = "yhesocvxduiglbkrztnwjpfmaq";
    ifstream fin;
    ofstream fout;
    fin.open("A-small-attempt0.in");
    fout.open("A-small-attempt0.out");
    fin>>n;
    getline(fin,a);
    for (int t=0;t<n;t++){
        getline(fin,a);
        string b;
        for (int i=0;i<a.size();i++){
            char c = ' ';
            if (a[i]!=' ') c= trans[a[i]-'a'];
            b += c;
        }
        fout<<"Case #"<<t+1<<": "<<b<<endl;
    }
            
    
}
