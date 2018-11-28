#include<iostream>
#include<fstream>
#include<string>

using namespace std;
int i,j,k,case_no;
char A[10000],B[100][100],ch;
string b;


main()
{ifstream fin;
 fin.open("input.txt");
 ofstream fout;
 fout.open("output.txt");
 fin>>case_no;
 getline(fin,b);
 for(i=0;i<case_no;i++)
   {fout<<"Case #"<<i+1<<": ";
    getline(fin,b);
    for(k=0;b[k]!='\0';k++)
       switch(b[k])    
          {case 'a' : fout<<"y";break;
           case 'b' : fout<<"h";break;
           case 'c' : fout<<"e";break;
           case 'd' : fout<<"s";break;
           case 'e' : fout<<"o";break;
           case 'f' : fout<<"c";break;
           case 'g' : fout<<"v";break;
           case 'h' : fout<<"x";break;
           case 'i' : fout<<"d";break;
           case 'j' : fout<<"u";break;
           case 'k' : fout<<"i";break;
           case 'l' : fout<<"g";break;
           case 'm' : fout<<"l";break;
           case 'n' : fout<<"b";break;
           case 'o' : fout<<"k";break;
           case 'p' : fout<<"r";break;
           case 'q' : fout<<"z";break;
           case 'r' : fout<<"t";break;
           case 's' : fout<<"n";break;
           case 't' : fout<<"w";break;
           case 'u' : fout<<"j";break;
           case 'v' : fout<<"p";break;
           case 'w' : fout<<"f";break;
           case 'x' : fout<<"m";break;
           case 'y' : fout<<"a";break;
           case 'z' : fout<<"q";break;
           case ' ' : fout<<" ";break;           
          }
          fout<<endl;
       } 
fin.close();
fout.close();          
}

      
      
      
      
      
      
