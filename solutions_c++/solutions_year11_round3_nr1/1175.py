#include <string>
#include <iostream>
#include <list>
#include <algorithm>
#include <math.h>

using namespace std;


int moddiff(int , int );
int main() 
{
    //--------------------------------
    int  t;
    cin >> t;
    int  _case = 1;
	for(;_case<=t;_case++)
	{     
      string str[51]; int r,c;
      bool strcheck[51][51];
      memset(strcheck, false, sizeof(strcheck));
      cin >>  r>>c;
      int i=0;
      while(i<r){ cin >> str[i]; i++;}
      bool possible = true; 
      for(i=0;i<r;i++)
      {           
          for(int j=0; j<c; j++)
          {   
              if (strcheck[i][j]) continue;  
              if(str[i][j]=='#')
              {
                           
                   //if( i==r-1 || j==c)   { possible=false;break;}             
                   if(j+1 <= c && str[i][j+1]=='#') possible=true; else { possible=false;break;}             
                   if(i+1 <= r && str[i+1][j]=='#' && str[i+1][j+1]=='#') possible=true; else {possible=false; break;}   
                    str[i][j]='/'; 
                    str[i][j+1]='\\';
                    str[i+1][j]='\\'; str[i+1][j+1]='/'  ;
                    strcheck[i][j] = true;   strcheck[i][j+1] = true;strcheck[i+1][j] = true;strcheck[i+1][j+1] = true;   
              }    
                   
          }            
            if (!possible )    break;
      }
      
      //--------------------------------
      cout << "Case #" << _case << ": " ;    
      if (!possible )  cout << endl << "Impossible"  ;
      else  
      { i=0;
         while(i<r) {cout << endl << str[i] ; i++; }
            }   cout << endl;   
    }
	return 0;
}

int moddiff(int a, int b)
{
       if (a > b)
          return a - b;
        else
          return b - a;     
}
