#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

main () {
  string line,m;
  int i=1,n;
  ofstream ofile;
  ifstream myfile ("A-small-attempt3.in");
  ofile.open ("bhavesh_output.in");
  if (myfile.is_open())
  {
     myfile>>n;     getline (myfile,m); 
    while ( !myfile.eof() && i<=n)
    {
       getline (myfile,line);
       const char *p = line.c_str();
       ofile<<"Case #"<<i<<": ";
     while (*p != '\0') 
     {  
        if(*p=='a') { ofile<<'y'; *p++; }
else if(*p=='b') { ofile<<'h'; *p++; }
else if(*p=='c') { ofile<<'e'; *p++; }
else if(*p=='d') { ofile<<'s'; *p++; }
else if(*p=='e') { ofile<<'o'; *p++; }
else if(*p=='f') { ofile<<'c'; *p++; }
else if(*p=='g') { ofile<<'v';  *p++; }
else if(*p=='h') { ofile<<'x'; *p++; }
else if(*p=='i') { ofile<<'d'; *p++; }
else if(*p=='j') { ofile<<'u'; *p++; }
else if(*p=='k') { ofile<<'i'; *p++; }
else if(*p=='l') { ofile<<'g'; *p++; }
else if(*p=='m') { ofile<<'l';  *p++; }
else if(*p=='n') { ofile<<'b';  *p++; }
else if(*p=='o') { ofile<<'k'; *p++; }
else if(*p=='p') { ofile<<'r'; *p++; }
else if(*p=='q') { ofile<<'z'; *p++; }
else if(*p=='r') { ofile<<'t'; *p++; }
else if(*p=='s') { ofile<<'n';  *p++; }
else if(*p=='t') { ofile<<'w';  *p++; }
else if(*p=='u') { ofile<<'j';  *p++; }
else if(*p=='v') { ofile<<'p'; *p++; }
else if(*p=='w') { ofile<<'f'; *p++; }
else if(*p=='x') { ofile<<'m';  *p++; }
else if(*p=='y') { ofile<<'a';  *p++; }
else if(*p=='z') { ofile<<'q';  *p++; }
      else {
          ofile<<*p; *p++; 
           }
     
     }cout << endl;
     ofile<<endl;
     i++;
     
    }
    myfile.close();
    ofile.close();
  }

  else cout << "Unable to open file"; 

}
