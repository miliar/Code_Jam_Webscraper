#include<vector>
#include <iostream>
#include <fstream>
#include <string>

void solve(int H, int W, std::vector<std::vector<int> >& height, std::vector<std::vector<char> >& res, int t)
{
	std::vector<int> alias(H * W);
	std::vector<char> letter(H * W);

	std::vector<std::vector<int> > paths(H);
	for (int h = 0; h < H; ++h)
		paths[h] = std::vector<int>(W);
	for (int h = 0; h < H; ++h)
	{
		for (int w = 0; w < W; ++w)
		{
			if (alias[h * W + w] == 0)
			  alias[h * W + w] = 1 + h * W + w;
			int i = h;
			int j = w;
			while (paths[i][j] == 0)
			{
				paths[i][j] = 1 + h * W + w;
				if (height[i][j + 1] < height[i + 1][j + 1]
				    && height[i][j + 1] <= height[i + 2][j + 1]
				    && height[i][j + 1] <= height[i + 1][j]
				    && height[i][j + 1] <= height[i + 1][j + 2])
				{				
					i--;
				}
				else if (height[i + 1][j] < height[i + 1][j + 1]
				    && height[i + 1][j] <= height[i + 2][j + 1]
				    && height[i + 1][j] <= height[i][j + 1]
				    && height[i + 1][j] <= height[i + 1][j + 2])
				{			
					j--;				
				}
				else if (height[i + 1][j + 2] < height[i + 1][j + 1]
				    && height[i + 1][j + 2] <= height[i + 2][j + 1]
				    && height[i + 1][j + 2] <= height[i + 1][j]
				    && height[i + 1][j + 2] <= height[i][j + 1])				
				{
					j++;				
				}

				else if (height[i + 2][j + 1] < height[i + 1][j + 1]
				    && height[i + 2][j + 1] <= height[i][j + 1]
				    && height[i + 2][j + 1] <= height[i + 1][j]
				    && height[i + 2][j + 1] <= height[i + 1][j + 2])
				{
					i++;			
				}
			}
			if (paths[i][j] != 1 + h * W + w)
			{
				alias[h * W + w] = paths[i][j];
			}
			
		}
	}

	std::cout << "Case #" << t + 1 << ":" << std::endl;
	char currLetter = 'a';
	for (int h = 0; h < H; ++h)
	{
		for (int w = 0; w < W; ++w)
		{
			if (w != 0)
			 std::cout << " ";
			int unalias = h * W + w;
			while (alias[unalias] != unalias + 1)
				unalias = alias[unalias] - 1; 
			if  (letter[unalias] == '\0')
			{
				letter[unalias] = currLetter;
				currLetter++;
			}
			res[h][w] = letter[unalias];
			std::cout << res[h][w];
		}
		std::cout << std::endl;
	}
}

int  main(int argc, char** argv)
{
	  std::ifstream f(argv[1]);
	  if (!f.is_open())
	    return -1;
	 int T;
	 f >> T;

	 for (int t = 0; t < T; ++t)
	 {
		int H, W;
		int value;
		int max;
		f >> H >> W;
		std::vector<std::vector<int> > height(H + 2);
		for (int h = 0; h < H; ++h)
   		{
			height[h + 1] = std::vector<int>(W + 2);
			for (int w = 0; w < W; ++w)
			{
			 	f >> value;
				max = std::max(max, value);
				height[h + 1][w + 1] = value; 
			}
		}
		height[0] = std::vector<int>(W + 2);
		height[H + 1] = std::vector<int>(W + 2);
		for (int h = 0; h < H; ++h)
		{
                	height[h + 1][0] = max;
			height[h + 1][W + 1] = max;
		}
				
		for (int w = 0; w < W; ++w)
		{
			height[0][w + 1] = max;
			height[H + 1][w + 1] = max;
		}

		std::vector<std::vector<char> > res (H);
		for (int h = 0; h < H; ++h)
			res[h] = std::vector<char>(W);
		solve(H, W, height, res, t);
	 }
}
