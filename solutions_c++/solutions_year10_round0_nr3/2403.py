#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int income(long r,long k, int n,long g[])

{
  long round = 0;
  int iterator = 0;
  long total = 0;
  int group = 0;
  long capacity = 0;
 
  
  while(round < r)
  {  
	 if(capacity + g[iterator] <= k && group <n)
	 {
		 capacity += g[iterator];
		 total += g[iterator];
		 iterator = (iterator + 1)%n;
		 group++;
	 }
	 else
	 { 
		 round++;
		 group = 0;
		 capacity = 0;
	 }
	}
  return total;

}
int main()
{
	long Euros = 0;
    int n,testcase = 0;
	long r, k;
	long g[1000];
	ifstream in("C-small-attempt0.in");
	ofstream out("out.txt");
	in >> testcase;
	for(int i  = 1; i <= testcase; i++)
	{
		in >> r;
		in >> k;
		in >> n;
		for(int j = 0 ; j < n ; j++)
		{
			in >> g[j];
		}
       Euros = income(r,k,n,g);
	   out << "Case #" << i << ": " << Euros << endl;
 	}
	return 0 ;
	
    
	

}
