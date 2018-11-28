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
       int n;
       long time_o=0, time_b = 0;
       long time = 0;
       int prev_o =1, prev_b=1;
       cin >> n;
       char ch, lastturn = 'K'; int button;
       while(n-->0)
       {
          cin >> ch >> button;                     
          if(ch=='O')
          {       
             time_o = time_o + 1 + moddiff(button,prev_o);   
             if(lastturn=='B')
             {
              if(time_o>time_b)
              {
                time = time + time_o - time_b;
                time_o = time_o - time_b;
                }
              else          
              {  time++;  time_o = 1; }
              time_b = 0;
            }
            else
            {
                time = time + 1 + moddiff(button,prev_o);                
            }
             prev_o = button;
          }
          else
          {
            time_b = time_b + 1 + moddiff(button,prev_b); 
            
            if(lastturn=='O')
            {
              if(time_b>time_o)
              {
                time = time + time_b - time_o;
                time_b = time_b - time_o;
               }
              else          
              {  time++;  time_b = 1; }
              time_o = 0;
            }
            else
            {
                time = time + 1 + moddiff(button,prev_b);                
            }
            prev_b = button;
          }  
          lastturn = ch;
          //cout << time_o << " ," << time_b << ", " << time << endl;          
       }
    	//------------- o/p --------------
		cout << "Case #" << _case << ": " ;
		cout << time << endl;
		//cout << endl;
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
