#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <fstream>
#include <time.h>
using namespace std;
#define INF 1000000000 //10^9

int main (int argc, const char * argv[])
{
    ifstream ifs("/Users/w_shunn/Desktop/A-small-attempt2.in");
    ofstream ofs;
    ofs.open( "/Users/w_shunn/Desktop/output.txt" );
    
    string str[3][2]={{"qzejp mysljylc kd kxveddknmc re jsicpdrysi","zqour language is impossible to understand"},{"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities"},{"de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up"}};
    
    map<char, char>s;
    for (int i=0; i<='z'-'a'; i++) {
        char t = 'a'+i;
        s.insert(map<char, char>::value_type(t,'?'));
    }
    
    for (int h=0; h<3;h++) {
    for (int i=0; i<str[h][0].size(); i++) {
        if(str[h][0][i]!=' '){
            s[(char)str[h][0][i]]=(char)str[h][1][i];
        }
    }
    }
    
    int X;
    ifs>>X;
    string n;
    getline(ifs,n);
    for (int i=0; i<X; i++) {
        getline(ifs,n);
        ofs<<"Case #"<<i+1<<": ";
        for (int j=0; j<n.size(); j++) {
            if(n[j]!=' '){
                ofs<<s[n[j]];
            }else ofs<<' ';
        }
        ofs<<endl;
    }
    
    
    return 0;
}

