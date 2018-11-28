#include <iostream>
#include <fstream>

using namespace std;

int main()
{
   ifstream inputFile;
   inputFile.open("A-small-attempt0.in");


   ofstream outputFile;
   outputFile.open("output.txt");

   int numOfTest = 0;
   inputFile >>numOfTest;
   for (int i =1; i<= numOfTest; i++)
   {
      int todayThreshold = 0;
      int ptoday = 0;
      int ptotal = 0;

      inputFile >> todayThreshold >> ptoday>>ptotal ;
      if(ptotal==0&&ptoday>0)
      {
          outputFile << "Case #" <<i << ": Broken"<<endl;
          continue;
     }
     else if(ptotal==100&&ptoday < 100)
     {
         outputFile << "Case #" <<i << ": Broken"<<endl;
         continue;
     }
     else
     {
         long long temp=ptoday;
         int denominator=100;
         if(temp%2==0)
         {
             temp=temp/2;
             denominator=denominator/2;
             if(temp%2==0)
             {
                 temp=temp/2;
                 denominator=denominator/2;
            }
         }

         if(temp%5==0)
         {
             temp=temp/5;
             denominator=denominator/5;

             if(temp%5==0)
             {
                 temp=temp/5;
                 denominator=denominator/5;
             }

        }

       if((todayThreshold>temp||todayThreshold==temp)&&(todayThreshold>denominator||todayThreshold==denominator))
       {
           outputFile << "Case #" << i <<": Possible" <<endl;
           continue;
       }
       else
       {
           outputFile << "Case #" <<i << ": Broken"<<endl;
           continue;
       }
    }
  }

  outputFile.flush();
  outputFile.close();

   return 0;
}
