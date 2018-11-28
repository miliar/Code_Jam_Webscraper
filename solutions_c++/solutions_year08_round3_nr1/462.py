
#include <fstream>
#include <string>
#include <math.h>
//#include <iostream>

using namespace std;

int compare (const void * a, const void * b)
{
 if (*(long *) a < *(long *)b )
  return (1);
  else return (-1);
}


int main()

{
	
ifstream input("input.txt");
ofstream output("output.txt");

int cnt, CNT, aux;
int P,K,L;
int A[1000];

input >> CNT;

//getline(input, aux1, '\n');
//aux1 = "";


for (cnt = 1; cnt <= CNT; cnt++)
{  
	
    input >> P >> K >> L; 
   
    
	for (int i = 0 ; i < L ; i++)
		{input >> A[i]; 
		 }
	
	qsort (A, L, sizeof(long), compare);
 
	long long out = 0;
	int k = 1;
	
	if (L <= P * K)
	{	
	
	int j = 0, i = 0;	
	while (j<L)
	{   i = 0;
		while (i < K & j + i < L )
		{out += A[j + i] * k ;
		i++;
		}
		j = j + K;
		
		k++;
		
	}
	output << "Case #" << cnt << ": " << out;
		
	
	}else
	
		output << "Case #" << cnt << ": " << "Impossible";
	
	
	output << '\n';

}
}
	
