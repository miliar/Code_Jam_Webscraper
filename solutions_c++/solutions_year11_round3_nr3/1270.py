#include<iostream>
#include<fstream>
#include<list>
#include<queue>
#include<vector>
#include <cmath>

using namespace std;

int main()
{
    long int cases=0;
    ifstream in;
    ofstream out;
    in.open("C-small-attempt0.in");
    out.open("output.txt");
    in>>cases;
    for(long int inn=1;inn<=cases;inn++)
    {
          int Num=0,Low=0,High=0;
          in>>Num;
          in>>Low;
          in>>High;
          int  my_array[Num];
          for(int j=0;j<Num;j++)
          {
                  in>>my_array[j];
          }    
          bool check=false;
          long int answer=0;
     
          while(Low<=High)
          {
                for(int mm=0;mm<Num;mm++)
                {
                        if(my_array[mm]>Low)
                        {
                             if(my_array[mm]%Low==0)
                             {
                                  check=true;                
                             }
                             else
                             {
                                 check=false;
                                 break;    
                             }
                        }
                        else
                        {
                            if(Low%my_array[mm]==0)
                            {
                                 check=true;                
                            }
                            else
                        {
                        check=false;
                        break;    
                }   
          }       
     }
            if(check==true){answer=Low;Low=High;}
             Low++;         
     }
           
     if(check==true)
     {
         out<<"Case #"<<inn<<": "<<answer<<endl;              
     }
     else
     {
         out<<"Case #"<<inn<<": NO"<<endl;   
     }
}
in.close();
out.close();
return 0;   
}
