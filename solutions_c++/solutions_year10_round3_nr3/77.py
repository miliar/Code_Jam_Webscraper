#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <sstream>
#include <iomanip>

using namespace std;

struct cell_info
{
	short color;
	short max;
};

vector<cell_info> cells;
int M, N;

cell_info &cell(int row, int col) { return cells[row * N + col]; }

int largestFromTopLeft(int row, int col)
{
	short tl_color = cell(row, col).color;
	if(tl_color > 1)
		return 0;
	int radius = 1;
	for(; row + radius < M && col + radius < N; ++radius)
	{
		short req_color = tl_color;
		for(int ri = row + radius; ri >= row; --ri, (req_color = req_color ^ 1))
			if(cell(ri, col + radius).color != req_color)
				return radius;
		req_color = tl_color;
		for(int ci = col + radius; ci >= col; --ci, (req_color = req_color ^ 1))
			if(cell(row + radius, ci).color != req_color)
				return radius;
	}
	return radius;
}

void invalidateArea(int row, int col, int radius)
{
	for(int ir = row; ir < row + radius; ++ir)
		for(int ic = col; ic < col + radius; ++ic)
			cell(ir, ic).color |= 2;
}

int main(int argc, char *argv[])
{
	int cases;
	cin >> cases;
	vector<pair<int, int> > biggests;

	for(int ci = 0; ci < cases; ++ci)
	{
		cin >> M >> N;
		string line;
		cells.resize(M * N);
		for(int im = 0; im < M; ++im)
		{
			cin >> line;
			for(int in = 0; in < N/4; ++in)
			{
				// meh, ugly
				string hexchar("0x");
				hexchar += line[in];
				istringstream str(hexchar);
				int val;
				str >> setbase(0) >> val;
				cell(im, in * 4 + 0).color = (val >> 3) & 1;
				cell(im, in * 4 + 1).color = (val >> 2) & 1;
				cell(im, in * 4 + 2).color = (val >> 1) & 1;
				cell(im, in * 4 + 3).color = (val >> 0) & 1;
			}
		}


		vector<pair<int, int> > results;

		int biggest_radius = 0;
		int cells_left = M * N;
		while(cells_left)
		{
			biggest_radius = 0;
			for(int im = 0; im < M; ++im)
			{
				for(int in = 0; in < N; ++in)
				{
					int radius = largestFromTopLeft(im, in);
					cell(im, in).max = radius;
					if(radius > biggest_radius)
					{
						biggest_radius = radius;
						biggests.clear();
					}
					if(radius == biggest_radius)
						biggests.push_back(make_pair(im, in));
				}
			}

			int biggest_count = biggests.size();
			int nonoverlapping_biggests = 0;
			for(int ib = 0; ib < biggest_count; ++ib)
			{
				int currow = biggests[ib].first, curcol = biggests[ib].second;
				if(currow == -1)
					continue;
				for(int ib2 = ib + 1; ib2 < biggest_count; ++ib2)
				{
					if(biggests[ib2].first >= currow + biggest_radius
							|| biggests[ib2].first == currow + biggest_radius - 1
									&& biggests[ib2].second >= curcol + biggest_radius)
						break;
					// invalidate overlap
					if(biggests[ib2].second < curcol + biggest_radius
							&& biggests[ib2].second + biggest_radius > curcol)
					{
						biggests[ib2].first = -1;
					}
				}
				++nonoverlapping_biggests;
				invalidateArea(currow, curcol, biggest_radius);
				cells_left -= biggest_radius * biggest_radius;
			}
			results.push_back(make_pair(biggest_radius, nonoverlapping_biggests));
		}

		cout << "Case #" << (ci + 1) << ": " << results.size() << endl;
		for(int i = 0; i < results.size(); ++i)
			cout << results[i].first << " " << results[i].second << endl;
	}

	return 0;
}
