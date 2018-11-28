#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	unsigned int T = 0;
	unsigned int N = 0;
	unsigned long int K = 0;
	string result = "";
	
	int click = 1;		//	Clicks
	int pInc = 0;		//	Previous increment
	int cInc = 2;		//	Current increment
	
	ifstream fin ("A-large.in");
	ofstream fout ("A-large.out");
	
	fin >> T;
	
	for(int i = 1; i <= T; i++)
	{
		click = 1;
		pInc = 0;
		cInc = 2;
		result = "";
		
		fin >> N >> K;
		
		if(!K)
		{
			result = "OFF";
		}
		else if(N == 1)
		{
			if(((K - N) % (N + 1)) == 0)
			{
				result = "ON";
			}
			else
			{
				result = "OFF";
			}
		}
		else
		{
			for(int j = 2; j <= N; j++)
			{
				cInc += pInc;
				click += cInc;
				pInc = cInc;
			}
			
			if(((K - click) % (1 + click)) == 0)
			{
				result = "ON";
			}
			else
			{
				result = "OFF";
			}
		}
		
		fout << "Case #" << i << ": " << result << endl;
	}
}
