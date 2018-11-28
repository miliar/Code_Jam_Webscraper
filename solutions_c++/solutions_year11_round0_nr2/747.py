#include <fstream.h>
#include <list>
using namespace std;
int ch2i(char let){
	switch (let){
		case 'Q': return 0;
		case 'W': return 1;
		case 'E': return 2;
		case 'R': return 3;
		case 'A': return 4;
		case 'S': return 5;
		case 'D': return 6;
		case 'F': return 7;
	}
	return 8 + let; /* non-base */
}
char letters[8] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
bool opp[8][8];
int rep[8][8], cntLet[8];

void clearRep()
{
	for (int i = 0; i< 8; i++)
		for (int j = 0; j< 8; j++)
			rep[i][j] = -1;
}
void clearOpp()
{
	for (int i = 0; i< 8; i++)
		for (int j = 0; j< 8; j++)
			opp[i][j] = false;
}
void clearLet()
{
	for (int i = 0; i< 8; i++)
		cntLet[i] = 0;
}
int main()
{
	int T, C, D, N;
	char c1, c2, c3, last;
	list<int> seq;
	
	fstream fin("magick.txt",ios::in);
	fstream fout("magick_out.txt",ios::out);

	fin >> T;
	for (int t=0; t<T; t++)
	{
		clearRep();
		fin >> C;
		for (int c = 0; c < C; c++)
		{
			fin >> c1 >> c2 >> c3;
			rep[ch2i(c1)][ch2i(c2)] = ch2i(c3);
			rep[ch2i(c2)][ch2i(c1)] = ch2i(c3);
		}

		clearOpp();
		fin >> D;
		for (int d = 0; d < D; d++)
		{
			fin >> c1 >> c2;
			opp[ch2i(c1)][ch2i(c2)] = true;
			opp[ch2i(c2)][ch2i(c1)] = true;
		}

                clearLet();
		fin >> N;
		for (int n = 0; n < N; n++)
		{
			fin >> c1;
                        last = ch2i(c1);
retry:
			if (0 == seq.size())
			{
				seq.push_back(last);
				if (last < 8)
					cntLet[last]++;
				continue;
			}
			if (last < 8)
			{
				if (8 > seq.back() && -1 != rep[seq.back()][last])
				{
					cntLet[seq.back()]--;
					last = rep[seq.back()][last];
					seq.pop_back();
					goto retry;
				}
				for (int i = 0; i < 8; i++)
				{
					if (opp[last][i] && cntLet[i] > 0)
					{
						clearLet();
						seq.clear();
						break;
					}
				}
			}
			if (0 != seq.size())
			{
				seq.push_back(last);
				if (last < 8)
					cntLet[last]++;
			}
		}
		
		fout <<  "Case #" <<  t + 1 << ": [";
		while (seq.size() != 0)
		{
			last = seq.front();
			fout <<  (last > 8 ? (char)(last - 8) : letters[last]);
			seq.pop_front();
			if (seq.size() != 0)
				fout <<  ", ";
		}
		fout << "]\n";
	}

	fin.close();
	fout.close();

	return 0;
}
