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
       long long N,Pd,Pg;   
       cin >> N >> Pd >> Pg;
       bool possible = false;
       long long i = 1;
       if (N < 100
            && Pd!=0){
                	   while(i<=N)
                	   {       
                          if( (Pd*i)%100 == 0 ) { possible=true;  break;} i++;
                       }
                     }
       else possible=true;
       if(possible)
       {
         if (Pg==100 && Pd!=100)  possible=false; 
         else  if (Pg==0 && Pd!=0)  possible=false; 
       }
       cout << "Case #" << _case << ": " ;
       if (possible) cout << "Possible" << endl; else  cout << "Broken"<< endl;         
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
