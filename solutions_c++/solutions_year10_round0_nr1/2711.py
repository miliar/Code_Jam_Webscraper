#include<iostream>
#include<fstream>
#include<string>
#include<conio.h>
#include<sstream>


using namespace std;

int r(int n)
{
    if (n==1)
       return 1;
    else
        return ((2*r(n-1))+1);
}

int main()

{
     string input_string,sub_str;
     int pos_space=0,n,k,no_of_cases,i=0,min_req;
    // char cstr[10];
     ifstream input_file ("input.in");
     ofstream output_file ("output.txt");
     if (input_file.is_open())
     {
             while(! input_file.eof())
             {
               getline(input_file,input_string);
               cout<<input_string<<endl;            //del this line
               
               
               if (i==0)
               {
                  istringstream ( input_string ) >> no_of_cases;
               }
               
               else
               {
                 if ((i)<=no_of_cases)
                   
                      {
                   
                   
                                   pos_space = input_string.find(" ");
                
                                   sub_str = input_string.substr(0,pos_space);
                                       
                                   istringstream ( sub_str ) >>n;
                  
                                        
                                   sub_str = input_string.substr(pos_space+1);
                                        
                                   istringstream ( sub_str ) >>k;
                                        
                                   cout<<n<<"and"<<k<<endl;
                   
                                   cout<<"Case #"<<i<<":";
                                   output_file<<"Case #"<<i<<":";
                                   
                                   min_req=r(n);
                                   cout<<min_req;
                                   
                                   if((k+1) % (min_req+1))
                                   {
                                            cout<<" OFF"<<endl;
                                            output_file<<" OFF"<<endl;
                                   }
                                   
                                   else
                                   {
                                       cout<<" ON"<<endl;
                                       output_file<<" ON"<<endl;
                                   }
                   
                                   
                       
                                   
                   
                      }
                       
                   
                   
                   
                       
               }
               
               i++;
               
               
               
            
             
               
             }
             
             
             input_file.close();              
     }
     
     else
     {
         cout<<"\nUnable to open input file for reading\n";
     
     }
     
     
   
   getch();
   
   return 0;  
}
