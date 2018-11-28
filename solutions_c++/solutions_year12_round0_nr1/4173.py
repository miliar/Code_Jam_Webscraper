#include<iostream>
#include<fstream>
#include<stdlib.h>
using namespace std;
ifstream afile("c:/users/vaibhav/desktop/small.in");
void get_data();
void solve();
char lines[106];
int t,j=0;
char ch;
main()
{
      get_data();
}     

void get_data()
{
      cout<<"the contents of file are : ";
      while(1)
      {
      afile.get(ch);
      if(ch!=10)
      t=(t*10)+((int) ch)-48;
      else
      break;
      cout<<t<<"\n";                     
      }
      for(int k=0;k<t;k++)
      {
      afile.getline(lines,105);
      solve();
      }
}

void solve()
{
     for(int k=0;lines[k]!='\0';k++)
     {
             switch(lines[k])
             {
             case 'a':lines[k]='y';
                      break;
             case 'b':lines[k]='h';
                      break;
             case 'c':lines[k]='e';
                      break;
             case 'd':lines[k]='s';
                      break;
             case 'e':lines[k]='o';
                      break;
             case 'f':lines[k]='c';
                      break;
             case 'g':lines[k]='v';
                      break;
             case 'h':lines[k]='x';
                      break;
             case 'i':lines[k]='d';
                      break;
             case 'j':lines[k]='u';
                      break;
             case 'k':lines[k]='i';
                      break;
             case 'l':lines[k]='g';
                      break;
             case 'm':lines[k]='l';
                      break;
             case 'n':lines[k]='b';
                      break;
             case 'o':lines[k]='k';
                      break;
             case 'p':lines[k]='r';
                      break;
             case 'q':lines[k]='z';
                      break;
             case 'r':lines[k]='t';
                      break;
             case 's':lines[k]='n';
                      break;
             case 't':lines[k]='w';
                      break;
             case 'u':lines[k]='j';
                      break;
             case 'v':lines[k]='p';
                      break;
             case 'w':lines[k]='f';
                      break;
             case 'x':lines[k]='m';
                      break;
             case 'y':lines[k]='a';
                      break;
             case 'z':lines[k]='q';
                      break;
             }
     }
      ofstream bfile("c:/users/vaibhav/desktop/small_out.in",ios::app);
      j++;
      bfile<<"Case #";
      bfile<<j;
      bfile<<": ";
      bfile<<lines;
      bfile<<"\n";
      if(afile.eof()!=0)
      {
      afile.close();
      bfile.close();
      exit(0);
      }     
}
