#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
  ifstream ifs("A-small-attempt1.in");
  ofstream ofs("output");
  string buf,sbuf;
  int i=0,j;
  ifs >> j;

  getline(ifs,buf);//i=0
  for(i=1;i<j+1;i++){
    getline(ifs,buf);
    ofs << "Case #" << i << ": ";
    for(int k=0;k<buf.size();k++){
      switch (buf[k]-'a'){
      case 0: ofs << 'y'; break; 
      case 1: ofs << 'h'; break; 
      case 2: ofs << 'e'; break; 
      case 3: ofs << 's'; break; 
      case 4: ofs << 'o'; break; 
      case 5: ofs << 'c'; break; 
      case 6: ofs << 'v'; break; 
      case 7: ofs << 'x'; break;
      case 8: ofs << 'd'; break; 
      case 9: ofs << 'u'; break; 
      case 10: ofs << 'i'; break; 
      case 11: ofs << 'g'; break; 
      case 12: ofs << 'l'; break; 
      case 13: ofs << 'b'; break; 
      case 14: ofs << 'k'; break; 
      case 15: ofs << 'r'; break; 
      case 16: ofs << 'z'; break; 
      case 17: ofs << 't'; break;
      case 18: ofs << 'n'; break; 
      case 19: ofs << 'w'; break; 
      case 20: ofs << 'j'; break; 
      case 21: ofs << 'p'; break; 
      case 22: ofs << 'f'; break; 
      case 23: ofs << 'm'; break; 
      case 24: ofs << 'a'; break; 
      case 25: ofs << 'q'; break; 
      default : ofs << ' ';break;
      }
    }
    ofs << endl;
  }

  return 0;
}
