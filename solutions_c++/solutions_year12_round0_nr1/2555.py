#include <map>
#include <iostream>
#include <fstream>
#include <cstdlib>
#include <climits>

using namespace std;

int main(int argc, char** argv) {
    map<char, char> g_e;
    map<char, char>::iterator ig_e;
    
    string g[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
                  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
                  "de kr kd eoya kw aej tysr re ujdr lkgc jv"};
    
    string e[] = {"our language is impossible to understand",
                  "there are twenty six factorial possibilities",
                  "so it is okay if you want to just give up"};
    string::iterator ig, ie;
    
    for(int i=0; i<3; i++) {
        for(ig=g[i].begin(), ie=e[i].begin(); ig!=g[i].end(); ++ie, ++ig) {
            g_e[*ig]=*ie;
        }
    }
    g_e['z']='q';
    g_e['q']='z';
    
    ifstream input ("A-small-attempt0.in");
    ofstream output("output.out");
    int T;
    string t;
    string::iterator it;
    
    input>>T;
    input.ignore(INT_MAX, '\n');
    
    for(int i=1; i<=T; i++) {
        getline(input,t);
        
        for(it=t.begin(); it!=t.end(); it++) {
           *it=g_e[*it];
        }
        output <<"Case #"<<i<<": "<< t <<endl;
    }
    
    return 0;
}

