#include <iostream>  /* Provide support for stand input and output such as cout*/
#include <fstream>  /* Provide support for file input and output*/
#include <algorithm>
#include <set>
#include <stack>
#include <iterator>
#include <stdlib.h>

using namespace std; /* Use stand name space*/

long solve(char* N)
{	
	 int mapping_table[255];
	int next = 0;
	int i = 0;
	long result;
	int base = 2;

	 for(int i=0; i<255; i++)
	 {
		mapping_table[i] = -1;
	 }
	
	 mapping_table[N[0]] = 1;

//	cout << "First letter is " << N[0] << " Mapping to " << mapping_table[N[0]] << endl; 
	 
	 while(i<strlen(N) && N[i]==N[0])
	 {
			i++;
	 }

	 if(i<strlen(N))
	 {
			mapping_table[N[i]] = 0;
//			cout << "Second letter is " << N[i] << " Mapping to " << mapping_table[N[i]] << endl; 
	 }



	 next = 2;

	 for(int j=i+1; j<strlen(N); j++)
	 {
		 if(mapping_table[N[j]]==-1)
		 {
			mapping_table[N[j]] = next;
			next++;
			base++;
		 }
//		 cout << "current letter is " << N[j] << " Mapping to " << mapping_table[N[j]] << endl; 
	 }

	 result = 0;

	 for(int i=0; N[i]!='\0'; i++)
	 {
			result = result*(long)base + (long)mapping_table[N[i]];
	 }

	 return result;
}


int main(int argc, char** args)
{
		long result;
		int T; /* Number of test cases */
		char* N;
		char c;

		N = (char*)malloc(255*sizeof(char));

	 /* Initialize input and output file */ 
		fstream input_file("A-small-attempt1.in.txt"/*"Debug\\input.in"*/, ios_base::in);
		fstream output_file("output.txt"/*"Debug\\output.txt"*/, ios_base::out);
		if(!input_file.is_open() || !output_file.is_open())
		{
				cout << "Unalbe to open file!" << endl;
				return 1;
		}

	/* Read the number of test cases*/
		input_file >> T;
		input_file.get();
	   cout << "The number of test cases is " << T << endl;

	/* For each test case, load variables*/
		for(int i=0; i<T; i++)
		{
			input_file.getline(N, 255);

			result = solve(N);
		
			cout << "The string N is " << N << endl;
			
			cout << "Case #" << i +1<< ":	" << result << endl << endl << endl << endl;
			output_file << "Case #" << i+1 << ":	" << result << endl;
		}

		input_file.close();
		output_file.close();

		return 0;
}