#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{   
   ifstream fin;
   ofstream fout;
   fin.open("C-small-attempt0.in");
   fout.open("output.txt");
   int t=0,r=0,k=0,n=0;
   int result, total, runtime;
   int cap;
   int g[1000]={0};
   int i,j,count;
   fin >> t;
   for (i=0; i<t; i++)
   {
      total = 0;
      result = 0;
      runtime = 0;
      // input for each cases
      fin >> r >> k >> n;
      for (j=0; j<n; j++)
      {
         fin >> g[j];
         total+= g[j];
      }
      if (total <= k)
         result = total * r;
      else
      {
         cap = 0;count=0;
         while (runtime < r)
         {
            if (cap+g[count % n]>k)
            {
               result+=cap;
               cap = 0;
               runtime++;
            }
            else
            {
               cap+= g[count % n];
               count++;
            }
         }
      }
      fout << "Case #" <<i+1 << ": " << result <<endl;

   }

   fin.close();
   fout.close();
   return 0;
}