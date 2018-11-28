#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <cstdlib>
#include <algorithm>


using namespace std;

string rotate (string s)
{
  for (int i = 1; i < s.size(); i++) 
  swap(s[i-1], s[i]); 
  return s;     
}
       

int main()
{
      unsigned int T, TestCase, LB , UB;
      char chararrayLB[10],chararrayUB[10],temparraynum[10];
      string strLB, strUB, strcurnum,strrp,strtempnum,rotationarray[10];
      int i,j,k,racount, RPCounter, LBlength, UBlength;
      
      ifstream inFile;
      ofstream outFile;
           
      size_t length;
      RPCounter = 0;
 
      inFile.open("C:\\Users\\Indira Krishnamurthi\\Desktop\\Smallinput.txt");
      outFile.open("C:\\Users\\Indira Krishnamurthi\\Desktop\\Smalloutput.txt");
      
      inFile >> T;
     
     
      for (TestCase=1; TestCase <= T; TestCase++)
      {
          inFile >> LB;
          inFile >> UB; 
    
          itoa(LB,chararrayLB,10);
          itoa(UB,chararrayUB,10);
          strLB = chararrayLB;
          strUB = chararrayUB;
          LBlength = strLB.length();
          UBlength = strUB.length();    
          RPCounter = 0;
          for (i = LB; i < UB; i++)
          {
              strcurnum =itoa(i,temparraynum,10);
              strtempnum =strcurnum;
              racount =0;
              rotationarray[racount] = strcurnum;
              for ( j = 1; j < strcurnum.length();j++)
              {
                  strrp=rotate(strtempnum);
                  racount++ ;
                  rotationarray[racount] = strrp;
                  if ((strrp[0] =='0') || (strrp <= strcurnum) || (strrp > strUB) || (strrp < strLB))
                  {
                    strtempnum =strrp;
                  }
               
                  else 
                  {
                   RPCounter ++;
                        
                   strtempnum = strrp;
                   for (k = 0;k < racount; k++)
                   {
                    if (strrp == rotationarray[k]) 
                    { RPCounter--;
                 
                    }
                    
                   }
                  }
               
              }
          }  
              outFile  << "Case #" << TestCase << ": " << RPCounter << "\n";
       }
          
      inFile.close();
      outFile.close();
      return 0;

}
