#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream in ("A-small-attempt1.in");
    ofstream out ("out.txt");
    char randomn;
    int T;
    in >> T;
    randomn = in.get();
    for(int i = 0;i < T; i++)
            {                 
              out << "Case #" << i+1 << ": ";
              char x;
              int counter = 0;
              while(0 == 0){  
              char x;
              x = in.get();
              counter ++;
              cout << counter;
              if(counter > 100){
                         break;
              }
              if(x == '\n'){
                   break;
                   }
                   if(x == 'a'){
                   out <<"y";
                    }
                    if(x == 'b'){
                         out <<"h";
                    }
                    if(x == 'c'){
                         out <<"e";
                    }
                    if(x == 'd'){
                         out <<"s";
                    }
                    if(x == 'e'){
                         out <<"o";
                    }
                    if(x == 'f'){
                         out <<"c";
                    }
                    if(x == 'g'){
                         out <<"v";
                    }
                    if(x == 'h'){
                         out <<"x";
                    }
                    if(x == 'i'){
                         out <<"d";
                    }
                    if(x == 'j'){
                         out <<"u";
                    }
                    if(x == 'k'){
                         out <<"i";
                    }
                    if(x == 'l'){
                         out <<"g";
                    }
                    if(x == 'm'){
                         out <<"l";
                    }
                    if(x == 'n'){
                         out <<"b";
                    }
                    if(x == 'o'){
                         out <<"k";
                    }
                    if(x == 'p'){
                         out <<"r";
                    }
                    if(x == 'q'){
                         out <<"z";
                    }
                    if(x == 'r'){
                         out <<"t";
                    }
                    if(x == 's'){
                         out <<"n";
                    }
                    if(x == 't'){
                         out <<"w";
                    }
                    if(x == 'u'){
                         out <<"j";
                    }
                    if(x == 'v'){
                         out <<"p";
                    }
                    if(x == 'w'){
                         out <<"f";
                    }
                    if(x == 'x'){
                         out <<"m";
                    }
                    if(x == 'y'){
                         out <<"a";
                    }
                    if(x == 'z'){
                         out <<"q";
                    }
                    if(x == ' '){
                         out <<" ";
                    }
              }
              out << "\n";
            }  
    return 0;
}

