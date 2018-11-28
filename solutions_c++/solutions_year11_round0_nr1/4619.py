#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

int main()
 {
  int t1, *time;
  ifstream f;
  ofstream o;
  o.open("new_output");
  f.open("new_trust");
  f>>t1;
  time = new int [t1];
  for(int i=0; i<t1; i++)
   {
     double n, prev_b = 1, prev_o = 1, time_b = 0, time_o = 0, time_tot = 0, t, flag = 1;
     char prev_ch;
     f>>n;
     for(int j=0; j<n; j++)
      {
       char ch;
       int pos;
       f>>ch;
       f>>pos;
       if(j!=0)
        if(prev_ch == ch)
         flag = 0;
        else
         flag = 1;
       if(ch=='B')
         {
          if(flag == 0)
           time_b = 0;
          t = abs(pos - prev_b) ;
          if(t<time_b)
           {
            if(flag == 0)
             time_o += 1;
            else
             time_o = 1;
            time_tot += 1;
           }
          else
           {
            if(flag == 0)
             time_o += t - time_b + 1;
            else
             time_o = t - time_b + 1;
            time_tot += t - time_b + 1;
           }
          prev_b = pos;
         }
       else if(ch=='O')                                                  
         {     
          if(flag == 0)
           time_o = 0;                                                         
          t = abs(pos - prev_o) ;
          if(t<time_o)
           {
            if(flag == 0)
             time_b += 1;
            else
             time_b = 1;
            time_tot +=1;
           }
          else
           {
            if(flag == 0)
             time_b += t - time_o + 1;
            else
             time_b = t - time_o + 1;
            time_tot += t - time_o + 1;
           }
          prev_o = pos;
         } 
       prev_ch = ch; 
      }
     cout<<time_tot<<endl;
     o<<"Case #"<<i+1<<": "<<time_tot<<endl;
   }
  f.close();
  o.close();
  return 0;
 }   
