#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

ifstream in("C-small-attempt0.in");
ofstream out("C-small-attempt0.out");

const string base = "welcome to code jam";
string comp;

int count(int comp_pos, int base_pos) {
    int c = 0;
    if(base_pos < base.length()-1) {
        while((comp_pos = comp.find(base[base_pos], comp_pos)) != string::npos) {
            comp_pos++;
            if(comp_pos == comp.length())
                break;
            c += count(comp_pos,base_pos+1);
            if(c>=10000)
                c=c%10000;
        }
    }
    else if(base_pos == base.length()-1) {
        while((comp_pos = comp.find(base[base_pos], comp_pos)) != string::npos) {
            comp_pos++;
            c++;
            if(c>=10000)
                c=c%10000;
            if(comp_pos == comp.length())
                break;
        }
    }
    return c;
}

int main() {
    int N;
    char temp;
    in >> N;
    in >> temp;
    string comps[N];
    int i;
    for(i=0; i<N; i++)
        getline(in,comps[i]);
    for(i=0; i<N; i++) {
        comp.assign(comps[i]);
        out << "Case #" << i+1 << ": " << setw(4) << setfill('0') << count(0, 0) << endl;
    }
    in.close();
    out.close();
    return 0;
}

