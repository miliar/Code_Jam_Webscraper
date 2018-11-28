#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <fstream>

using namespace std;

template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

int main() {
    
    ifstream in("A-large.in");
    //ifstream in("X-large.in");
    
    ofstream out("A-large.out");
    //ofstream out("X-large.out");

    int N;
    
    in >> N;
    
    for (int i = 0; i < N; i++) {
        int S,Q;
        
        vector<string> SE;
        vector<string> QR;
        
        in >> S;
        
        string s;
        
        char tmp[101];
        
        in.getline(tmp, 101);
        
        for (int j = 0; j < S; j++) {
            in.getline(tmp, 101);
            s = tmp;  
            SE.push_back(s);
        }
        
        in >> Q;
        
        in.getline(tmp, 101);
        
        for (int j = 0; j < Q; j++) {
            in.getline(tmp, 101);
            s = tmp;
            QR.push_back(s);
        }
        
        bool a = 1;
        
        for (int j = 0; j < S; j++)
            if (find(QR.begin(), QR.end(), SE[j]) == QR.end()) {
               a = 0;
               break;                  
            }
            
        out << "Case #" << i + 1 << ": ";
            
        if (!a) { out << "0" << endl; continue; }
        
        int res = 0;
        
        set<string> all_SE; for (int j = 0; j < SE.size(); j++) all_SE.insert(SE[j]);
        set<string> tmp_SE = all_SE;
        
        for (int j = 0; j < QR.size(); j++) {
            tmp_SE.erase(QR[j]);
            
            if (tmp_SE.size() == 0) {
               res++;
               tmp_SE = all_SE;
               tmp_SE.erase(QR[j]);
            }
        }
        
        out << res << endl;
    }
    
    return 0;
}
