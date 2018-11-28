#include <stdlib.h>
#include <fstream>
#include <iostream>

int main(int argc, char** argv)
{
  std::ifstream f1;
  std::ofstream f2;
  
  f1.open("A-small-0.in");
  f2.open("A-small-0.out");
  
  int T, R, C;
  bool flag;
  char image[50][50];
  
  f1>>T;
  
  for (int i=0; i<T; i++)
      {
        f1>>R>>C;
        
        flag=true;
        
        for (int j=0; j<R; j++)
            {
              for (int k=0; k<C; k++)
                  f1>>image[j][k];
            }
        
        for (int j=0; ((j<R) && (flag==true)); j++)
            {
              for (int k=0; ((k<C) && (flag==true)); k++)
                  {
                    if (image[j][k]=='#')
                       {
                         if ((image[j][k+1]=='#') && (image[j+1][k]=='#') && (image[j+1][k+1]=='#'))
                            {
                              image[j][k]=image[j+1][k+1]='/';
                              image[j][k+1]=image[j+1][k]='\\';
                            }
                         else
                             flag=false;
                       }
                  }
            }
         
         f2<<"Case #"<<(i+1)<<":"<<std::endl;
         
         if (flag==true)
            {
              for (int j=0; j<R; j++)
                  {
                    for (int k=0; k<C; k++)
                        f2<<image[j][k];
                    f2<<std::endl;
                  }
            }
         else
             f2<<"Impossible"<<std::endl;
      }
  return (EXIT_SUCCESS);
}
