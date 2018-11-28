#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int seq[101];
int BO[101];
int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    int T, N;
    fin >> T;
    for (int i = 1 ; i <= T; i++)
    {  
		fin >> N;

		for (int j = 1 ; j <= N ; j++)
        {	
            char c;	
			fin >> c >> seq[j];
			if (c == 'B') BO[j] = 1;
			else BO[j] = 2;
        }
		
		int current[3] = {1,1,1};
		int steps = 0; int intermediate = 0;
		for (int j = 1 ; j <= N ; j++)		
		{
            int stage = abs(seq[j]-current[BO[j]]); 
            if (BO[j] != BO[j-1]) stage = max(stage-intermediate,0);
            stage++; steps+= stage;
            current[BO[j]] = seq[j]; 

            if (BO[j] == BO[j-1]) intermediate += stage;
            else intermediate = stage;
        }
  
		fout << "Case #" << i << ": ";
		fout << steps << endl;		
    }
}
