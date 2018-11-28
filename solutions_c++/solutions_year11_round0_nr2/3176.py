#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char **argv)
{
	ifstream in(argv[1]);
	if (!in)
	{
		cout << "Cannot open file";
		return 1;
	}

	int T, N, C, D;
	char combi[26][26];
	char b1, b2, nb, lastb;
	
	in >> T;
	for (int i = 1; i <= T; ++i)
	{
		// read combinations
		memset(combi, 0, sizeof(char)*26*26);
		in >> C;
		for (int c = 0; c < C; ++c)
		{
			in >> b1 >> b2 >> nb;
			b1 -= 'A'; b2 -= 'A';
			combi[b1][b2] = nb;
			combi[b2][b1] = nb;
		}
		// read anti
		vector<char> anti[26];
		in >> D;
		for (int d = 0; d < D; ++d)
		{
			in >> b1 >> b2;
			anti[b1 - 'A'].push_back(b2);
			anti[b2 - 'A'].push_back(b1);
		}
		// read element invoke list
		in >> N;
		vector<char> elems;
		int curAnti[26] = { 0 };		
		for (int n = 0; n < N; ++n)
		{
			in >> b1;
			if (elems.empty())
			{
				elems.push_back(b1);
				// add b1's anti elems to curAnti
				for (int a = 0, size = anti[b1 - 'A'].size(); a < size; ++a)
					curAnti[anti[b1 - 'A'][a] - 'A']++;
				continue;
			}
			lastb = elems.back();
			// check for combi
			if (combi[lastb - 'A'][b1 - 'A'])
			{
				// combine
				elems.back() = combi[lastb - 'A'][b1 - 'A'];
				// update curAnti
				for (int a = 0, size = anti[lastb - 'A'].size(); a < size; ++a)
					curAnti[anti[lastb - 'A'][a] - 'A']--;
			}
			// check for anti
			else if (curAnti[b1 - 'A'])
			{
				memset(curAnti, 0, sizeof(int)*26);
				elems.clear();
			}
			// add elem to list
			else
			{
				elems.push_back(b1);
				// add b1's anti elems to curAnti
				for (int a = 0, size = anti[b1 - 'A'].size(); a < size; ++a)
					curAnti[anti[b1 - 'A'][a] - 'A']++;
			}
		}
		
		if (elems.empty())
			printf("Case #%d: []\n", i);
		else
		{
			printf("Case #%d: [", i);
			for (int v = 0; v < elems.size() - 1; ++v)
				printf("%c, ", elems[v]);
			printf("%c]\n", elems.back());
		}
	}	

	return 0;
}