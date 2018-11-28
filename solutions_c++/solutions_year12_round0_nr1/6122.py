#include <iostream>
#include <map>
#include <fstream>
#include <cstring>
#include <cctype>
int main()
{
	std::ifstream infile;
	infile.open("d://codejam/mapping.out",std::ios::binary);
	std::map<char,char> mapping;	
	char ch , ch1;
	while (infile.get(ch)&&infile.get(ch1))
	{
		mapping[ch] = ch1;
	}
	infile.close();

	//here we go.....

	infile.open("D:\\codejam\\A-small-attempt1.in" , std::ios::binary);
	freopen("D:\\codejam\\A-small.out","wt",stdout);

	int tests;
	infile>>tests;   
	char line[103];

	while(infile.get(ch)) 
	{
		if(isspace(ch)) continue;
		else { 
			infile.putback(ch);
			break;
		}
	}

	for (int i = 1 ; i<=tests ; ++i)
	{
		std::cout<<"Case #"<<i<<": ";
		infile.getline(line , 102);

		for (int j=0 ; j<strlen(line) ; j++)
		{
			std::cout<<mapping[line[j]];
		}
		std::cout<<std::endl;
	}
	return 0;
}