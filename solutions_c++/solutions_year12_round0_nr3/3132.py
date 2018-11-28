#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

//Checks if two numbers are cyclic
bool areCyclic(string original, string resultado)
{
	unsigned int r_ptr;
	vector<int> ptrs;

	//We find all the possible connection points
	bool esta = false;
	for(unsigned int i=0; i<resultado.length(); ++i)
	{
		if(resultado[i] == original[0])
		{
			esta = true;
			ptrs.push_back(i);
		}
	}

	//If we haven't found any, then they aren't cyclic
	if(!esta)
	     return false;

	//Otherwise, we check every connection point
	for(unsigned int j = 0; j<ptrs.size(); ++j)
	{
		//We assume it's the connection point we're looking for
		r_ptr = ptrs[j];
		esta = true;
		
		//We check if the remaining letters also match
		for(unsigned int i = 0; i<original.size(); ++i)
		{
			//If we find two that don't, then these AREN'T the droids we're looking for
		     	if(original[i] != resultado[r_ptr])
		     	{
				esta = false;
				break;
		     	}

			//Increase the counter
		     	++r_ptr;

			//We check the loop
		     	if(r_ptr == resultado.size())
				r_ptr = 0;
		}

		//If this IS the connection point we're looking for, then the numbers are cyclic
		if(esta)
			return true;
	}

	//If no connection point has found the answer, then they're not cyclic
     	if(!esta)
        	return false;
}

int main()
{
	int T, A, B;
	int recycled;
	
	string first, second;

	//Get the number of test cases
	cin >> T;

	//For each test case
	for(int w = 0; w<T; ++w)
	{
		//Reset the number of recycled numbers
		recycled = 0;

		//Get A and B
		cin >> A >> B;

		for(int i = A; i<=B; ++i)
			for(int j = i+1; j<=B; ++j)
			{
				stringstream sf, ss;
				sf << i;
				first = sf.str();

				ss << j;
				second = ss.str();

				//If they don't have the same length, don't even check
				if(first.length() != second.length())
					continue;

				if(areCyclic(first, second))
					++recycled;
			}

		//Print how many cyclic numbers we have
		cout << "Case #" << w+1 << ": " << recycled << endl;

	}
}
