#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int main()
{
    int testcases;
    char G[101];
    char S[101];
    int i, j=1;
    char temp;
    ifstream fin;
    ofstream fout;
    
    fin.open("A-small-attempt0.in", ios::in);
    fout.open("A-small-attempt0.out", ios::out);
    
    fin>>testcases;
    fin.getline(G, 101);
    for(j=1;j<=testcases;j++)
    {
     fin.getline(G, 101);
     for(i=0; G[i]!='\0'; i++)
     {
             switch(G[i])
             {
              case 'y': S[i] = 'a';
              break;
              
              case 'n': S[i] = 'b';
              break;
              
              case 'f': S[i] = 'c';
              break;
              
              case 'i': S[i] = 'd';
              break;
              
              case 'c': S[i] = 'e';
              break;
              
              case 'w': S[i] = 'f';
              break;
              
              case 'l': S[i] = 'g';
              break;
              
              case 'b': S[i] = 'h';
              break;    

              case 'k': S[i] = 'i';
              break;
              
              case 'u': S[i] = 'j';
              break;
              
              case 'o': S[i] = 'k';
              break;
              
              case 'm': S[i] = 'l';
              break;
              
              case 'x': S[i] = 'm';
              break;
              
              case 's': S[i] = 'n';
              break;
              
              case 'e': S[i] = 'o';
              break;
              
              case 'v': S[i] = 'p';
              break;    
    
              case 'z': S[i] = 'q';
              break;
              
              case 'p': S[i] = 'r';
              break;
              
              case 'd': S[i] = 's';
              break;
              
              case 'r': S[i] = 't';
              break;
              
              case 'j': S[i] = 'u';
              break;
              
              case 'g': S[i] = 'v';
              break;
              
              case 't': S[i] = 'w';
              break;
              
              case 'h': S[i] = 'x';
              break;    

              case 'a': S[i] = 'y';
              break;
              
              case 'q': S[i] = 'z';
              break;
              
              case ' ': S[i] = ' ';
              break;
               
              }
              }
              S[i] = '\0';
              fout<<"Case #"<<j<<": "<<S<<"\n";
              }
              fout.close();
              fin.close();
              return 0;
}
