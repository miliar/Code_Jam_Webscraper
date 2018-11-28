#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream in("in.in");    
    ofstream out("out.out");    
    
    long long num;
    char c[4][4];
    
    in>>num;
    
    for(long long k=0;k<num;k++){
      bool full=true;
      for(int x=0;x<4;x++){
        for(int y=0;y<4;y++){              
          in>>c[x][y];
          if(c[x][y]=='.')full=false;
      }}      
      
      //rows
        bool xx2=true;
        bool oo2=true;
        bool xx3=true;
        bool oo3=true;
        bool xx=true;
        bool xx1=true;
        bool oo=true;
        bool oo1=true;
      
      for(int x=0;x<4;x++){
        xx=true;
        xx1=true;
        oo=true;
        oo1=true;
        
        for(int y=0;y<4;y++){
          if(c[x][y]!='X' && c[x][y]!='T') xx=false;       
          if(c[x][y]!='O' && c[x][y]!='T') oo=false;       
          if(c[y][x]!='X' && c[y][x]!='T') xx1=false;       
          if(c[y][x]!='O' && c[y][x]!='T') oo1=false;       
        }
        
        if(c[x][x]!='X' && c[x][x]!='T') xx2=false;       
        if(c[x][x]!='O' && c[x][x]!='T') oo2=false;       
        if(c[x][3-x]!='X' && c[x][3-x]!='T') xx3=false;
        if(c[x][3-x]!='O' && c[x][3-x]!='T') oo3=false;       
        
        
        if(xx || xx1 || oo || oo1){oo2=false;oo3=false;xx2=false;xx3=false;break;}
      }
      
      out<<"Case #"<<k+1<<": ";
      if(xx || xx1 || xx2 || xx3){
            out<<"X won"<<endl;
      }else if(oo || oo1 || oo2 || oo3){
            out<<"O won"<<endl;
      }else if(full){
        out<<"Draw"<<endl;      
            
      }else{
         out<<"Game has not completed"<<endl;   
      }
                  
      
    
    }

    system("PAUSE");
    return EXIT_SUCCESS;
}
