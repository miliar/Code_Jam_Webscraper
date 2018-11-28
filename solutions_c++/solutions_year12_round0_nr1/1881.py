#include <fstream>
#include <iostream>

using namespace std;

const int convert[]={121,104,101,115,111,99,118,120,100,117,105,103,108,98,107,114,122,116,110,119,106,112,102,109,97,113};

ifstream f("input.in");
ofstream g("output.out");

int t;
string s;

int main(){

    f >> t;
    f.get();
    for(int j=1; j<=t; ++j){
        getline(f,s);
        int n = s.size()-1;
        g << "Case #" << j <<": ";
        for(int i=0; i<=n; i++){
            if (s[i] == ' ') g << ' ';
            else{
                char c = convert[s[i]-'a'];
                g << c;
            }
        }
        g << "\n";
    }


}
