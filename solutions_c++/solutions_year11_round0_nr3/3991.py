using namespace std;
#include <iostream>
#include <vector>
#include <cmath>

void check_situation(long long &result, long long n, vector<long long> candy)
{
	long long asum=0;
	long long arealsum=0;
	long long bsum=0;
	long long brealsum=0;
	long long index=0;
	
	while (n!=0)
	{
		if (n&1)
		{
			asum^=candy[index];
			arealsum+=candy[index];
		}
		else
		{
			bsum^=candy[index];
			brealsum+=candy[index];
		}
		
		n >>= 1;
		++index;
	}
	
	if (asum==bsum)
	{
		if (arealsum > brealsum && arealsum > result)
			result=arealsum;
		else if (arealsum < brealsum && brealsum > result)
			result=brealsum;
		else if (arealsum == brealsum && arealsum > result)
			result=arealsum;
		else if (arealsum == brealsum && brealsum > result)
			result=brealsum;
	}
}

int main()
{
	int cases;
	int n_count;
	int buffer;
	
	long long result=0;
	
	vector<long long> input;
	vector<long long> output;

	cin >> cases;
	while (cases>0)
	{
		cin>>n_count;
		while (n_count>0)
		{
			cin >> buffer;
			input.push_back(buffer);
			--n_count;
		}
		
		//process
		for (unsigned long long index= (pow(2, input.size())/2); index<pow(2, input.size())-1; ++index)
		{
			check_situation(result, index, input);
		}
		
		//save result
		if (result!=0)
			output.push_back(result);
		else
			output.push_back(-1);
			
		input.clear();
		result=0;
		--cases;
	}
	
	for (unsigned long long index=0; index<output.size(); ++index)
	{
		if (output[index]==-1)
			cout << "Case #" << index+1 << ": NO" << endl;
		else
			cout << "Case #" << index+1 << ": " << output[index] << endl;
	}
	
	
	return 0;
}
