#include <iostream>
#include <map>
#include <set>
#include <vector>

int nCases;
int nCombinations;
int nDestructions;
int nInvocationLength;
std::map<char, std::map<char, char>> mapCombinations;
std::map<char, std::set<char>> mapDestructions;
std::vector<char> vInvocation;
std::vector<char> vSolution;

void reset()
{
	mapCombinations.clear();
	mapDestructions.clear();
	vInvocation.clear();
	vSolution.clear();
}

void read_input()
{
	std::cin >> nCombinations;
	for (int i = 0; i < nCombinations; i++)
	{
		char a, b, c;
		std::cin >> a;
		std::cin >> b;
		std::cin >> c;
		mapCombinations[a][b] = c;
		mapCombinations[b][a] = c;
	}

	std::cin >> nDestructions;
	for (int i = 0; i < nDestructions; i++)
	{
		char a, b;
		std::cin >> a;
		std::cin >> b;
		mapDestructions[a].insert(b);
		mapDestructions[b].insert(a);
	}

	std::cin >> nInvocationLength;
	for (int i = 0; i < nInvocationLength; i++)
	{
		char a;
		std::cin >> a;
		vInvocation.push_back(a);
	}
}

void solve_input()
{
	for (int i = 0; i < nInvocationLength; i++)
	{
		char cCurrent = vInvocation[i];
		if (vSolution.size() == 0)
		{
			vSolution.push_back(cCurrent);
		}
		else
		{
			char cLast = *(vSolution.end() - 1);

			// Perform combinations
			bool bCombined = false;
			if (nCombinations > 0)
			{
				std::map<char, std::map<char, char> >::iterator it = mapCombinations.find(cLast);
				if (it != mapCombinations.end())
				{
					std::map<char, char>::iterator jt = it->second.find(cCurrent);
					if (jt != it->second.end())
					{
						char cCombo = jt->second;
						vSolution.pop_back();
						vSolution.push_back(cCombo);
						bCombined = true;
					}
				}
			}

			// Perform destructions
			bool bDestruction = false;
			if (!bCombined && nDestructions > 0)
			{
				for (int j = 0; !bDestruction && j < vSolution.size(); j++)
				{
					cLast = vSolution[j];
					std::map<char, std::set<char> >::iterator it = mapDestructions.find(cLast);
					if (it != mapDestructions.end())
					{
						std::set<char>::iterator jt = it->second.find(cCurrent);
						if (jt != it->second.end())
						{
							vSolution.clear();
							bDestruction = true;
						}
					}
				}
			}
			
			// Append if nothing occurred
			if (!bCombined && !bDestruction)
			{
				vSolution.push_back(cCurrent);
			}
		}
	}
}

void print_solution(int nCase)
{
	std::cout << "Case #" << (nCase + 1) << ": [";
	for (std::vector<char>::iterator it = vSolution.begin(); it != vSolution.end(); it++)
	{
		std::cout << *it;
		if (it + 1 != vSolution.end())
			std::cout << ", ";
	}
	std::cout << "]" << std::endl;
}

int main()
{
	std::cin >> nCases;
	for (int i = 0; i < nCases; i++)
	{
		reset();
		read_input();
		solve_input();
		print_solution(i);
	}
	return 0;
}
