#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cmath>
#include <vector>

using namespace std;

void outputMap(map<string, int> Map){
  map<string,int>::iterator it;
  cout<<"Map: "<<endl;
  for ( it=Map.begin() ; it != Map.end(); it++ ){
    cout<<"    "<<it->first<<" "<<it->second<<endl;      
  }
}

int main(){
  
  //read the N - number of cases (first line of file)    
  int N;
  ifstream infile;
  infile.open("A-large.in");
  infile>>N; 
  ofstream outfile;
  outfile.open("A-large.out");
   
  string line;
  
  //loop through the file
  for (int i=1; i<=N; i++){
    map<string, int> Map;
    //read search engines
    int S;
    string strS;
    infile>>S;    
    string engine;
    string crap;
    for (int j=0; j<=S; j++){
      getline(infile, engine);      
      if (engine.size()!=0) {
        Map[engine] = 0;        
      }
    }
    //outputMap(Map);
    
    int Q;
    infile>>Q;    
    string query;       
    int limit = S;
    //cout<<"limit"<<limit<<endl;
    int num = 0;
    int jumps = 0;  
    
    for (int m =0; m<=Q; m++){
      getline(infile,query); 
      if (query.size()!=0) {//if it is not empty line
        if (num!=limit){//if all engines haven't been checked
          //check the query
          if (Map[query]==0) {//if its zero (new engine in this loop)
            Map[query]++; //check it
            num++; // and increase the count of engines which have gone through
          }
        }
        if (num==limit){//if there is only one space free left
          jumps++; //jump happens
          //erase/set counts to zero
          map<string,int>::iterator it;
          for ( it=Map.begin(); it != Map.end(); it++ ){
             it->second = 0;      
           }
          Map[query]++; //increase the count of current engine
          num = 1;
        }    
      }
      //cout<<"Querry "<<query<<" Num "<<num<<endl;
      //outputMap(Map);
    }
   
    cout<<"Case #"<<i<<": "<<jumps<<endl; 
    outfile<<"Case #"<<i<<": "<<jumps<<endl; 
  
  }
  infile.close();
  outfile.close();
  
  cin.ignore(256, '\n');
  cout << "Press ENTER to continue..." << endl;
  cin.get();
}
