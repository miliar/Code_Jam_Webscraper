#include<iostream>
#include<sstream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<list>

using namespace std;

int main()
{
	int T;
	std::cin >> T;
	int case_num = 1;

	while(case_num <= T)
	{
		int correct = 0;
		unsigned __int64 N,PD,PG;
		std::cin >> N >> PD >> PG;
		//(N==1 && (PG != 100 || PG != 0)) || 
		if((PD < 100 && PG == 100) || (PD > 0 && PG  == 0))
		{
			std::cout << "Case #" << case_num << ": " << "Broken" << std::endl;
			case_num++;
			continue;
		}
		for(unsigned __int64 i = 1; i <= N; i++)
		{
			for(unsigned __int64 j = 0 ; j <= i ; j++)
			{
				if((double)(j*100)/i == (double)PD)
				{
					std::cout << "Case #" << case_num << ": " << "Possible" << std::endl;
					case_num++;
					correct = 1;
			        break;
				}
			}
			if(correct == 1)
				break;
		}
		if(correct == 0)
		{
			std::cout << "Case #" << case_num << ": " << "Broken" << std::endl;
			case_num++;
		}
	}
	std::cin >> T;
	return 1;
}
