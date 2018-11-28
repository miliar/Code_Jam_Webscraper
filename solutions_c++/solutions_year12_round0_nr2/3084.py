#include <iostream>
#include <string>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::string;
using std::vector;


struct tDancer
{
	int numberOfDancers;
	int surprises;
	int p;
	int scores[200];

	int result;
	int surprisesUsed;
};



void determineResult(tDancer &input)
{
	int avg;
	int result = 0, iter = 0, usedSurprises = 0;

	for(; iter < input.numberOfDancers; iter++)
	{
		avg = ( (input.scores[iter]) / 3);
		if(avg < input.p)
		{
			int num1,num2,num3;
			{
				bool notFound = true;
				bool first = true;
				int least = ( (input.scores[iter]) / 3) - 2;
				int max = least + 5;
				if(least < 0)
					least = 0;
				for(num1 = least; (num1 <= max) && notFound; num1++)
					for(num2 = least; (num2 <= max) && notFound; num2++)
						for(num3 = least; (num3 <= max) && notFound; num3++)
						{
							if((num1 + num2 + num3) == (input.scores[iter]))
							{
								if( (num1 >= input.p) || (num2 >= input.p) || (num3 >= input.p))
								{
									if( (num1 < (num2 + 2)) 
										&& (num1 < (num3 + 2)) 
										&& (num2 < (num1 + 2)) 
										&& (num2 < (num3 + 2)) 
										&& (num3 < (num1 + 2)) 
										&& (num3 < (num2 + 2)))
									{
										notFound = false;
									}
								}
							}
						}
				if((notFound) && (usedSurprises < input.surprises))
				{
					first = false;
					for(num1 = least; (num1 <= max) && notFound; num1++)
						for(num2 = least; (num2 <= max) && notFound; num2++)
							for(num3 = least; (num3 <= max) && notFound; num3++)
							{
								if((num1 + num2 + num3) == (input.scores[iter]))
								{
									if( (num1 >= input.p) || (num2 >= input.p) || (num3 >= input.p))
									{
										if( (num1 <= (num2 + 2)) 
											&& (num1 <= (num3 + 2)) 
											&& (num2 <= (num1 + 2)) 
											&& (num2 <= (num3 + 2)) 
											&& (num3 <= (num1 + 2)) 
											&& (num3 <= (num2 + 2)))
										{
											notFound = false;
										}
									}
								}
							}
				}
			
				if(!notFound)
				{
					result++;
					if(!first)
						usedSurprises++;
				}
			}
		}
		else
		{
			result++;
		}
	}

	input.result = result;
	input.surprisesUsed = usedSurprises;
	
	
}

int main()
{
	int T; // Total number of inputs
	vector<tDancer> inputList;
	tDancer current;

	int iter, iter2;

	cin>>T;

	

	for(iter=0;iter<T;iter++)
	{
		cin.ignore();
		cin>>current.numberOfDancers;
		cin>>current.surprises;
		cin>>current.p;
		for(iter2 = 0;iter2 < current.numberOfDancers;iter2++)
		{
			cin>>current.scores[iter2];
		}
		current.result = 0;
		inputList.push_back(current);
	}

/*
	for(iter=0;iter<inputList.size();iter++)
	{
		cout<<inputList[iter].numberOfDancers<<endl;
		cout<<inputList[iter].surprises<<endl;
		cout<<inputList[iter].p<<endl;
		for(iter2 = 0;iter2 < inputList[iter].numberOfDancers;iter2++)
		{
			cout<<inputList[iter].scores[iter2]<<"\t";
		}
		cout<<endl<<inputList[iter].result<<endl<<endl;
	}
*/
	
	for(iter=0;iter<inputList.size();iter++)
	{
		determineResult(inputList[iter]);
		cout<<"Case #"<<(iter+1)<<": "<<inputList[iter].result<<endl;
	}

	return 0;
}

