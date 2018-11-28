#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

int main() {
    ifstream in("A-large.in");
    ofstream out("LargeOutput.txt");
    
    int T=0, N=0, M=0;
    int dir=0;
    bool found=false;
    
    vector<string> path;
    string s;
    stringstream str;
    string chk;
    
     getline(in, s);
     str << s;
     str >> T;
     
     for(int i=0; i<T; i++) {
             s.erase();
             str.clear();
             path.clear();
             dir=0;
             found=false;
             getline(in, s);
             str << s;
             str >> N;
             str >> M;
             
             for(int j=0; j<N; j++) {
                     s.erase();
                     getline(in, s);
                     path.push_back(s);
                     }
             
             for(int k=0; k<M; k++) {
                     s.erase();
                     chk.erase();
                     getline(in, s);
                     for(int h=1; h<s.length(); h++) {
                             found = false;
                             if( (s[h] == '/') || (h == s.length() - 1)) {
                               if(s[h] == '/')
                               chk = s.substr(0,h);
                               else
                               chk = s.substr(0,h+1);
                               
                                //cout << "chk " << chk << endl;
                               for(int w=0; w<path.size(); w++) {
                                       if(chk == path[w]){
                                              found=true;
                                              break;
                                              } // end of chk 
                                       } // end of w for
                               if(!found) {
                                          path.push_back(chk);
                                          dir++;
                                          } // end of !found
                                       
                              }  // end of if s[h]
                               }     // end of s.length();
                     } // end of for M
                     out << "Case #" << (i+1) << ": " << dir << endl;
             } // end of for T
 //char ch;
 //cin >> ch;
} // end of main();
