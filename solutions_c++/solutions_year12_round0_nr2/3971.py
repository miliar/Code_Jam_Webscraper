#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream in ("B-large.in");
    ofstream out ("out.txt");
    int T;
    in >> T;
    for(int i = 0; i < T; i++){
            
            int ti; //number of scores
            int s; //number of surprise scores
            int p; //scores to pass
            in >> ti;
            in >> s;
            in >> p;
            int scores[ti];
            int passed = 0;
            
            for(int ii = 0; ii < ti; ii++){
                    in >> scores[ii];
                    
                    if(scores[ii]%3 == 0){
                                    if((scores[ii]/3) >= p){
                                    passed++;
                                    }
                                    if(p - (scores[ii]/3) == 1 && s != 0 && scores[ii] != 0){
                                    s--;
                                    passed++;
                                    }
                    }
                    if(scores[ii]%3 == 2){
                                    if((scores[ii]+1)/3 >= p){
                                    passed++;
                                    }                
                                    if(p - ((scores[ii]+1)/3) == 1 && s != 0){
                                    s--;
                                    passed++;
                                    }               
                    }
                    if(scores[ii]%3 == 1){  
                                    if((scores[ii]+2)/3 >= p){
                                    passed++;
                                    }
                    } 
            }           
            out << "Case #" << i+1 << ": "<< passed <<"\n";
    }                     
    return 0;
}        
            
    
