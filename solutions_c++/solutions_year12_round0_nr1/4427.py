#include<iostream>
#include<fstream>
#include<stdlib.h>

using namespace std;

ifstream myfile("c:/users/chaturvedi/desktop/small.in");
void find();
void calc();
char arr[200];
int T,N=0;
char letter;
main()
{
      find();
}     

void find()
{
      cout<<"the contents of file are : ";
      while(1)
      {
      myfile.get(letter);
      if(letter!=10)
      T=(T*10)+((int) letter)-48;
      else
      break;
      cout<<T<<"\n";                     
      }
      for(int lp=0;lp<T;lp++)
      {
      myfile.getline(arr,200);
      calc();
      }
}

void calc()
{
     for(int lp=0;arr[lp]!='\0';lp++)
     {
             switch(arr[lp])
             {
             case 'a':arr[lp]='y';
                      break;
             case 'b':arr[lp]='h';
                      break;
             case 'c':arr[lp]='e';
                      break;
             case 'd':arr[lp]='s';
                      break;
             case 'e':arr[lp]='o';
                      break;
             case 'f':arr[lp]='c';
                      break;
             case 'g':arr[lp]='v';
                      break;
             case 'h':arr[lp]='x';
                      break;
             case 'i':arr[lp]='d';
                      break;
             case 'j':arr[lp]='u';
                      break;
             case 'k':arr[lp]='i';
                      break;
             case 'l':arr[lp]='g';
                      break;
             case 'm':arr[lp]='l';
                      break;
             case 'n':arr[lp]='b';
                      break;
             case 'o':arr[lp]='k';
                      break;
             case 'p':arr[lp]='r';
                      break;
             case 'q':arr[lp]='z';
                      break;
             case 'r':arr[lp]='t';
                      break;
             case 's':arr[lp]='n';
                      break;
             case 't':arr[lp]='w';
                      break;
             case 'u':arr[lp]='j';
                      break;
             case 'v':arr[lp]='p';
                      break;
             case 'w':arr[lp]='f';
                      break;
             case 'x':arr[lp]='m';
                      break;
             case 'y':arr[lp]='a';
                      break;
             case 'z':arr[lp]='q';
                      break;
             }
     }
      ofstream outfile("c:/users/chaturvedi/desktop/out.in",ios::app);
      N++;
      outfile<<"Case #";
      outfile<<N;
      outfile<<": ";
      outfile<<arr;
      outfile<<"\n";
      if(myfile.eof()!=0)
      {
      myfile.close();
      outfile.close();
      exit(0);
      }     
}
