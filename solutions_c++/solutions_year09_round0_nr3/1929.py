#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int subSeq(const char * src, const char * tar)
{
	int num = 0;
	
	if (strlen(src) == 1)
	{
		while (*tar != '\0')
		{
			if (*src == *tar)
			{
				num++;	
			}
			tar++;
		}
	}else 
	{
		do
		{
			if (*src == *tar)
			{
				num += subSeq(src + 1, tar + 1);	
			}
			tar++;
		}while(*tar != '\0');
	}		
	return num;	
}

int main()
{
	ifstream infile("C-small-attempt1.in");
	ofstream outfile("C-small-attempt1.out");

	int N = 0;
	char * src = "welcome to code jam", tar[500];
	
	infile >> N;
	
	infile.get();

	for (int i = 0; i < N; i++)
	{
		int num = 0;
		
		infile.getline(tar, 500);
		
		cout << "tar: " << tar << endl;
		
		num = subSeq(src, tar) % 10000;
			
		outfile << "Case #" << i + 1 << ": ";
		
		outfile.fill('0');
		outfile.width(4);
		
		outfile << num << endl;
	}
	
	infile.close();
	outfile.close();
	getchar();
	return 0;
}
