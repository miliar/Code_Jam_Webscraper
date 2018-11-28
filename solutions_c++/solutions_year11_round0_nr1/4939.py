#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <map>
#include <vector>
#include <string.h>

using namespace std;

int main(int argc, char *argv[]){
  char*cpToken;  
  char buffer[400];    
  ifstream input("A-small-attempt0.in");
  ofstream output("out.out");
  input.getline(buffer,400);
  int casos =atoi(buffer);
  for(int i=1;i<casos+1;i++){
    vector<int> O;
    vector<int> B;
    vector<char> secuencia;
    if(!input.eof() && input.good()){
      input.getline(buffer,400);
      cpToken = strtok(buffer," ,.-\n");
      int botones=atoi(cpToken);
      for(int j=0;j<botones;j++){
        cpToken = strtok(NULL," ,.-\n");          
        char c = cpToken[0];
        cpToken = strtok(NULL," ,.-\n");          
        if(c=='O'){          
          O.push_back(atoi(cpToken));          
          secuencia.push_back('O');          
        }if(c=='B'){          
          B.push_back(atoi(cpToken));            
          secuencia.push_back('B');
        }
        
      } 
    }
    int resp=0;
    int flag=0;
    int posO=1;int o=0;
    int posB=1;int b=0;
    int pasitos=0;

    while(pasitos!=(int)secuencia.size()){
      flag=1;
      if(O.size()>0)
        if(posO<O[o])
          posO++;
        else
          if(posO>O[o])
            posO--;
          else
            if(posO==O[o])
              if(secuencia[pasitos]=='O'){              
                pasitos++;o++;
                flag=0;
              }
      
      if(B.size()>0)
        if(posB<B[b]){
          posB++; 
        }else
          if(posB>B[b]){
            posB--;   
          }else
            if(flag)
            if(posB==B[b])
              if(secuencia[pasitos]=='B'){
                pasitos++;b++;
              }

      resp++;
    }



    //salida
    output << "Case #"<<i<<": "<<resp << endl;
    
  }
    output.close();
    input.close();      
    return 0;
}









//
