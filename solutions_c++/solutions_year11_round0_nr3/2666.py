#include <iostream.h>
#include <fstream.h>
#include <vector.h>
#include <numeric.h>

// Code Jam 2011
// Qualification Round
// C. Candy Splitting


int main(int argc, char *argv[])
{
	int T,t;
	int N,n;
	
	int answer;
	int sum;
	
	int candy;
	
	int gotcandy;
	
	vector<int> numbers;
	
	vector<int>::iterator iter;
	
	ifstream inFile;
	
	//inFile.open("test.in");
	if ( argc < 2 )
	{
		cout << "No input file given!" << endl;
		exit(1);
	}
	inFile.open(argv[1]);
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	inFile >> T;
	
	for (t=0;t<T;t++)
	{
		inFile >> N;
		
		numbers.clear();
		answer = 0;
		sum = 0;
		gotcandy = 0;
		
		for (n=0;n<N;n++)
		{
			inFile >> candy;
			numbers.push_back(candy);
		}
		
		int nn = 0;
		for(unsigned int x = 0; x < numbers.size(); x++)
		{
			nn = nn^numbers[x];
		}
		
		if ( nn == 0 )
		{
			sort (numbers.begin(), numbers.end());
			numbers[0] = 0;
			sum = 0;
			for(unsigned int x = 0; x < numbers.size(); x++)
			{
				sum = sum + numbers[x];
			}
			answer = sum;
		}
		
		
		if ( answer == 0 )
			cout << "Case #" << t+1 << ": NO" << endl;
		else
			cout << "Case #" << t+1 << ": " << answer << endl;
	}
		
		
	
	inFile.close();
	return 0;
}