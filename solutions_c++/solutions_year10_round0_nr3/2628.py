#include<iostream>
#include<fstream>
#include<string>
#include<conio.h>
#include<sstream>


using namespace std;

int main()

{
     string input_string,sub_str;
     int pos_space1=0,pos_space2=0,n,k,r,no_of_cases,i=0,q[1000],revenue=0,empty_seats,front_of_q=0,a,j;
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
               
               else if ( i % 2)
               {
                    pos_space1 = input_string.find(" ");
                    sub_str = input_string.substr(0,pos_space1);
                    istringstream ( sub_str ) >>r;
                    
                    pos_space2 = input_string.find(" ", pos_space1+1);
                    sub_str = input_string.substr(pos_space1,pos_space2);
                    istringstream ( sub_str ) >>k;
                    
                    sub_str = input_string.substr(pos_space2);
                    istringstream ( sub_str ) >>n;
                    
                    cout<<"r="<<r<<"..."<<"k="<<k<<"...."<<"n="<<n<<endl;
                    
               }
               
               else
               {
                   revenue=0;
                 if ((i)<=2*no_of_cases)
                   
                   {
                                        
                                        pos_space1=0;pos_space2=0;
                                      
                                   for(j=0;j<input_string.length();j++)
                                   {
                                                   
                                                   pos_space2=pos_space1;
                                                   pos_space1 = input_string.find(" ",pos_space1+1);
                                                   if(j==0)
                                                   {
                                                         sub_str = input_string.substr(0,pos_space1);
                                                   }
                                                   else
                                                   {
                                                         
                                                          sub_str = input_string.substr((pos_space2+1),(pos_space1-pos_space2-1));
                                                   }
                                                  
                                                    istringstream ( sub_str ) >>q[j];
                                                   if(pos_space1==input_string.length())
                                                   break;
                                                   
                                                   
                                   }
                               
                                        
                                front_of_q=0;
                                   
                                   for(j=0;j<r;j++)
                                   {
                                                
                                                   empty_seats=k;
                                                    for(a=0;a<n;a++)
                                                    {
                                                                 if(q[front_of_q]<=empty_seats)
                                                                 {
                                                                      empty_seats=empty_seats-q[front_of_q];
                                                                      revenue=revenue+q[front_of_q];
                                                                      front_of_q = (front_of_q +1)%n;
                                                                
                                                                 } 
                                                                 
                                                                 else
                                                                 {
                                                                     
                                                                     break;
                                                                     
                                                                 } 
                                                    } 
                                                    
                                                    
                                   }
                                   
                                   
                       cout<<"Case #"<<i/2<<": "<<revenue<<endl;
                       output_file<<"Case #"<<i/2<<": "<<revenue<<endl;
                                   
                   
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
