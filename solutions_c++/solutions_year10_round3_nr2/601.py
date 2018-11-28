#include <iostream>  /* Provide support for stand input and output such as cout*/
#include <fstream>  /* Provide support for file input and output*/
#include <algorithm>
#include <set>
#include <stack>
#include <iterator>
#include <stdlib.h>
#include <cmath>

using namespace std; /* Use stand name space*/

int solve(int L, int P, int C)
{			
	   float temp1, temp2, temp4;
	   int temp3, temp5; 

	   temp1 = (float)P/(float)L;
	   temp2 = log(temp1)/log((float)C);
	   temp3 = ceil(temp2);
	   temp4 = log((float)temp3)/log((float)2);
	   temp5 = ceil(temp4);
		
		return temp5;
}



int main(int argc, char** args)
{
		int result;
		int T; /* Number of test cases */
		int L;
		int P; 
		int C; 

	 /* Initialize input and output file */ 
		fstream input_file("B-small-attempt1.in", ios_base::in);
		fstream output_file("output.txt", ios_base::out);
		if(!input_file.is_open() || !output_file.is_open())
		{
				cout << "Unalbe to open file!" << endl;
				return 1;
		}
 
	/* Read the number of test cases*/
		input_file >> T;
//		cout << "The number of test cases is " << C << endl << endl;

   /* For each test case, load variables*/
		for(int i=0; i<T; i++)
		{
//        cout << "Test case: " << i+1 << endl;

			input_file >> L;
			input_file >> P;
			input_file >> C;

   cout << "Number L, P, C is: " << L << ", "<< P<< ", "<< C << endl;

		result = solve(L, P, C);

			cout << "Case #" << i +1<< ":	" << result << endl;


output_file << "Case #" << i+1 << ":	" << result << endl;
		}

}