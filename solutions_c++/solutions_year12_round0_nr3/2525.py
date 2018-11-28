#include <cstdlib>
#include <iostream>
#include <fstream>
#include<conio.h>
#include <string>
#include <math.h>
using namespace std;

int main(int argc, char *argv[])
{
    using std::string;
   using std::cout;
   using std::endl;
   using std::replace;
   
    ifstream  in(argv[1],ios::in| ios::binary);
    ifstream file(argv[1],ios::in| ios::binary);
    if(!in)
	     {
		 cout<<"cannot open file";
	     return 1;
         }
    ofstream  out(argv[2],ios::out| ios::binary);
    int t;
    in>>t;
    int cases=0;
    int a,b,c,x,s;
    
    while(cases<t)
          {      
                  s=0;
                  in>>a;
                  in>>b;
                 
                  for(x=a;x<b;x++)
                  {
                   int arr[1000]; //holding temps
                   int ct=0;
                  int flag=0;
                  c=floor(log10(x));//cout<<c;cout<<"number"<<x<<endl;
                  int div=10;
                     for(int i=1;i<=c;i++)
                     {        
                           
                             int temp=floor(x%div);
                             
                             int temp2=floor(x/div);
                             int temp3=temp*floor(pow(10,c-i+1))+temp2;
                             if((temp3>x)&&(temp3<=b))
                                     {
                                          for(int j=0;j<ct;j++)
                                          {
                                                  if(arr[j]==temp3){flag=1;break;}
                                          }        
                                          if(flag==0)            
                                           {
                                           s++;//out<<x<<"---"<<temp3<<" ";
                                           arr[ct]=temp3;ct++;
                                           }
                                     flag=0;
                                     }
                                     
                        div=div*10;     
                             
                     }
                     //cout<<endl;
                  }
                  
                  cases++;
                  out<<"Case #"<<cases<<": "<<s<<endl;
                  
          }

    
    return 1;
    
}
