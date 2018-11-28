#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <string>
#include <vector>
using namespace std;

#include "matrix.h"

#define AND 1
#define OR 0
#define CANT 0
#define CAN  1


int* values_A;
		int* gates_A;
		int* changeable_A;
		int M;
		int V;


int min_number_of_gates( int index, int desired_value )
{
		
		

		if(index >= (M-1)/2)
		{
			if(desired_value != values_A[index]) { return -1;}
			else { return 0;}

		}
		else
		{
			int min1, min2, min3, min4, min5, min6;
		  if(desired_value == 1) 
		  {
				if((gates_A[index] == AND)	&& (changeable_A[index] == CANT))
				{
						min1 = min_number_of_gates(2*index+1,1);
						min2 = min_number_of_gates(2*index+2,1);
						if((min1 == -1) || (min2 == -1)) { return -1;}
						else { return min1+min2; }
				}
			 if((gates_A[index] == OR)	&& (changeable_A[index] == CANT))
				{
						int hello = -1;



						min1 = min_number_of_gates(2*index+1,0);
						min2 = min_number_of_gates(2*index+2,1);
						min3 = min_number_of_gates(2*index+1,1);
						min4 = min_number_of_gates(2*index+2,0);

						if(!((min1 == -1) || (min2 == -1)) )
						{
							hello = min1+min2;
						}
						if(!((min2 == -1) || (min3 == -1)) )
						{
							
							if(hello > min2+min3 ||  hello == -1) { hello = min2+min3;}
						}
						if(!((min3 == -1) || (min4 == -1)) )
						{

							if(hello > min3+min4 || hello == -1) { hello = min3+min4;}
						}

						return hello;	
				}
				if((gates_A[index] == AND)	&& (changeable_A[index] == CAN))
				{
						int hello1, hello2;
						hello1 = -1;
						hello2 = -1;
						
						{
						min1 = min_number_of_gates(2*index+1,1);
						min2 = min_number_of_gates(2*index+2,1);
						if(!((min1 == -1) || (min2 == -1))) 
						{ hello1 = min1+min2; }

						}

						{
						min1 = min_number_of_gates(2*index+1,0);
						min2 = min_number_of_gates(2*index+2,1);
						min3 = min_number_of_gates(2*index+1,1);
						min4 = min_number_of_gates(2*index+2,0);

						if(!((min1 == -1) || (min2 == -1)) )
						{
							hello2 = min1+min2;
						}
						if(!((min2 == -1) || (min3 == -1)) )
						{
							if(hello2 > min2+min3 || hello2 == -1) { hello2 = min2+min3;}
						}
						if(!((min3 == -1) || (min4 == -1)) )
						{

							if(hello2 > min3+min4 || hello2 == -1) { hello2 = min3+min4;}
						}

							if(hello2 != -1) {hello2++;}
						}
						
						if( hello1 == -1 && hello2 == -1) { return -1;}
						else if( hello1 == -1) { return hello2;}
						else if(hello2 == -1) { return hello1;}
						else { 
							if(hello1 < hello2) { return hello1;}
							else { return hello2;}
						}
				}
				if((gates_A[index] == OR)	&& (changeable_A[index] == CAN))
				{
						int hello1, hello2;
						hello1 = -1;
						hello2 = -1;
						
						{
						min1 = min_number_of_gates(2*index+1,1);
						min2 = min_number_of_gates(2*index+2,1);
						if(!((min1 == -1) || (min2 == -1))) 
						{ hello1 = min1+min2+1; }

						}

						{
						min1 = min_number_of_gates(2*index+1,0);
						min2 = min_number_of_gates(2*index+2,1);
						min3 = min_number_of_gates(2*index+1,1);
						min4 = min_number_of_gates(2*index+2,0);

						if(!((min1 == -1) || (min2 == -1)) )
						{
							hello2 = min1+min2;
						}
						if(!((min2 == -1) || (min3 == -1)) )
						{
							if(hello2 > min2+min3 || hello2 == -1) { hello2 = min2+min3;}
						}
						if(!((min3 == -1) || (min4 == -1)) )
						{

							if(hello2 > min3+min4 || hello2 == -1) { hello2 = min3+min4;}
						}

						}
						
						if( hello1 == -1 && hello2 == -1) { return -1;}
						else if( hello1 == -1) { return hello2;}
						else if(hello2 == -1) { return hello1;}
						else { 
							if(hello1 < hello2) { return hello1;}
							else { return hello2;}
						}
				}




		  }
		  else
		  {
				if((gates_A[index] == OR)	&& (changeable_A[index] == CANT))
				{
						min1 = min_number_of_gates(2*index+1,0);
						min2 = min_number_of_gates(2*index+2,0);
						if((min1 == -1) || (min2 == -1)) { return -1;}
						else { return min1+min2; }
				}
			 if((gates_A[index] == AND)	&& (changeable_A[index] == CANT))
				{
						int hello = -1;

						min1 = min_number_of_gates(2*index+1,1);
						min2 = min_number_of_gates(2*index+2,0);
						min3 = min_number_of_gates(2*index+1,0);
						min4 = min_number_of_gates(2*index+2,1);

						if(!((min1 == -1) || (min2 == -1)) )
						{
							hello = min1+min2;
						}
						if(!((min2 == -1) || (min3 == -1)) )
						{
							if(hello > min2+min3 || hello == -1) { hello = min2+min3;}
						}
						if(!((min3 == -1) || (min4 == -1)) )
						{

							if(hello > min3+min4 || hello == -1) { hello = min3+min4;}
						}

						return hello;	
				}
				if((gates_A[index] == OR)	&& (changeable_A[index] == CAN))
				{
						int hello1, hello2;
						hello1 = -1;
						hello2 = -1;
						
						{
						min1 = min_number_of_gates(2*index+1,0);
						min2 = min_number_of_gates(2*index+2,0);
						if(!((min1 == -1) || (min2 == -1))) 
						{ hello1 = min1+min2; }

						}

						{
						min1 = min_number_of_gates(2*index+1,1);
						min2 = min_number_of_gates(2*index+2,0);
						min3 = min_number_of_gates(2*index+1,0);
						min4 = min_number_of_gates(2*index+2,1);

						if(!((min1 == -1) || (min2 == -1)) )
						{
							hello2 = min1+min2;
						}
						if(!((min2 == -1) || (min3 == -1)) )
						{
							if(hello2 > min2+min3 || hello2 == -1) { hello2 = min2+min3;}
						}
						if(!((min3 == -1) || (min4 == -1)) )
						{

							if(hello2 > min3+min4 || hello2 == -1) { hello2 = min3+min4;}
						}

						if(hello2 != -1) {	hello2++;}
						}
						
						if( hello1 == -1 && hello2 == -1) { return -1;}
						else if( hello1 == -1) { return hello2;}
						else if(hello2 == -1) { return hello1;}
						else { 
							if(hello1 < hello2) { return hello1;}
							else { return hello2;}
						}

				}
				if((gates_A[index] == AND)	&& (changeable_A[index] == CAN))
				{
						int hello1, hello2;
						hello1 = -1;
						hello2 = -1;
						
						{
						min1 = min_number_of_gates(2*index+1,0);
						min2 = min_number_of_gates(2*index+2,0);
						if(!((min1 == -1) || (min2 == -1))) 
						{ hello1 = min1+min2+1; }

						}

						{
						min1 = min_number_of_gates(2*index+1,1);
						min2 = min_number_of_gates(2*index+2,0);
						min3 = min_number_of_gates(2*index+1,0);
						min4 = min_number_of_gates(2*index+2,1);

						if(!((min1 == -1) || (min2 == -1)) )
						{
							hello2 = min1+min2;
						}
						if(!((min2 == -1) || (min3 == -1)) )
						{
							if(hello2 > min2+min3 || hello2 == -1) { hello2 = min2+min3;}
						}
						if(!((min3 == -1) || (min4 == -1)) )
						{

							if(hello2 > min3+min4 || hello2 == -1) { hello2 = min3+min4;}
						}

						}
						
						if( hello1 == -1 && hello2 == -1) { return -1;}
						else if( hello1 == -1) { return hello2;}
						else if(hello2 == -1) { return hello1;}
						else { 
							if(hello1 < hello2) { return hello1;}
							else { return hello2;}
						}

				}





		  }



		}

}


int main()
{
	int num_cases;
	int i;

	cin >> num_cases;
	

	for(i=0;i< num_cases;i++)
	{
		
			cin >> M;
		cin >> V;

		int k;

		values_A = new int[M];
		gates_A = new int[M];
		changeable_A = new int[M];

		for(k=0; k < (M-1)/2; k++)
		{
			cin >> gates_A[k];
			cin >> changeable_A[k];
		}

		for(k = (M-1)/2 ; k < M; k++)
		{
			cin >> values_A[k];
		}


		int value = min_number_of_gates(0,V);			
		
		if(value != -1)
		{
 	  cout << "Case #"<<i+1<<": "<< value<< endl;
		}
		else 
		{

 	  	cout << "Case #"<<i+1<<": IMPOSSIBLE"<< endl;
		}

	  delete values_A;
	  delete gates_A;
	  delete changeable_A;

	}
}
