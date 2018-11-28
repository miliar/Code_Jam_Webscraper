#include <Windows.h>
#include <fstream>
#include <string>
int main(int argc, char* argv[])
{
	printf("Output %s \n",argv[1]);
	char mapList[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

	std::ifstream infile;
	if(argc>1)
	{
		infile.open(argv[1]);
	}
	else { infile.open("input.in"); }

	int size = 0;
	infile >> size;

	if(size == 0)
	{
		printf("Kein Wort da\n");
		return 0;
	}

	std::ofstream outfile;
	outfile.open("outfile.out",std::ios::out | std::ios::app );
	std::string line;

	getline(infile,line);
	for(int i=0;i<size;i++)
	{
		//infile >> line;
		getline(infile,line);
		for(int j=0;j<line.length();j++)
		{
			if(line[j] != ' ')
			{
				int alpha = line[j] - 97;
				line[j] = mapList[alpha];
			}
		}
		outfile << "Case #" << i+1 << ": " << line << "\n";
	}
}