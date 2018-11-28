#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <iostream>

int main(int argc, char **argv)
{
	int L,D,N,w;
	std::vector<std::string> words;
	std::cin >> L >> D >> N; 	
	words.reserve(D); 
	char t; 
	w = D; 
	while (w--)
	{
		std::string word;
		std::cin >> word ;
		words.push_back(word);
	}
	char maskStr[15 * 30];  
	std::cin.getline(maskStr, sizeof(maskStr));  

	for (int i = 1; i <= N; i++)
	{
	    bool mask[20][28];
	    memset(&mask, 0, sizeof(mask));
	    maskStr[0] = 0; 
	    std::cin.getline(maskStr, sizeof(maskStr));  
		int j = 0; 
		char *p = maskStr; 
		while (*p)
		{
			if (isalpha(*p))
			{
				mask[j++][*p - 'a'] = 1; 
			} else if (*p == '(')
			{
				p++;
				while (*p != ')')
				{
					mask[j][*p - 'a'] = 1; 
					p++; 
				}
				j++; 
			}
			else
			{
				std::cerr << "Unexpected char: " << *p << std::endl; 
			}
			p++; 
		}
		
		int count = 0; 
		for (int k = 0; k < D; k++)
		{
			int x; 
			for (x = 0; x < L; x++)
			{
				if (!mask[x][words[k][x] - 'a'])
					break;
			}
			if (x == L)
				count++; 
		}
		std::cout << "Case #" << i << ": " << count << std::endl; 
	    	
	}

}
