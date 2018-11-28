#include<iostream>
#include<fstream>
using namespace std;


int main()
{
 ifstream in("A-small-attempt2.in");
 ofstream out("output.txt");
 int N;
 char C;
 in>>N;
 
  string S;
  getline(in, S);

 for(int k=0; k<N; k++)
 {

  getline(in, S);
  char *line= new char[S.size()+1];
  strcpy(line, S.c_str());

//  for(int i= 0 ; i< S.size(); i++)
  //        cout<<line[i];
  //cout<<endl;
          out<<"Case #"<<k+1<<": ";  
  for(int i= 0 ; i< S.size(); i++)
  {

  switch(line[i])
           {
            case 'a':
                     out<<"y";
                     break;
                     
            case 'b':
                     out<<"h";
                     break;
            case 'c':
                     out<<"e";
                     break;
            case 'd':
                     out<<"s";
                     break;
            case 'e':
                     out<<"o";
                     break;
            case 'f':
                     out<<"c";
                     break;
            case 'g':
                     out<<"v";
                     break;
            case 'h':
                     out<<"x";
                     break;
            case 'i':
                     out<<"d";
                     break;
            case 'j':
                     out<<"u";
                     break;
            case 'k':
                     out<<"i";
                     break;
                                          
            case 'l':
                     out<<"g";
                     break;
            
            case 'm':
                     out<<"l";
                     break;
            
            case 'n':
                     out<<"b";
                     break;
            
            case 'o':
                     out<<"k";
                     break;
            
            case 'p':
                     out<<"r";
                     break;
            
            case 'q':
                     out<<"z";
                     break;
                     
            case 'r':
                     out<<"t";
                     break;
            case 's':
                     out<<"n";
                     break;

            case 't':
                     out<<"w";
                     break;

            case 'u':
                     out<<"j";
                     break;
                                                                                
            case 'v':
                     out<<"p";
                     break;

            case 'w':
                     out<<"f";
                     break;
                     
            case 'x':
                     out<<"m";
                     break;
                   
            case 'y':
                     out<<"a";
                     break;
                     
            case 'z':
                     out<<"q";
                     break;
                     
            default:         
                      out<<line[i];
                      break;
            }
 }
 out<<endl;
}
 return 0;
}
