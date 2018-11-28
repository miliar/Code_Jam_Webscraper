#include <iostream>

int main()
{
    int t;
    std::cin >> t;

    for(int i=1; i<=t; ++i)
    {
	int r, k, n;
	std::cin >> r >> k >> n;
	int* groups = new int[n];
	for(int j=0; j!=n; j++)
	{
	    std::cin >> groups[j]; 
	}
	int count = 0;
	int curIdx=0;
	int passengers = 0;
	for(int j=0; j!=r; ++j)
	{
	    for(int groupCount=0; groupCount!=n; groupCount++)
	    {
		if(passengers+groups[curIdx] <= k)
		{
		    passengers+=groups[curIdx];
		    curIdx = (curIdx+1)%n;
		}
		else
		    break;
	    }
	    count += passengers;
	    passengers =0;
	}
	std::cout << "Case #" << i << ": " << count << std::endl;
    }

    return 0;
}
