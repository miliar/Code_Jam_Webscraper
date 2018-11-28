#include <fstream>
#include <string>
#include <math.h>
//#include <iostream>

using namespace std;

int main()

{
	
ifstream input("input2.txt");
ofstream output("output2.txt");

int cnt, CNT, maxS, Q, sch;
string B[100], Sx, Qx;

input >> CNT;
for (cnt = 1; cnt <= CNT; cnt++)
{   
	sch = 0;
	
	input>> maxS;
    getline(input, Sx, '\n');

	for (int i = 1; i <= maxS; i++)
		getline(input,Sx, '\n');

	input >> Q;
	getline(input, Qx,'\n');
	
	if (Q != 0) 
	 {
	  getline(input,Qx, '\n');
	  B[0] = Qx;
	  int count = 1;
	  
	  for (int i = 2; i <= Q; i++)
		{   
		    getline(input,Qx, '\n');		
			for( int j = 0; j< count ; j++)
			{
				
			   if (Qx.compare(B[j]) == 0)
			   { j = count;
			   }
			   else if (j == count - 1)
				   { B[j+1] = Qx;
				     count++;
				     j = count;
				   }
			}
			if (count == maxS)
				{sch++;
				 B[0] = B[count-1];
				 count = 1; 
				 }
						   
		  }
	
		}
	 
	 
	
	 output << "Case #" << cnt << ": " << sch;
	 output << '\n';

	}
}
	
