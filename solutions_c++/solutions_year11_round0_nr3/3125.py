#include <iostream>
#include <fstream>
#include <string>

using namespace std;

#define lint long long
#define uint usigned long long

int main (int argc, char * const argv[]) {
    
	ifstream inFile("../../input.txt");
	ofstream outFile("../../output.txt");
	int numCases;
	inFile >> numCases;
	for(int caseNum =1; caseNum <=numCases; caseNum++)
	{
		int numCandyPieces;
		inFile >> numCandyPieces;
		int minCandy=1000001, dumbSum=0, realSum=0, newPiece;
		for(int cntr=0; cntr < numCandyPieces; cntr++)
		{
			inFile>> newPiece;
			if(newPiece <minCandy)
				minCandy= newPiece;
		
			dumbSum ^=newPiece;
			realSum +=newPiece;
		}
		
		if(dumbSum != 0)
		{
			outFile<<"Case #"<<caseNum<<": NO\n";
			cout<<"Case #"<<caseNum<<": NO\n";
		}
		else
		{
			outFile<<"Case #"<<caseNum<<": "<<realSum-minCandy<<"\n";
			cout<<"Case #"<<caseNum<<": "<<realSum-minCandy<<"\n";
			
		}
		
	}
	inFile.close();
	outFile.close();
	std::cout << "Done!\n";
    return 0;
}
