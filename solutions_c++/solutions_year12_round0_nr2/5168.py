#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <memory>
#include <vector>

int main(int argc, const char* argv[])
{
	std::ifstream input(argv[1]);
	std::ofstream output("output1.txt");

	char currLine[255];

	input.getline(currLine, 255);
	int testcases = std::atoi(currLine);

	for(int i = 0; i < testcases; ++i)
	{
		input.getline(currLine, 255);
		char* pEnd;
		long googlers = std::strtol(currLine,&pEnd, 10);
		long suprisings = std::strtol(pEnd, &pEnd, 10);
		long p = std::strtol(pEnd, &pEnd, 10);

		int result =  0;

		if(p >= 0 && p <= 10)
		{
			std::vector<long> sums;
			for(long j = 0; j < googlers; ++j)
			{
				sums.push_back(std::strtol(pEnd, &pEnd, 10));
			}
		
			for(size_t l = 0; l < sums.size(); ++l)
			{
				long tmp = sums[l];
				long currP = p;
				bool found = false;
				while(currP <= 10 && !found)
				{
					tmp = sums[l];
					tmp -= currP;

					if(currP+currP == tmp) //case: p,p,p
					{
						++result;
						found = true;
					}

					if(!found && (currP-1)>=0)
					{
						if(((currP-1)+currP) == tmp) // p, p, p-1
						{
							++result;
							found = true;
						}
						else if((2*(currP-1)) == tmp) // p-1,p-1,p
						{
							++result;
							found = true;
						}
					}

					if(!found && (currP+1) <= 10)
					{
						if(((currP+1)+currP)==tmp) // p, p, p+1
						{
							++result;
							found = true;
						}
						else if(((currP+1)+(currP+1))==tmp) // p, p+1, p+1
						{
							++result;
							found = true;
						}
					}


					if(!found)
					{
						if(suprisings > 0)
						{					
							if((currP-2) >= 0)
							{
								if((2*(currP-2)) == tmp) // p, p-2, p-2
								{
									--suprisings;
									++result;
									found = true;
								}
								else if((currP+(currP-2))==tmp) // p, p, p-2
								{
									--suprisings;
									++result;
									found = true;
								}
								else if(((currP-1)+(currP-2))==tmp) //p, p-1, p-2
								{
									--suprisings;
									++result;
									found = true;
								}
							}
						
							if(!found && (currP+2) <= 10)
							{
								if((2*(currP+2))==tmp) //p, p+2, p+2
								{
									--suprisings;
									++result;
									found = true;
								}
								else if((currP+(currP+2))==tmp) // p, p, p+2
								{
									--suprisings;
									++result;
									found = true;
								}
								else if((currP+(currP+1)+(currP-2))== tmp) // p, p+1, p+2
								{
									--suprisings;
									++result;
									found = true;
								}
							}

							if(!found && (currP-1) >= 0)
							{
								if((currP+(currP-1)+(currP+1))==tmp) // p, p-1, p+1
								{
									--suprisings;
									++result;
									found = true;
								}
							}
						}
					}					
					++currP;				
				}
			}
		}
		output << "Case #" << i+1 << ": " << result << std::endl;
		std::cout << "Case #" << i+1 << ": " << result << std::endl;
	}

	std::cin.get();
}