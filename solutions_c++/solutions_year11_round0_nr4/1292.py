#include <iostream>
#include <fstream>
#include <string>
using namespace std;

//#include "Case.h"

int* sort(int* array, int N)
{
	int sorted[1000];
	for (int i = 0; i<N; i++)
	{
		sorted[i] = array[i];
	}

	int iMin;
	int temp;

	for (int iPos = 0; iPos < N; iPos++)
	{
	  iMin = iPos;
	  for (int i = iPos+1; i < N; i++)
	    {
	      if (sorted[i] < sorted[iMin])
	        {
	          iMin = i;
	        }
	    }
	  if ( iMin != iPos )
	  {
	    temp = sorted[iPos];
	    sorted[iPos] = sorted[iMin];
	    sorted[iMin] = temp;
	  }
	}

	return sorted;
}


int main()
{
	//Open files
	ifstream in;
	ofstream out;

	in.open("in.txt", ios::in);

	if (!in) {
	  cout << "Can't open input file." << endl;
	}

	out.open("out.txt", ios::out);

	if (!out) {
	  cout << "Can't open output file " << endl;
	  return 1;
	}
	//Get number of cases
	int T = 0;
	in >> T;

//	Case cur;
	cout<<"got here!\n";

	int N;
	int array [1000];
	int inOrder;
	int* sorted;
	for (int i = 0; i<T; i++)
	{
		inOrder = 0;
		//initialize case CODE HERE
		cout<<"and here:"<<i<<endl;
		in >> N;
		for (int j = 0; j<N; j++)
		{
			in>> array[j];
		}
	    sorted = sort(array,N);
	    for (int j = 0; j<N; j++)
	    {
	    	if (array[j]==sorted[j])
	    		inOrder++;
	    }


		
		//run case & add to output file
		out << "Case #" << i+1 << ": "<< N-inOrder << endl;
	}		
	//close input file
	in.close();
	//close output file
	out.close();
	return 0;
}





