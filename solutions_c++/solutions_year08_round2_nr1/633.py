// Crop Triangles.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
	ifstream                     input;
	int                          caseCount = 0;
	int                          A;
	int                          B;
	int                          C;
	int                          D;
	int                          i;
	int                          j;
	int                          k;
	int                          l;
	int                          m;
	int                          n;
	int                          M;
	_int64                       x;
	int                          x0;
	_int64                       x1;
	_int64                       y;
	int                          y0;
	_int64                       y1;
	_int64                       r = 0;
	ofstream                     output;
	pair < _int64, _int64 >       p;
	pair < _int64, _int64 >       s1;
	pair < _int64, _int64 >       s2;
	vector < pair < _int64, _int64 > > trees;

	input.open("Crop Triangles.in", ios_base::in);
	output.open("Crop Triangles.out", ios_base::out);

	input >> caseCount;
	for (i = 0; i < caseCount; i++)
	{
		trees.erase(trees.begin(), trees.end());
		r = 0;

		input >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

		x = x0;
		y = y0;
		for (j = 0; j < n; j++)
		{
			p.first  = x;
			p.second = y;
			trees.push_back(p);
			x = ((_int64) A * (_int64) x + (_int64) B) % M;
			y = ((_int64) C * (_int64) y + (_int64) D) % M;
		}

		for (j = 0; j < trees.size(); j++)
		{
			for (k = j + 1; k < trees.size(); k++)
			{
				for (l = k + 1; l < trees.size(); l++)
				{
					pair < _int64, _int64 > a = trees[j];
					pair < _int64, _int64 > b = trees[k];
					pair < _int64, _int64 > c = trees[l];
					x1 = (trees[j].first + trees[k].first + trees[l].first);
					y1 = (trees[j].second + trees[k].second + trees[l].second);

					if (0 == x1 % 3 && 0 == y1 % 3)
						r++;
				}
			}
		}

		output << "Case #" << i + 1 << ": " << r << endl;
	}

	input.close();
	output.close();
}

