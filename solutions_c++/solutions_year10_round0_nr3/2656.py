#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	ifstream fin("c.in");
	ofstream fout("c.out");
	
	int T, R, K, N, C, S;
	int i, j, k, l;
	int Q[20];
	
	fin >> T;
	
	for(j = 1 ; j <= T ; j++)
	{
		fin >> R >> K >> N;
		
		for(i = 0; i < N; i++) fin >> Q[i];
		
		k = S = 0;
		
		while(R--)
		{
			C = 0;
			for(l = 0; l < N; l++)
			{
				if(C + Q[k] > K) break;
				
				C += Q[k];
				k++;
				if(k == N) k = 0;
			}
			S += C;
		}
		
		fout << "Case #" << j << ": " << S << endl;
	}
}