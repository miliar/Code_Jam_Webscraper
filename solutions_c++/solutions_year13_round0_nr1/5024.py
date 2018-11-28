#include<iostream>
#include<fstream>
#include<conio.h>
#include<string.h>
#include<iomanip>
using namespace std;
int checkrandc(char T[4][4],int m,int n,char c)
{
 if((T[m][(n+1)%4]==c&&T[m][(n+2)%4]==c&&T[m][(n+3)%4]==c)||(T[(m+1)%4][n]==c&&T[(m+2)%4][n]==c&&T[(m+3)%4][n]==c))
 { 
  return 1;
 }   
 return 0;
}
int check1diag(char T[4][4],int n,char c)
{
    if(T[(n+1)%4][(n+1)%4]==c&&T[(n+2)%4][(n+2)%4]==c&&T[(n+3)%4][(n+3)%4]==c)
    return 1;
    
    return 0;
}
int check2diag(char T[4][4],int m,char c)
{
    if(T[(m+1)%4][3-(m+1)%4]==c&&T[(m+2)%4][3-(m+2)%4]==c&&T[(m+3)%4][3-(m+3)%4]==c)
    {
        return 1;                                                                      
                                                                              }
      return 0;                                                                        
}
char* analyzewin(char T[4][4],int i)
{ int m,n,p,q,flag;
m = -1; n = -1;
    //Find position of T
    for(p = 0;p <4;p++)
    { for(q = 0; q<4;q++)
       {
       if(T[p][q]=='T')
       {m = p; 
       n = q; 
       break; }
       if(n != -1 ) break;
       }
          }
          
//to check who won
//if T exists 
if(m!=-1)
{
        
   if(checkrandc(T,m,n,'X')==1)
  {
                    return "X won";                                          
                                                                 }
 else if(checkrandc(T,m,n,'O')==1)
 {
      return "O won";
  }                                                          
 else if(m==n)
 {
  if(check1diag(T,m,'X')==1)
   return "X won";
    if(check1diag(T,m,'O')==1)
    return "O won";   
  }   
  else if(m+n ==3)
  {if(check2diag(T,m,'X')==1)
   return "X won";
    if(check2diag(T,m,'O')==1)
    return "O won"; 
   }                                                                   
         }
//if neither won with T
//check with all rows and columns
for(p=0;p<4;p++)
{ if(checkrandc(T,p,p,T[p][p])==1)
   {if(T[p][p]=='X') return "X won";
     else if(T[p][p]=='O') return "O won";}   
                }      
//check if won with 4 on diags
if(check1diag(T,0,T[0][0])==1)
{
            if(T[0][0]=='X')
            return "X won";
            else if(T[0][0]=='O') return "O won";
                 }                                         
 if(check2diag(T,0,T[0][3])==1  )
 {           if(T[0][3]=='X')
            return "X won";
            else if(T[0][3]=='O') return "O won";
                                }  
//check if incomplete
for(p = 0; p<4; p++)
for(q = 0 ; q<4; q++)
{
      if(T[p][q]=='.')
      return "Game has not completed";
      
      }                                
return "Draw";                                                                                                     
}
int main()
{
    char x,T[4][4];
    int n;
    char* w;
    
    ifstream fin;
    ofstream fout;
    fin.open("As.in",ios::in);
    fout.open("Aso.out",ios::out);
    fin>>n;
    for(int i = 0; i<n ; i++)
    {
            for(int j = 0; j<4;j++)
            {
                for(int k =0; k<4;k++)
                { fin>>x ;
                   T[j][k] = x;
                   
                        }
                       
            }
             w = analyzewin(T,i);
             fout<<"Case #"<<i+1<<": "<<w<<endl;
            
            }

    fin.close();
    fout.close();
    }
