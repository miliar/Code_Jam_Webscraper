#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    
    ifstream in("A-large.in");
    ofstream out("Wireoutput.txt");
    int T=0, N=0;
    int p[1000][2];
    int inter=0;
    
    string s;
    stringstream str;
    
    getline(in, s);
    str << s;
    str >> T;
    
    for(int i=0; i<T; i++) {
            s.erase();
            str.clear();
            inter =0;
            getline(in, s);
            str << s;
            str >> N;
            
            for(int j=0; j<N; j++) {
                    s.erase();
                    str.clear();
                    getline(in, s);
                    str << s;
                    str >> p[j][0];
                    str >> p[j][1];        
                    } // end of for N
            
            for(int k=0; k<N; k++) {
                    for(int h=(k+1); h<N; h++) {
                            
                            if((p[k][0] > p[h][0]) && (p[k][1] < p[h][1])) inter++;
                            if((p[k][0] < p[h][0]) && (p[k][1] > p[h][1])) inter++;
                            } // end of for h
                            } // end of for k
            
            out << "Case #" << (i+1) << ": " << inter << endl;
            
            } // end of for T
 
    
} // end of main
