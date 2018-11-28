#include <fstream>
#include <cstdlib>
#include <cstring>
using namespace std;



int main()
{
    fstream in, out;
    int T, j=0;
    char *G, *S;
    
    in.open("input.in", ios::in);
        
    out.open("output.txt", ios::out);
    
    
    in>>T;
    in.getline(G,101);
    
    for(int i=0; i<T; i++){
            
            G=new char[101];
            
            in.getline(G,101);
                         
            out<<"Case #"<<1+i<<": "; 
            
            for(int j=0; j< strlen(G); j++){
                    
                    switch(G[j]){
                                
                                                  case 'a':
                                                       out<<'y';
                                                       break;
                                                  case 'b':
                                                       out<<'h';
                                                       break;
                                                  case 'c':
                                                       out<<'e';
                                                       break;
                                                  case 'd':
                                                       out<<'s';
                                                       break;
                                                  case 'e':
                                                       out<<'o';
                                                       break;
                                                  case 'f':
                                                       out<<'c';
                                                       break;
                                                  case 'g':
                                                       out<<'v';
                                                       break;
                                                  case 'h':
                                                       out<<'x';
                                                       break;
                                                  case 'i':
                                                       out<<'d';
                                                       break;
                                                  case 'j':
                                                       out<<'u';
                                                       break;
                                                  case 'k':
                                                       out<<'i';
                                                       break;
                                                  case 'l':
                                                       out<<'g';
                                                       break;
                                                  case 'm':
                                                       out<<'l';
                                                       break;
                                                  case 'n':
                                                       out<<'b';
                                                       break;
                                                  case 'o':
                                                       out<<'k';
                                                       break;
                                                  case 'p':
                                                       out<<'r';
                                                       break;
                                                  case 'q':
                                                       out<<'z';
                                                       break;
                                                  case 'r':
                                                       out<<'t';
                                                       break;
                                                  case 's':
                                                       out<<'n';
                                                       break;
                                                  case 't':
                                                       out<<'w';
                                                       break;
                                                  case 'u':
                                                       out<<'j';
                                                       break;
                                                  case 'v':
                                                       out<<'p';
                                                       break;
                                                  case 'w':
                                                       out<<'f';
                                                       break;
                                                  case 'x':
                                                       out<<'m';
                                                       break;
                                                  case 'y':
                                                       out<<'a';
                                                       break;
                                                  case 'z':
                                                       out<<'q';
                                                       break;
                                                  case ' ':
                                                       out<<' ';
                                                       break;
                                      }    
            
            }
                         
    out<<endl;
    delete [] G;

    }
    in.close();   
    out.close();
    
    
    return 0;
    
    }
