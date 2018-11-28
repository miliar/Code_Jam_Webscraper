#include <fstream.h>
#include <string.h>

int main()
{
	ifstream fin("1.in");
	ofstream fout("1.out");
	
	int T, i, j, N, S, p, count, counts;
	int t;
	int score[100][3];
	int ascore[3];
	
	fin >> T;
	for (i = 0; i<T; i++)
	{
		fin >> N;
		fin >> S;
		fin >> p;
		count = 0;
		counts = 0;
		for (j = 0; j<N; j++) 
		{
			fin >> t;
			switch (t % 3)
			{
				case 0: 
				{
					ascore[0] = t / 3;
					ascore[1] = t / 3;
					ascore[2] = t / 3;
					break;
				};
				case 1:
				{
					ascore[0] = t / 3;
					ascore[1] = t / 3;
					ascore[2] = t / 3 + 1;
					break;
				};
				case 2:
				{
					ascore[0] = t / 3;
					ascore[1] = t / 3 + 1;
					ascore[2] = t / 3 + 1;
					break;
				};
			}
			//fout << ascore[0] << ' ' << ascore[1] << ' ' << ascore[2] << endl;
			
			if (ascore[2] >= p) { counts++; continue;};
			if ((ascore[2] + 1 < p) || (ascore[0] - 1 <0) || (ascore[2] + 1 - (ascore[1] - 1) > 2)) continue;
			count++;
		};
		counts += min(S, count);
		
		fout << "Case #" << i+1 << ": " << counts << endl;
	}
	
	fin.close();
	fout.close();
}