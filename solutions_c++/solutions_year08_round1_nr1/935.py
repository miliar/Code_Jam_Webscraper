#include <fstream>
#include <string>
#include <math.h>
//#include <iostream>

using namespace std;

int compare (const void * a, const void * b)
{
 if (*(int*) a < *(int*)b )
  return (1);
  else return (-1);
}


int main()

{
	
ifstream input("input.txt");
ofstream output("output.txt");

int cnt, CNT, aux;

//string A[64], aux1,aux2;
int A[800] , B [800], max;

input >> CNT;

//getline(input, aux1, '\n');
//aux1 = "";


for (cnt = 1; cnt <= CNT; cnt++)
{  
	
    input >> aux; 
    max = 0;
	for (int i = 0 ; i < aux ; i++)
		{input >> A[i]; 
		 max++;
		}
	
	for (int i = 0 ; i < aux ; i++)
	{	input >> B[i]; 
	}	
	qsort (A, max, sizeof(int), compare);
	qsort (B, max, sizeof(int), compare);
 
	int out = 0;
	
	for (int j =0; j< max ; j++)
	{
		out = A[j] * B [max - 1 - j] + out;
		
	}
		 
	output << "Case #" << cnt << ": " << out;
	output << '\n';

}
}
	


