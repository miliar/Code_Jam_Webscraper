#include <iostream>
#include <string>

using namespace std;

void convgo(char& x){
     switch (x){
     case 'a':
          {
              x='y';
              break;
          }
     case 'b':
          {
              x='h';
              break;
          }
     case 'c':
          {
              x='e';
              break;
          }
     case 'd':
          {
              x='s';
              break;
          }
     case 'e':
          {
              x='o';
              break;
          }
     case 'f':
          {
              x='c';
              break;
          }
     case 'g':
          {
              x='v';
              break;
          }
     case 'h':
          {
              x='x';
              break;
          }
     case 'i':
          {
              x='d';
              break;
          }
     case 'j':
          {
              x='u';
              break;
          }
     case 'k':
          {
              x='i';
              break;
          }
     case 'l':
          {
              x='g';
              break;
          }
     case 'm':
          {
              x='l';
              break;
          }
     case 'n':
          {
              x='b';
              break;
          }
     case 'o':
          {
              x='k';
              break;
          }
     case 'p':
          {
              x='r';
              break;
          }
     case 'q':
          {
              x='z';
              break;
          }
     case 'r':
          {
              x='t';
              break;
          }
     case 's':
          {
              x='n';
              break;
          }
     case 't':
          {
              x='w';
              break;
          }
     case 'u':
          {
              x='j';
              break;
          }
     case 'v':
          {
              x='p';
              break;
          }
     case 'w':
          {
              x='f';
              break;
          }
     case 'x':
          {
              x='m';
              break;
          }
     case 'y':
          {
              x='a';
              break;
          }
     case 'z':
          {
              x='q';
              break;
          }    
     default:
             break;}     
     }

int main(int argc, char *argv[])
{
    int T,len,i=0,j=0;
    cin>>T;
    char G[100];
    cin.get();
    for(i=0;i<T;i++)
    {
            gets(G);
            len= strlen(G);
            for(j =0;j<len;j++)
            {
                    convgo(G[j]);
                    }
            cout<<"Case #"<<i+1<<": "<<G<<endl;
            }
    return 0;
}
