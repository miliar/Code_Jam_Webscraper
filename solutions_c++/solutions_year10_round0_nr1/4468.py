#include <iostream>
#include <conio.h>
#include <fstream>

using namespace std;

void toggleBit(bool &b)
{
     if(b == true)
     b = false;
     else 
     b = true;
}
void processSet(int N, uint64_t K, int caseId)
{
 bool* bitArray = new bool[N];
 for(int i=0;i<N;i++)
 {
         bitArray[i] = false;
 }    

 for(uint64_t iter=0;iter <K; iter++)
 {
         // process one single iteration here
          bool status = true;
         for(int i=0;i<N;i++)
         {
                 bool prevStatus = status;
                 status = bitArray[i] && prevStatus;
                 if(prevStatus)
                 toggleBit(bitArray[i]);
         }
       /*  for(int i=0;i<N;i++)
         cout<< bitArray[i]<<"  ";
         cout << endl;*/
         
 }
 // Now that we have final array, need to check if it is a true case or false
 bool status = true;
 for(int i=0;i<N;i++)
 status = status && bitArray[i];
 delete []bitArray;
 if(status)
 cout<< "Case #"<<caseId<<": "<<"ON"<<endl;
 else
 cout<< "Case #"<<caseId<<": "<<"OFF"<<endl;
}


/*{
  cout<< "Case #"<<caseId<<": "<<'0'<<endl;
  else
  cout<< "Case #"<<caseId<<": "<<findInteger(buffer,len,maxDistinct)<<endl;
}*/
int main(int argc, char** argv)
{
/* Code to parse input file */
   if(argc!=2)
   {
              cout <<"\n Please enter input file name ";
              getch();
              return 0;
   }
   fstream infile(argv[1]);
   int num;
   infile>>num;
   for(int i=0;i<num;i++)
   {
           int N;
           uint64_t K;
           infile>>N;
           infile>>K;
           processSet(N,K, i+1);
   }
   return 0;
}
