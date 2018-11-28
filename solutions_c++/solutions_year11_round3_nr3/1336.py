#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  

using namespace std;

unsigned __int64 gcd(unsigned __int64 a, unsigned __int64 b)
{
int temp;

while(b)
{
temp = a % b;
a = b;
b = temp;
}

return(a);
}

int main()
{
	unsigned __int64 T;
	std::cin >> T;
	unsigned __int64 case_num = 1;
//std::sort(notes.begin(),notes.end());

	while(case_num <= T)
	{
		unsigned __int64 N,L,H; 
		std::cin >> N>>L>>H;
		vector<unsigned __int64>  notes(N);
		vector<unsigned __int64> abc(H-L+1);
		for(unsigned __int64 i = L ; i <= H ; i++)
		{
			abc[i-L] = i;
		}
		for(unsigned __int64 i =0; i< N ; i++)
		{
			std::cin >> notes[i];
		}
		//vector<unsigned __int64>
		int poss = 1;
		for(unsigned __int64 i = L ; i <= H ; i++)
		{
			poss = 1;
			if(abc[i-L] == 0)
			{
				poss = 0; continue;
			}
			unsigned __int64 gc= i;
			for(unsigned __int64 j =0; j< N ; j++)
			{
				if(notes[j]%i > 0 && i%notes[j] > 0)
				{
					poss = 0 ;
					break;
				}
			}	
			if(poss == 1)
			{
				poss = i;
				break;
			}
			/*else
			{
				for(int k = i ;k < H+1 ; k++)
				{
					if(abc[k-L]%i == 0)
						abc[k-L] = 0;
				}
			}*/
		}
		if(poss == 0)
		{
			std::cout << "Case #" << case_num << ": " << "NO" << std::endl;
		}
		else
		{
			std::cout << "Case #" << case_num << ": " << poss << std::endl;
		}
		
		case_num++;
	}
//	std::cin >> T;
	return 1;
}