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
	
	double weights[500][500];
	for(int caseNum =1; caseNum <=numCases; caseNum++)
	{
		int rows, cols;
		uint initialW;
		inFile>>rows;
		inFile>>cols;
		inFile>>initialW;
		
		for(int y=0; y<rows; y++)
			for(int x=0; x<cols; x++)
			{
				char tmpC;
				inFile >> tmpC;
				weights[x][y] = tmpC-'0';
				//weights[x][y]+=initialW;
			}
		
		bool slnFnd = false;
		int maxFnSz = rows;
		if(cols<rows)
			maxFnSz = cols;
		for(;maxFnSz>2;maxFnSz--)
		{
			for(int fnPosY=0; fnPosY <= rows-maxFnSz; fnPosY++)
			{
				for(int fnPosX=0; fnPosX <= cols-maxFnSz; fnPosX++)
				{	
					double centX= ((double)maxFnSz-1)/2+fnPosX;
					double centY = ((double)maxFnSz-1)/2+fnPosY;
					double weightX =0;
					double weightY =0;
					
					if(fnPosX==1 && fnPosY==1)
						weightY=0;
					
					for(int cntr=1;cntr<maxFnSz-1;cntr++)
					{
						weightX+=weights[fnPosX+cntr][fnPosY] *(fnPosX+cntr - centX);
						weightY+=weights[fnPosX+cntr][fnPosY] *(fnPosY - centY);
					}
					for(int cntr2=1;cntr2<maxFnSz-1;cntr2++)
						for(int cntr=0;cntr<maxFnSz;cntr++)
						{
							weightX+=weights[fnPosX+cntr][fnPosY+cntr2] *(fnPosX+cntr - centX);
							weightY+=weights[fnPosX+cntr][fnPosY+cntr2] *(fnPosY+cntr2 - centY);
						}
					for(int cntr=1;cntr<maxFnSz-1;cntr++)
					{
						weightX+=weights[fnPosX+cntr][fnPosY+maxFnSz-1] *(fnPosX+cntr - centX);
						weightY+=weights[fnPosX+cntr][fnPosY+maxFnSz-1] *(fnPosY+maxFnSz-1 - centY);
					}
					
					if(weightX==0 && weightY==0)
						slnFnd = true;
					if(slnFnd)
						break;
				}	
				if(slnFnd)
					break;
			}
			if(slnFnd)
				break;
		}
		if(slnFnd)
			outFile<<"Case #"<<caseNum<<": "<<maxFnSz<<"\n";
		else
			outFile<<"Case #"<<caseNum<<": IMPOSSIBLE\n";
	}
	inFile.close();
	outFile.close();
	std::cout << "Done!\n";
    return 0;
}
