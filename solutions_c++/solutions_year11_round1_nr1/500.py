#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define lint long long
#define uint unsigned long long

int main (int argc, char * const argv[]) {
    
	ifstream inFile("../../input.txt");
	ofstream outFile("../../output.txt");
	int numCases;
	inFile >> numCases;
	for(int caseNum =1; caseNum <=numCases; caseNum++)
	{
		uint N, Pd, Pg;
		inFile >> N;
		inFile >> Pd;
		inFile >> Pg;
		
		if(Pg == 100)
			if(Pd == 100)
			{
				outFile<<"Case #"<<caseNum<<": Possible\n";
				continue;
			}
			else {
				outFile<<"Case #"<<caseNum<<": Broken\n";
				continue;
			}
		
		if(Pg == 0)
			if(Pd == 0)
			{
				outFile<<"Case #"<<caseNum<<": Possible\n";
				continue;
			}
			else {
				outFile<<"Case #"<<caseNum<<": Broken\n";
				continue;
			}

		
		
		if(N >=100 || Pd == 0)
		{
			outFile<<"Case #"<<caseNum<<": Possible\n";
			continue;
		}
		
		bool success = false;
		for(int D=N; D>0; D--)
		{
			if(D*Pd % 100 == 0)
			{
				outFile<<"Case #"<<caseNum<<": Possible\n";
				success=true;
				break;
			}
		}
		if(!success)
			outFile<<"Case #"<<caseNum<<": Broken\n";
		
	}
	inFile.close();
	outFile.close();
	std::cout << "Done!\n";
    return 0;
}
