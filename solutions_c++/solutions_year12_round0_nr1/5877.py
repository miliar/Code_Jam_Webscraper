#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    ifstream in1("a_in.txt"), in2("a_out.txt");
    char table[256];
    
    char from, to;
    memset(table, 0, 256);
    table['q'] = 'z';
    table['z'] = 'q';
    
    while(in1>>from && in2>>to) {
        if(table[from] == 0) {
            table[from] = to;
            cout << from << "->" << to << "\t";    
        }
    }
    
    ifstream in("a.in");
    ofstream out("a.out");
    int t;
    
    in>>t;
    string s;
    getline(in,s);
    
    for(int i = 0; i<t;i++) {
        
        getline(in,s);
        for(int j = 0; j<s.size();j++) {
            if(s[j] != ' ') s[j] = table[s[j]];    
        }    
        out << "Case #"<<i+1<<": "<<s<<endl;
    }
    
    system("pause");
        
}