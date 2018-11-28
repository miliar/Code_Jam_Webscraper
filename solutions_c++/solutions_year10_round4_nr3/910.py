#include <iostream>
#include <vector>
#include <cmath>

typedef long long int lli;

void make_grid(std::vector<std::vector<bool> >& grid)
{
	grid.clear();
	for (lli i = 0; i <= 100; i++) {
		std::vector<bool> row;
		for (lli j = 0; j <= 100; j++) {
			row.push_back(false);
		}
		grid.push_back(row);
	}
}

lli do_step(std::vector<std::vector<bool> >& grid)
{
	std::vector<std::vector<bool> > grid_new;
	make_grid(grid_new);
	for (lli i = 0; i <= 100; i++) {
		for (lli j = 0; j <= 100; j++) {
			bool neighbour = false, both = true;
			if ((i > 0) && (grid[i-1][j])) neighbour = true; else both = false;
			if ((j > 0) && (grid[i][j-1])) neighbour = true; else both = false;
			grid_new[i][j] = false;
			if (both) grid_new[i][j] = true;
			if (grid[i][j] && neighbour) grid_new[i][j] = true;
		}
	}
	lli count = 0;
	for (lli i = 0; i <= 100; i++) {
		for (lli j = 0; j <= 100; j++) {
			grid[i][j] = grid_new[i][j];
			if (grid[i][j]) count++;
		}
	}
	return count;
}

lli solve(lli r, std::vector<lli>& x1, std::vector<lli>& y1, std::vector<lli>& x2, std::vector<lli>& y2)
{
	std::vector<std::vector<bool> > grid;
	make_grid(grid);
	lli count = 0;
	for (lli i = 0; i < r; i++) {
		for (lli j = x1[i]; j <= x2[i]; j++) {
			for (lli k = y1[i]; k <=y2[i]; k++) {
				grid[j][k] = true;
				count++;
			}
		}
	}
	lli steps = 0;
	while(count != 0) {
		count = do_step(grid);
		steps++;
	}
	return steps;
}

int main()
{
	lli c;
	std::cin >> c;
	for (lli i = 1; i <= c; i++) {
		lli r;
		std::cin >> r;
		std::vector<lli> x1, y1, x2, y2;
		for (lli j = 0; j < r; j++) {
			lli x1_, y1_, x2_, y2_;
			std::cin >> x1_ >> y1_ >> x2_ >> y2_;
			x1.push_back(x1_);
			y1.push_back(y1_);
			x2.push_back(x2_);
			y2.push_back(y2_);

		}
		std::cout << "Case #" << i << ": " << solve(r, x1, y1, x2, y2) << std::endl;
	}
	return 0;
}
	
