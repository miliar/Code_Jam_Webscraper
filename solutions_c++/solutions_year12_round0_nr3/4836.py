#include <iostream>
#include <string>
#include <fstream>
#include <stdio.h>
#include <math.h>
#include <cstdlib>
using namespace std;
int main()
{
string line;
string numstr,numstr2;
int small,big;
ifstream fileInput("C-small-attempt4.in");
ofstream fileOutput("out.in",ios::app);
if(fileInput.is_open())
{
 int z=1;
   while(getline(fileInput,line))
   {
  
    int num = line.find(" ");
    if(num>0)
    {
            int pair = 0;
       int digit = 0;
      numstr = line.substr(0,num);
      small = atof(numstr.c_str());
      numstr2 = line.substr(num,line.length()-1);
      big = atof(numstr2.c_str());
      int testdigit = big;
      while(testdigit>0)
        {
        ++digit;
        testdigit = testdigit/10;
        }
      int s=0;
      for(s=small;s<=big;s++)
      {
              int g = digit; 
        int a[digit];
        int equals = s;
        
         while(equals>0)
        {
        a[--g] = equals%10;
        equals/=10;
        }

        for(int judge=1;judge<digit;judge++)
         {
            int total = 0;
            for(int b=digit;b>0;b--)
           {
             int power = judge-b;
             if(power<0)
             {
              power = power+digit;
             }
             total+= a[b-1]*pow(10,power);
             
           }
          
         if(total>=small&&total<=big&&total!=s)
          {
           pair++;
          }
        }
      }
    
 if(fileOutput.is_open())
{
 fileOutput << "Case #" << z++ << ": " << pair/2 <<"\n" ;
}

}

}
}
return 1;
}
