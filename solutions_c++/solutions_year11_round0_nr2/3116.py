#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{    
   int T,C,D,N;
   char ch;
    ifstream  in(argv[1],ios::in| ios::binary);
	  if(!in)
	     {
		 cout<<"cannot open file";
	     return 1;
		 }
		 
   ofstream  out(argv[2],ios::out| ios::binary);
   in>>T;in.get(ch);
   //cout<<T<<" TEST CASES"<<endl;
   int test_cases=0;
   while(test_cases<T)
           {           
                      in>>C;//cout<<" COMBOS "<<C<<" ";
                      in.get(ch);
                      char trkset[3];
                      if(C==1)
                      {
                      for(int j=0;j<3;j++)
                            {
                            in.get(ch);
                            trkset[j]=ch;
                            }
                      
                      //for(int j=0;j<3;j++)cout<<trkset[j];  
                      }
                      in>>D;//cout<<" OPPOSE "<<D<<" ";
                      in.get(ch);
                      char oppset[2];
                      if(D==1)
                      {
                      for(int j=0;j<2;j++)
                            {
                            in.get(ch);
                            oppset[j]=ch;
                            }
                      
                     // for(int j=0;j<2;j++)cout<<oppset[j];  
                      }    
                      in>>N;//cout<<" CHARACTER SET "<<N<<" ";
                      in.get(ch);
                      char charset[N];
                      int cj=0,j=0;
                      if(N>0)
                      {
                      for( cj=0,j=0;cj<N;cj++,j++)
                            {
                            in.get(ch);
                            charset[j]=ch;
                            if(((charset[j-1]==trkset[0])&&(ch==trkset[1]))||((charset[j-1]==trkset[1])&&(ch==trkset[0])))
                              {
                             
                              charset[j-1]=trkset[2];
                              charset[j]=0;
                              j--;
                              }
                           
                                if((charset[j]==oppset[0])||(charset[j]==oppset[1]))
                                   {
                                   int flag=0;                                                
                                   if(charset[j]==oppset[0])flag =1;                                               
                                   for(int k=0;k<=j;k++)
                                       {
                                         if(charset[k]==oppset[flag])
                                           {
                                           for(int l=0;l<=j;l++)charset[l]=0;
                                           j=0;
                                           }
                                       }
                                   }
                                
                            }
                      
                      int flag=0;
                      out<<"Case #"<<test_cases+1<<": "<<"[";
                      for(int jd=0;jd<N;jd++){
                                           if(charset[jd]!=0)
                                           {
                                           if(flag==1)out<<", ";
                                           out<<charset[jd]; 
                                           flag=1;
                                           }
                                           
                                           }out<<"]";
                      } 
                      out<<endl;   
                      test_cases++;          
           
           }
   
    
     
    return 0;
}
