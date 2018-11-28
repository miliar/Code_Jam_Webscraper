// ==============================================
// ==Author: zerosumi@gmail.com
// ==School: Beijing Institute of Technology
// ==============================================

#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream filein("C:\\Users\\zerosumi\\Project\\tmp\\Debug\\in.txt");
	ofstream fileout("C:\\Users\\zerosumi\\Project\\tmp\\Debug\\out.txt");
	int T, R, K, N;
	filein >> T;
	int group[1001];
	int chead, thead;
	int inpeople, tinpeople;
	int cfee;
	for (int h = 1; h <= T; h++)
	{
		cfee = 0;
		chead = 1;
		filein >> R;
		filein >> K;
		filein >> N;
		for (int i = 1; i <= N; i++) {
			filein >> group[i];
		}
		if (N == 1)
		{
			cfee = group[chead] * R;
		}
		else {
			for (int i = 1; i <= R; i++)
			{
				thead = chead == N ? 1 : (chead + 1);
				inpeople = group[chead];
				for (int j = 1; j <= N; j ++)
				{
					if (chead == thead)
					{
						cfee+=inpeople;
						break;
					}
					tinpeople = inpeople + group[thead];
					if (tinpeople > K)
					{
						chead = thead;
						cfee += inpeople;
						break;
					}
					else
					{
						inpeople = tinpeople;
						thead = thead == N ? 1 : (thead + 1);
					}


				}
			}
		}
		fileout << "Case #" << h << ": " << cfee << endl;
	}
}
