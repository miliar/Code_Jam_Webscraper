#include <iostream>
#include <math>
#include <conio>
#include <fstream>
//using namespace std;

main()
{
	int n, t;
   unsigned long int k;
   cin>>t;
   int i, j;
   ofstream f("result.txt");
   for(i = 0; i<t; i++)
   {
   	cin>>n>>k;
      j = pow(2,n);
      cout<<"Case #"<<(i+1)<<" ";
      f<<"Case #"<<(i+1)<<": ";
      if((k+1)%j==0)
      {
      	cout<<"ON\n";
         f<<"ON\n";
      }
      else
      {
      	cout<<"OFF\n";
         f<<"OFF\n";
      }
   }
   f.close();
   getch();
}
