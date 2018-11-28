#include<iostream>
#include<fstream>
#include<string.h>
#include<stdlib.h>
using namespace std;
int main()
{
  int no_of_case,i,j=1;
  char line[120], line2[120]={},line3[120],temp[3];
  ifstream file;
  ofstream file2;
  file.open("input.txt");
  file2.open("output.txt");
  file>>no_of_case;
  file.getline(line,120);
  while(no_of_case)
  {
    file.getline(line,120);
    i=0;
    line2[0]='C';
    line2[1]='a';
    line2[2]='s';
    line2[3]='e';
    line2[4]=' ';
    line2[5]='#';
    line2[6]='\0';
    itoa(j,temp,10);
    strcat(line2,temp);

    line3[0]=':';
    line3[1]=' ';
    while(line[i]!='\0')
    {
     switch(line[i])
     {
      case 'y':
           line3[i+2]='a';
           i++;
           break;
      case 'n':
           line3[i+2]='b';
           i++;
           break;
      case 'f':
           line3[i+2]='c';
           i++;
           break;
      case 'i':
           line3[i+2]='d';
           i++;
           break;
      case 'c':
           line3[i+2]='e';
           i++;
           break;
      case 'w':
           line3[i+2]='f';
           i++;
           break;
      case 'l':
           line3[i+2]='g';
           i++;
           break;
      case 'b':
           line3[i+2]='h';
           i++;
           break;
      case 'k':
           line3[i+2]='i';
           i++;
           break;
      case 'u':
           line3[i+2]='j';
           i++;
           break;
      case 'o':
           line3[i+2]='k';
           i++;
           break;
      case 'm':
           line3[i+2]='l';
           i++;
           break;
      case 'x':
           line3[i+2]='m';
           i++;
           break;
      case 's':
           line3[i+2]='n';
           i++;
           break;
      case 'e':
           line3[i+2]='o';
           i++;
           break;
      case 'v':
          line3[i+2]='p';
           i++;
           break;
      case 'z':
         line3[i+2]='q';
           i++;
           break;
      case 'p':
           line3[i+2]='r';
           i++;
           break;
      case 'd':
           line3[i+2]='s';
           i++;
           break;
      case 'r':
          line3[i+2]='t';
           i++;
           break;
      case 'j':
          line3[i+2]='u';
           i++;
           break;
      case 'g':
       line3[i+2]='v';
           i++;
           break;
      case 't':
          line3[i+2]='w';
           i++;
           break;
      case 'h':
           line3[i+2]='x';
           i++;
           break;
      case 'a':
           line3[i+2]='y';
           i++;
           break;
      case 'q':
          line3[i+2]='z';
           i++;
           break;                                                                                                                   
      case ' ':
          line3[i+2]=' ';          
           i++;
           break; 
       }
    }               
  
    j++;
    no_of_case--;
  line3[i+2]='\0';
  strcat(line2,line3);
  file2<<line2;
  file2<<"\n";

  } 
  file.close();
  file2.close();

 return 0;
}
