#include<iostream>
#include<cstring>

using namespace std;

char ekansh[100];



int main(void)
{
     
     int nr,ui=1,a;
     cin>>nr;
     while(nr!=0)
     {
                    nr=nr-1;
                  cin>>a;
     
     gets(ekansh);
     
     
     int length = strlen(ekansh);
    
    
    if(nr!=-1)
     cout<<"Case #"<<ui<<": ";
     ui++;
      
     
     for(int i=0;i<length;i++)
     {
             
             if(ekansh[i]=='a')
             cout<<'y';
             else if(ekansh[i]=='o')
             cout<<'k';
             else if(ekansh[i]=='u')
             cout<<'j'; 
              else if(ekansh[i]=='e')
             cout<<'o';
             else if(ekansh[i]=='j')
             cout<<'u'; 
              else if(ekansh[i]=='p')
             cout<<'r';
             else if(ekansh[i]=='m')
             cout<<'l'; 
             else if(ekansh[i]=='y')
             cout<<'a';
             else if(ekansh[i]=='s')
             cout<<'n'; 
              else if(ekansh[i]=='l')
             cout<<'g';
             else if(ekansh[i]=='c')
             cout<<'e'; 
              else if(ekansh[i]=='k')
             cout<<'i';
             else if(ekansh[i]=='d')
             cout<<'s';   
             else if(ekansh[i]=='n')
             cout<<'b';
             else if(ekansh[i]=='r')
             cout<<'t'; 
              else if(ekansh[i]=='x')
             cout<<'m';
             else if(ekansh[i]=='i')
             cout<<'d'; 
              else if(ekansh[i]=='b')
             cout<<'h';
             else if(ekansh[i]=='p')
             cout<<'r';  
             else if(ekansh[i]=='t')
             cout<<'w';
             else if(ekansh[i]=='h')
             cout<<'x'; 
              else if(ekansh[i]=='w')
             cout<<'f';
             else if(ekansh[i]=='f')
             cout<<'c'; 
              else if(ekansh[i]=='v')
             cout<<'p';
             else if(ekansh[i]=='g')
             cout<<'v';
              else if(ekansh[i]=='q')
             cout<<'z';
             else if(ekansh[i]=='z')
             cout<<'q';
             else if(ekansh[i]==' ')
             cout<<' ';
              }
              cout<<endl;
            
             
            
             
     }
     
     
     
             
     }
        
                
