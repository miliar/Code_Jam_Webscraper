#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

#include <stdlib.h>

bool is_all_same(char* c)
{
	for(int i = 0; c[i] != 0; i++)
	{
		if(c[0] != c[i])
		{
			return false;
		}
	}
	return true;
}

int main(int argc, char** argv)
{
	std::ifstream ifp(argv[1]);
	int testcases;
	std::string line, line2;
	int n, m, a, b;
	
	std::getline(ifp, line);
	testcases = atoi(line.c_str());
	for(int i = 0; i < testcases; i++)
	{
		int recycles = 0;
		ifp >> line >> line2;
		std::cerr << "line:" << line << "," << line2 << std::endl;
		a = atoi(line.c_str());
		b = atoi(line2.c_str());
		n = a;
		while(n < b)
		{
			std::string sr = "", sr2 = "";
			m = b;
			while(n < m)
			{
				{ // m loops
					std::stringstream sss2;
					std::string s2 = "";
					char cs2[100], *cp2;
					char c2[100];
					int cas;
					sss2 << m;
					s2 = sss2.str();
					sss2.clear();
					
					strcpy(c2, s2.c_str());
					sr2 = "";
					for(int i2 = 0; c2[i2] != 0; i2++)
					{
						//if(i2 != 0 && is_all_same(c2)) break;
						std::stringstream ssss;
						strncpy(cs2, c2, i2);
						cs2[i2] = 0;
						cp2 = c2 + i2;
						ssss << cp2 << cs2;
						cas = atoi(ssss.str().c_str());
						//std::cout << " " << cas << std::endl;
						if(cas == n)
						{
							//std::cout << cas << "(" << n << ") == " << ca << "(" << m << ")" << std::endl;
							recycles++;
						}
					}
				}
				m--;
			}
			n++;
		}
		//std::cout << "Case #" << i+1 << ": " << recycles / (line.length() < line2.length() ? line.length() : line2.length()) << std::endl;
		std::cout << "Case #" << i + 1 << ": " << recycles << std::endl;
	}
	return 0;
}