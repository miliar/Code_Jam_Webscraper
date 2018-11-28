#include <cstdlib>
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main(int argc, char *argv[])
{   
    
    ifstream  in(argv[1],ios::in| ios::binary);
    if(!in)
	     {
		 cout<<"cannot open file";
	     return 1;
         }
    ofstream  out(argv[2],ios::out| ios::binary);
    int t;
    in>>t;//cout<<"test cases---------->"<<t<<endl;;
    int cases=0;
    while(cases<t)
          {   
              int r,c;
			  in>>r;in>>c;
              char mat[r][c];
			  int b=0,w=0;
              
              for(int i=0;i<r;i++)
              {
                    
              for(int j=0;j<c;j++)
                  {
                      char ch;
                      in>>ch;
                      while((ch!='.')&&(ch!='#'))in>>ch;
                      if(ch=='.'){mat[i][j]=ch;w++;}
                      if(ch=='#'){mat[i][j]=ch;b++;}
                     
                  }
               }    
               
              for(int i=0;i<r;i++)
              {
                    
              for(int j=0;j<c;j++)
                  {
                      if(mat[i][j]=='#'){
                                        if((mat[i][j+1]=='#')&&(mat[i+1][j]=='#')&&(mat[i+1][j+1]=='#'))
                                          {
                                            mat[i][j]='/';
                                            mat[i][j+1]='c';
                                            mat[i+1][j]='c';
                                            mat[i+1][j+1]='/';
                                            b=b-4;
                                          }
                                        }
                  }
              }
                         
             
          if(b==0){
          out<<"Case #"<<cases+1<<":"<<endl;
           for(int i=0;i<r;i++)
              {for(int j=0;j<c;j++)
                  if(mat[i][j]=='c')out<<"\\";
                   else out<<mat[i][j];
                   out<<endl;}
                  }
                     
         if(b!=0){
          out<<"Case #"<<cases+1<<":"<<endl;
          out<<"Impossible"<<endl;
                  
                  }
          cases++; 
          }

    
    return 1;
    
}
