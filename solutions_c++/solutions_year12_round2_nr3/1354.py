#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <map>
#include <cmath>

using namespace std;

struct sum_type
{
	int c;
	int sum;
};

int sum_exists(vector<sum_type>& sums, int i)
{
	for(int k = 0; k < sums.size(); k++)
	{
		if(i == sums[k].sum) {
			return k;
		}
	}
	return -1;
}


int main()
{
	int numCases;
	cin>>numCases;

	
	for(int c = 1; c < numCases+1; c++)
	{
		int n;
		cin>>n;
		vector<int> vals;
		int t;
		for(int i = 0; i < n; i++)
		{
			cin>>t;
			vals.push_back(t);	
		}
		
		int max = pow(2, vals.size()-1);
		vector<sum_type> sums;
		printf("Case #%d:\n", c);
		for(int c=0; c <= max; c++)
		{
			if(c==max){
				printf("Impossible\n");
				break;
			}
			int theSum = 0;
			for(int i = 0; i < vals.size(); i++)
			{
				if((c>>i) & 1)
				{
					theSum+=vals[i];
				}
			}	
			int reta = sum_exists(sums, theSum);
//			printf("%d, %d!\n", c, reta);
			if(reta!=-1) {
				//found it.
				for(int i = 0; i < vals.size(); i++)
				{
					if((c>>i) & 1)
					{
						printf("%d ", vals[i]);
					}
				}
				printf("\n");
				for(int i = 0; i < vals.size(); i++)
				{
					if((reta>>i) & 1)
					{
						printf("%d ", vals[i]);
					}
				}
				printf("\n");	
				break;
			}
			sum_type thing;
			thing.c = c;
			thing.sum = theSum;		
			sums.push_back(thing);
		}
		




	}


	
}
