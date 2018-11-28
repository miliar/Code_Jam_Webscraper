#include <iostream>
#include <fstream>
#include <string>
using namespace std;

char translator(char a) //Translator function, works by passing a single char
{
  if (a=='y') {return 'a';}    // replace cases
  if (a=='n') {return 'b';}
  if (a=='f') {return 'c';}
  if (a=='i') {return 'd';}
  if (a=='c') {return 'e';}
  if (a=='w') {return 'f';}
  if (a=='l') {return 'g';}
  if (a=='b') {return 'h';}
  if (a=='k') {return 'i';}
  if (a=='u') {return 'j';}
  if (a=='o') {return 'k';}
  if (a=='m') {return 'l';}
  if (a=='x') {return 'm';}
  if (a=='s') {return 'n';}
  if (a=='e') {return 'o';}
  if (a=='v') {return 'p';}
  if (a=='z') {return 'q';}
  if (a=='p') {return 'r';}
  if (a=='d') {return 's';}
  if (a=='r') {return 't';}
  if (a=='j') {return 'u';}
  if (a=='g') {return 'v';}
  if (a=='t') {return 'w';}
  if (a=='h') {return 'x';}
  if (a=='a') {return 'y';}
  if (a=='q') {return 'z';}
  if (a=='Y') {return 'A';}
  if (a=='N') {return 'B';}
  if (a=='F') {return 'C';}
  if (a=='I') {return 'D';}
  if (a=='C') {return 'E';}
  if (a=='W') {return 'F';}
  if (a=='L') {return 'G';}
  if (a=='B') {return 'H';}
  if (a=='K') {return 'I';}
  if (a=='U') {return 'J';}
  if (a=='O') {return 'K';}
  if (a=='M') {return 'L';}
  if (a=='X') {return 'M';}
  if (a=='S') {return 'N';}
  if (a=='E') {return 'O';}
  if (a=='V') {return 'P';}
  if (a=='Z') {return 'Q';}
  if (a=='P') {return 'R';}
  if (a=='D') {return 'S';}
  if (a=='R') {return 'T';}
  if (a=='J') {return 'U';}
  if (a=='G') {return 'V';}
  if (a=='T') {return 'W';}
  if (a=='H') {return 'X';}
  if (a=='A') {return 'Y';}
  if (a=='Q') {return 'Z';}
  
  else return a;  // for everything else like numbers and special
}

int main()
{ int T=0; int temp=0; string G; char pass;
  ifstream in("A-small-attempt0.in");
  
  in>>temp;getline(in,G);
  if (temp<=30 && temp>=1)
  {T=temp;}
  else
  {cout<<"Input Error: T";}
  
  fstream f;                      
  f.open("output.txt");
  
  for(int j=1;j<=T;j++)
  {getline(in,G);
   f<<"Case #"<<j<<": ";

  for(int i=0;i<G.size(); i++)
  { f.put(translator(G[i])); }
   
  f<<"\n";   
  
  }
   
  f.close();
  
  system("pause");
  return 0;
}
