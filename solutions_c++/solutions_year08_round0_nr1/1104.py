#include <iostream>
#include <cstdio>
#include <list>
#include <vector>
using namespace std;
vector<string> engine;
vector<string> word;
void read_engine(){
     int k;
     cin >> k;
     engine.clear();
     scanf("\n"); 
     for(int i =0;i<k;i++){             
             char u[1000];            
             gets(u);
             engine.push_back(u);                            
     }
}
void print_input(){
     for(unsigned int i =0; i<engine.size(); i++){
                  cout << engine[i] << endl;
     }     
}
void read_word(){
     int k;
     cin >> k;
     scanf("\n");
     word.clear();
     for(int i=0; i<k; i++){             
             char u[1000];                       
             gets(u);
             word.push_back(u);           
     }
}
void print_word(){
     for(unsigned int i=0; i<word.size(); i++){
             cout << word[i] << endl;             
     }     
}
void process(int test){
     int tmp = 0;
     int max = 0;
     int maxi = -1;
     int tmpnum;
     int sum = 0;
     unsigned int j;
     while(true){
          for(unsigned int i=0; i<engine.size(); i++){
                       tmpnum = 0;
                       for(j=tmp; j<word.size(); j++){                                    
                                    if(engine[i] == word[j]){                                                  
                                         break;
                                    }else{
                                          tmpnum++;                                          
                                    }                        
                       }  
                       if(tmpnum > max){
                                max = tmpnum;
                                maxi = j;  
                                //cout << i << " <<< "  << endl;        
                      }         
          }          
        //cout << max << " || " << maxi << endl;
        tmp = maxi;
        max = 0;
        sum++;
        if(max + maxi >= word.size()) break; 
        
          

          //break;            
     }     
     cout << "Case #" << test << ": " << sum-1 << endl;
}
int main(){
    int k;
    cin >> k;
    for(int i=1; i<=k; i++){
             read_engine();
             
             //cout << " ====== " << endl;
             //if(i == 11) print_input();    
             //cout << " ++++++ " << endl;
             read_word();     
             //if(i == 11) print_word(); 
             process(i);
             //break;   
    }    
    return 0;
}
