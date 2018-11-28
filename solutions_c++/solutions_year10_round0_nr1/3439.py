#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{   
   ifstream fin;
   ofstream fout;
   fin.open("A-large.in");
   fout.open("output.txt");
   int t=0,n=0,k=0;
   int i;
   long a[31];
   a[0]=1;
   for (i=1;i<=30;i++)
   {
      a[i]=a[i-1]*2;
   }
   fin >> t;
   for (i=1; i <= t ; i++)
   {
      fin >> n >> k;
      if (k % a[n]==a[n]-1)
         fout << "Case #" << i << ": ON" << endl;
      else 
         fout << "Case #" << i << ": OFF" << endl;
   }

   fin.close();
   fout.close();
   return 0;
}