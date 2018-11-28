# include <iostream>
# include <cstdio>
# include <vector>
# include <algorithm>
# include <fstream>
# include <map>

using namespace std;

bool isOpposed(const string &invoke, char ch, map<char, char> opposed){
                     
                     for(int i = 0; i < invoke.size() ; ++i){
                             if(opposed[invoke[i]] == ch || opposed[ch] == invoke[i]){
                                  return true;
                                  }                                  
                             }
                             return false;
     }

int main()
{
    ifstream in("B-small-attempt0.in");
    ofstream out("B-small-output");
 
    int T, cas = 0;
    in>>T;
    
    while(T--){
               
               int C, D, N;
               map<string, char> nonbase;
               map<char, char> opposed;
               string invoke = "";
               string input;
               
               in>>C;
               
               for (int i = 0; i < C; ++i) {
                       string inp;
                       in>>inp;
                       string t = inp.substr(0, inp.size()-1);
                       nonbase[t] = inp[2];
                       reverse(t.begin(), t.end());
                       nonbase[t] = inp[2];                       
                       }
                     
               in>>D;  
               for (int i = 0; i < D; ++i) {
                       string inp;
                       in>>inp;
                       opposed[inp[0]] = inp[1];
                       opposed[inp[1]] = inp[0];  
                       }

               in>>N;
               in>>input;
               
               for (int i = 0; i < input.size(); ++i) {

                        if (invoke.empty()) {
                              invoke += input[i];
                              continue;
                              }    
                              
                        string t =  invoke.substr(invoke.size()-1) + input[i] ;
                        if ( nonbase[t] != '\0' ) {
                                        invoke[invoke.size()-1] = nonbase[t];
                              }
                        else if (reverse(t.begin(), t.end()), nonbase[t] != '\0') {
                                        invoke[invoke.size()-1] = nonbase[t];                             
                             }
                        else if (isOpposed(invoke, input[i], opposed)) {
                                invoke = "";
                             }
                        else invoke += input[i];
                       }        
               
               out<<"Case #"<<++cas<<": ";
               out<<"[";
               for(int i = 0; i < invoke.size(); ++i){
                       out<<invoke[i];
                       if (i != invoke.size() -1 ) {
                            out<<", ";
                            }
                       }
               out<<"]"<<endl;
               }
    
 return 0;   
}
