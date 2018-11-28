/*
  Name: google code jam (round 1)
  Copyright: 
  Author: dipankar dutta
  Date: 12/09/09 17:07
  Description: 
*/
// istream get
#include <iostream>
#include <fstream>
#include<conio.h>
using namespace std;

int main () 
{       
    //&&&&&&&&&&&&&&&&&&&&&&&&& file hanhaling &&&&&&&&&&&&&&&&&&&&&&&&&&&
       ifstream in("input.in");
         if(!in)
         {cout<<"problem!! INPUT FILE CAN NOT BE OPEN !!!!!";
         getch();
         return 1;
         }   
         ofstream out("output.out");
          if(!out)
         {cout<<"problem!!OUTPUT FILE CAN NOT BE OPEN !!!!!";
         getch();
         return 1;
         }   
    //&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    //---------------------read input & extraction--------------------------------
         int testcase;
        
         in>>testcase;
         cout<<endl<<"welcome::TEST CASE=>"<<testcase<<" "<<endl;
         
         
       
         char array[100];
         
         //-------------------------------
         
         in.getline(array,50,'\n'); //set for avoid ist row as input line
 for (int t=0;t<testcase;t++)
 {   
             
             
             //--------------input - from file-------------------------
                         in.getline(array,65,'\n');
                         //###########################end of logic#############################
          
        //char array[]="123456789abcdefgh";
       
        int len=strlen(array);cout<<len<<endl;
        char dlist[len];
        
        for(int i=0;i<len ;i++)
        dlist[i]='*';
        
          int distinct=0;
          for(int i=0;i<len;i++)
          {   int found=0;
              for(int j=0;j<len;j++)
             {  
                 if(array[i]==dlist[j])
                  { found=1;
                    break;
                  }    
             }
             if(found==0)
             {dlist[distinct++]=array[i];
             }    
         }  
        /* for(int i=0;i<len;i++)
         cout<<dlist[i]; */
       
         cout<<endl<<distinct<<endl;
         int assign[distinct];
         //******assign------------
         assign[0]=1;
         for(int d=1,val=0;d<distinct;val++)
         {  if(val!=1)
             {assign[d]=val;
              d++;
             }    
         } 
         for(int i=0;i<len;i++)
         cout<<array[i];
         cout<<endl;
         for(int i=0;i<len;i++)
         cout<<dlist[i];
         cout<<endl;
         for(int i=0;i<distinct;i++)
         cout<<assign[i];
         
       //-cal
         long long output=0;
         if(distinct==1)
         { 
             for(int i=0;i<len;i++)
             output+=pow(2.0,i);  
         }
         else
         {    
                 for(int r=len-1,exp=0;r>=0;r=r-1,exp++)
                 {   int weight=0;
                     for(int j=0;j<distinct;j++)
                     { if(array[r]==dlist[j])
                        { weight=assign[j];cout<<endl<<array[r]<<"-->"<<weight;
                          break;
                        }
                     }            
                   double temp=pow(distinct,double(exp));
                   output=output+weight*temp;  
                 }   
                  
         }  cout<<endl<<output<<endl;            
          
          
          
          
          
          
          
          
             
           //###########################end of logic#############################
      
                      
                   
           //###########################end of logic#############################
           out<<"Case #"<<(t+1)<<": "<<output<<endl;
          
  }//end of test case loop        

     
     
     
      
     
      
         
       
     
            
//------------------------end of main problem-----------------------------------
         
         
         
in.close();
getch();
  return 0;
}
