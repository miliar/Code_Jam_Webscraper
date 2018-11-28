#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <math.h>

using namespace std;

int nTestCases;
fstream	fin;
fstream fout;

int N;
int K;
int B;
int T;
int pos[50];
int vol[50];

//vector<int> chickIdx[50];

void main()
{
	fin.open("z:\\input.txt", ifstream::in);
	fout.open("z:\\output.txt", ifstream::out);

	
	fin >> nTestCases;
	int countArri;
	int countOpt;

	for(int testCase = 1; testCase <= nTestCases; testCase++){
		
		fin>>N;
		fin>>K;
		fin>>B;
		fin>>T;
		
		for(int i=0;i<N;i++){
			fin>>pos[i];	
		}

		for(int i=0;i<N;i++){
			fin>>vol[i];	
		}

		countArri=0;
		countOpt=0;

		for(int i=N-1;i>=0;i--){
			if(vol[i]*T+pos[i]>=B){
				countArri++;
				if (countArri>=K)
					break;
			}
			else{
				countOpt=K-countArri+countOpt;
			}
			
		}

		if(countArri==K)
			fout << "Case #" << testCase <<": " <<countOpt<<endl;
		else
			fout << "Case #" << testCase <<": " <<"IMPOSSIBLE"<<endl;
	}

	fin.close();
	fout.close();
}