#include <fstream>
#include <string>
#include <math.h>
//#include <iostream>

using namespace std;

int main()

{
	
ifstream input("input4.txt");
ofstream output("output4.txt");

int cnt, CNT, A, B, ta, At, Bt;
int As[100][2], Bs[100][2];
string aux1, aux2;

input >> CNT;

for (cnt = 1; cnt <= CNT; cnt++)
{  
	input >> ta;
	input >> A >> B;
	for (int i = 0; i < A; i++)
	{ input>> aux1 >> aux2; 
	  As[i][0]= atoi(aux1.substr(0,2).c_str())* 60 + atoi(aux1.substr(3,2).c_str()) ;
	  As[i][1]= atoi(aux2.substr(0,2).c_str())* 60 + atoi(aux2.substr(3,2).c_str()) + ta;
	}

	for (int i = 0; i < B; i++)
	{
	 input>> aux1 >> aux2; 
	 Bs[i][0]= atoi(aux1.substr(0,2).c_str())* 60 + atoi(aux1.substr(3,2).c_str()) ;
	 Bs[i][1]= atoi(aux2.substr(0,2).c_str())* 60 + atoi(aux2.substr(3,2).c_str()) + ta;
	}

	int prev = -1, posprev = -1;
	
	for (int i = 0; i < A; i++)
	{   prev = -1; posprev = -1;
		for (int j = 0; j < B; j++)
		{
			if( Bs[j][1] <= As[i][0] && Bs[j][1] > prev)
			{prev = Bs[j][1];			            
			 posprev = j;
			}
			
		}
		if (posprev != -1) 
		{ As[i][0] = -1;
		  Bs[posprev][1] = -1;
		}
	} 
	
	
	for (int i = 0; i < B; i++)
		{   prev = -1; posprev = -1;
			for (int j = 0; j < A; j++)
			{
				if( As[j][1] <= Bs[i][0] && As[j][1] > prev)
				{prev = As[j][1];			            
				 posprev = j;
				}
				
			}
			if (posprev != -1) 
			{ Bs[i][0] = -1;
			  As[posprev][1] = -1;
			}
		}
	
	
	At = 0; Bt = 0;
	for (int i = 0; i < A; i++)
		if (As[i][0] != -1)
		  At++;
		
	for (int i = 0; i < B; i++)
		if (Bs[i][0] != -1)
				  Bt++;
						
		
	 output << "Case #" << cnt << ": " << At << " " << Bt;
	 output << '\n';

}
}
	
