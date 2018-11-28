#include <cstdio>
#include <cmath>
#include <cctype>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
int main()
{
          int i,j,T,N;
          freopen("input7.txt","r",stdin);
          freopen("out6.txt","w",stdout);
          char s[31][101], a[31][101];
          scanf("%d\n",&T);
          for (i=1; i<=T; i++)
          {
                    gets(s[i]);
                    cout<<"Case #"<<i<<": ";
                    for (j=0; j<strlen(s[i]); j++)
                    {
                    a[i][j]=s[i][j];
                         switch(s[i][j])
                         {
                                     case 'y': a[i][j]='a'; break;
                                     case 'n': a[i][j]='b';break;
                                     case 'f': a[i][j]='c';break;
                                     case 'i': a[i][j]='d';break;
                                     case 'c': a[i][j]='e';break; 
                                     case 'w': a[i][j]='f'; break;  
                                     case 'l': a[i][j]='g';break;
                                     case 'b': a[i][j]='h';break;
                                     case 'k': a[i][j]='i';break;
                                     case 'u': a[i][j]='j';break;
                                     case 'o': a[i][j]='k';break;
                                     case 'm': a[i][j]='l';break;
                                     case 'x': a[i][j]='m';break;
                                     case 's': a[i][j]='n';break;
                                     case 'e': a[i][j]='o';break;
                                     case 'v': a[i][j]='p';break;
                                     case 'z': a[i][j]='q';break;
                                     case 'p': a[i][j]='r';break;
                                     case 'd': a[i][j]='s';break;
                                     case 'r': a[i][j]='t';break;
                                     case 'j': a[i][j]='u';break;
                                     case 'g': a[i][j]='v';break;
                                     case 't': a[i][j]='w';break;
                                     case 'h': a[i][j]='x';break;
                                     case 'a': a[i][j]='y';break;
                                     case 'q': a[i][j]='z';break;
                         }
                         cout<<a[i][j];
                    }
                    cout<<endl;
          }
          //system("pause");
          return 0;
}
