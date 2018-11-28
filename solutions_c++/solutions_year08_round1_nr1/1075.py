#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;


bool UDgreater ( int elem1, int elem2 );

int main()
{
	// read file
	ifstream infile("A-small-attempt0.in");
	ofstream outfile("A-small-result.out");

	int N;
	vector<int> vec1, vec2;
	
	int vecnum;
	infile >> N;   // case number

	int i,j,k;
	int tmp;
	int sum = 0;
	for(i = 0; i < N; i++)
	{	
		vec1.clear();
		vec2.clear();

		int number;
		sum = 0;
		infile >> vecnum;

		for(j = 0; j < vecnum; j++)
		{
			// input the vector
			infile >> number;
			vec1.push_back(number);
		}
		for(j = 0; j < vecnum; j++)
		{
			// input the vector
			infile >> number;
			vec2.push_back(number);
		}

		sort(vec1.begin(), vec1.end());
		sort(vec2.begin(), vec2.end());

		tmp = 0;
		j=0;
		k=vecnum-1;
		while (tmp < vecnum)
		{
			sum = sum + vec1[j]*vec2[k];
			j++;
			k--;
			tmp++;
		}

		outfile << "Case #" << i+1 << ": " << sum << endl;
	}
	
	infile.close();
	outfile.close();
	return 0;
}

bool UDgreater ( int elem1, int elem2 )
{
   return elem1 > elem2;
}

