#include<cstdlib>
#include <iostream>
using namespace std;

int check(char arr[][5], char ch)
{
    int val=0;
           for(int j=0; j< 4; j++)
           {
              bool fl=true;
              int c=0;     
              for(int i=0; i< 4; i++)
              {
                   if(arr[j][i]!=ch&&arr[j][i]!='T')
                   {
                                          
                       fl=false;
                       //break;
                   }
                   if(arr[j][i]==ch)
                            c++;        
                   
               }
               if(fl&&c>=3)
                  return 1;
           }
           for(int i=0; i< 4; i++)
           {
              bool fl=true;
              int c=0;          
              for(int j=0; j< 4; j++)
              {
                   if(arr[j][i]!=ch&&arr[j][i]!='T')
                   {                           
                       fl=false;
                       //break;
                   }
                   if(arr[j][i]==ch)
                            c++;        
                   
               }
               if(fl&&c>=3)
                  return 1;
           }
           //for(int i=0; i< 4; i++)
           {
              bool fl=true;
              int c=0;          
              //for(int j=0; j< 4; j++)
              for(int i=0; i< 4; i++)
              {
                   if(arr[i][i]!=ch&&arr[i][i]!='T')
                   {                           
                       fl=false;
                       //break;
                   }
                   if(arr[i][i]==ch)
                            c++;        
                   
               }
               if(fl&&c>=3)
                  return 1;
           }
           //for(int i=0; i< 4; i++)
           {
              bool fl=true;
              int c=0;          
              //for(int j=0; j< 4; j++)
              for(int i=0; i< 4; i++)
              {
                   if(arr[i][3-i]!=ch&&arr[i][3-i]!='T')
                   {                           
                       fl=false;
                       //break;
                   }
                   if(arr[i][3-i]==ch)
                            c++;        
                   
               }
               if(fl&&c>=3)
                  return 1;
           }
           return 0;
}
int main()
{
    int T;
    cin>>T;
    char chh[2]={0};
    cin.getline(chh, 2);
    for(int k=0; k< T; k++)
    {
         char arr[4][5];
         bool f=true;   
         //for(int i=0; i< 4; i++)
           for(int j=0; j< 4; j++)
           {
                   cin.getline(arr[j], 5);
           }
           bool ac=false;
           char sol[40]={0};
           sprintf(sol,"Case #%d: ", k+1);
           if(1==check(arr, 'X'))
           {
                 ac=true;           
                 strcat(sol,"X won");           
           }
           else if(1==check(arr, 'O'))
           {
                ac=true;
               strcat(sol,"O won");           
           }
           else 
           {
                
                for(int i=0; i< 4; i++)
                    for(int j=0; j< 4; j++)
                       if(arr[i][j]=='.')
                       {
                          f=false;       
                          i=4;       
                          strcat(sol,"Game has not completed");                
                          break;
                       }
               //if(!f)        
                     
           }
           if(f && !ac)
              strcat(sol, "Draw");
          cout<<sol<<endl;
         cin.getline(arr[0], 5);     
    }
    return 0;
}
