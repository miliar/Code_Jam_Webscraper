// istream get
#include <iostream>
#include <fstream>
#include<conio.h>
using namespace std;

int main () 
{ ifstream in("A-small-attempt5.in");
         if(!in)
         {cout<<"problem!! INPUT FILE CAN NOT BE OPEN !!!!!";
         getch();
         return 1;
         }   
         ofstream out("A-small-attempt5.out");
          if(!out)
         {cout<<"problem!!OUTPUT FILE CAN NOT BE OPEN !!!!!";
         getch();
         return 1;
         }   
         //*******************input from file--------------------
         int N,D,L;
        
         in>>L>>D>>N;
         cout<<endl<<"welcome"<<endl;
         cout<<L<<D<<N;
         
         char dec[D][L];
         char reg[N][1000];
         char part[L][50];
         char x;
          
         for(int i=0;i<D;i++)
            { 
              for(int j=0;j<L;j++)
                {   in>> x;
                dec[i][j]=x;
                }
            }
           
         
        
      
        

         cout<<endl<<"dictionary==========>"<<endl;
         for(int i=0;i<D;i++)
         {for(int j=0;j<L;j++)
                  cout<< dec[i][j];
                  cout<<endl<<"---------------"<<endl;
         }
         
         
         for(int i=0;i<N;i++)
         {   int count=0; int mulplex=0;
             for(int j=0;j<1000;j++)
             { in>> x;
                if(x=='(')
                {count++; mulplex=1;
                  reg[i][j]=x;
                }
                else if(x==')')
                {reg[i][j]=x;
                  mulplex=0;
                  if(count==L)
                     {
                       reg[i][j+1]='\0';
                        break;
                     }    
                }
                else
                { if(mulplex==1)
                   {reg[i][j]=x;
                   }    
                   else
                   { reg[i][j]=x;
                    count++;
                    if(count==L)
                     {
                       reg[i][j+1]='\0';
                        break;
                     }  
                   }    
                }    
                        
             
             }
           
        }    
             
           
        cout<<endl<<"regular==========>"<<endl;
             
         for(int i=0;i<N;i++)
          { for(int j=0;reg[i][j]!='\0';j++)
                  cout<< reg[i][j];
                  cout<<endl<<"---------------"<<endl;
         }
     //*****************input done****************************
             //***************************logic****************************
     
     for(int i=0;i<N;i++)
      {   
         //@@@@@@@@@@@@@@@@@@@ logic@@@@@@@@@@@@@@@@@@@@@
          
                 //*******break the multiplex************-/
                 {   
          int part_no=0;
          int k=0;
          int multiplex=0;

          for(int j=0;reg[i][j]!='\0';j++)
          {if(reg[i][j]=='(')
            {multiplex=1;
            k=0;
            }
            else if(reg[i][j]==')')
            { multiplex=0;
              part[part_no][k]='*';
              part_no++;
              k=0;
            }
            else
            { if(multiplex==1)
               { part[part_no][k]=reg[i][j];
                k++;
               }  
               else if(  multiplex==0)
               {part[part_no][0]=reg[i][j];part[part_no][1]='*';
                part_no++;
                
               }    
            }            
          } 
                          }    
          //------end of-------brak done-------------  
          cout<<"--------break--------"<<endl<<endl; 
          for(int i=0; i<L ;i++)
          { for (int j=0;part[i][j]!='*';j++)
              { cout<<part[i][j];
              } cout<<endl;
          }           
         
         //----------------matching-------------------------------
         int output=0;
         for( int im=0;im<D;im++) //search for all word...
         {   int all_found=1;
             for(int j=0;j<L;j++)//search for all letter
             { char letter=dec[im][j];//geting jth letter of ith word..match to part[j][] or not
             
                int found=0;
                for(int k=0;part[j][k]!='*';k++)
                { if(part[j][k]==letter)
                  { found=1;break;
                  }     
                } 
                if(found==0)
                 {all_found=0;}
                   
               
             
             } //end   of search for all letter
             if(all_found==1)
               output++;
         }   
         cout<<endl<<"CASE#"<<(i+1)<<":"<<output<<endl;
         out<<"Case #"<<(i+1)<<": "<<output<<endl;
         
         
         
         
         
         
         //--------------end of matching-----------
        
        
        
        
        
        //@@@@@@@@@@@@@@@@@@  end logic @@@@@@@@@@@@@@@@@@@@@@@
       }     
//------------------------end of main problem-----------------------------------*/
         
         
         
in.close();
getch();
  return 0;
}
