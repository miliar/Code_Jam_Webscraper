#include "iostream"
#include "fstream"
#include "string"
#include "stack"

using namespace std;

#define small_in "B-small.in"
#define small_out "B-small.out"
#define large_in "B-large.in"
#define large_out "B-large.out"

void Process(int **map, char **c_map, int j, int k, int &xmin, int &ymin, int H, int W)
{
	int x_direction[] = {0, -1, 1, 0};
	int y_direction[] = {-1, 0, 0, 1};
	xmin = k;
	ymin = j;
	for(int l=0; l<4; l++)
	{
		if((j + y_direction[l]) >= H || (j + y_direction[l]) < 0
			|| (k + x_direction[l]) >= W || (k + x_direction[l]) < 0)
			continue;
		else
		{
			if(map[j + y_direction[l]][k + x_direction[l]] < map[ymin][xmin])
			{
				xmin = k + x_direction[l];
				ymin = j + y_direction[l];
			}
		}
	}
}
void main()
{
	int T=0, H=0, W=0;
	// Read input file
	ifstream infile;
	infile.open(large_in);
	infile >> T;
	
	// Output file
	ofstream outfile;
	outfile.open(large_out);
	for(int i=0; i<T; i++)
	{
		if(i == 12)
		{
			int a=0;
			a++;
		}
		infile >> H >> W;
		int **map = new int*[H];
		char **c_map = new char*[H];
		bool **b_map = new bool*[H];
		char c = 'a';
		for(int j=0; j<H; j++)
		{
			map[j] = new int[W];
			c_map[j] = new char[W];
			b_map[j] = new bool[W];
			for(int k=0; k<W; k++)
			{
				infile >> map[j][k];
				c_map[j][k] = 0;
				b_map[j][k] = false;
			}
		}
		c_map[0][0] = c;
		
		for(int j=0; j<H; j++)
		{
			for(int k=0; k<W; k++)
			{
				b_map[j][k] = true;
				int xmin = k;
				int ymin = j;
				Process(map, c_map, j, k, xmin, ymin, H, W);
				b_map[ymin][xmin] = true;
				if(c_map[ymin][xmin] != 0 && c_map[j][k] == 0)
				{
					c_map[j][k] = c_map[ymin][xmin];
				}
				else if(c_map[j][k] != 0 && c_map[ymin][xmin] == 0)
				{
					c_map[ymin][xmin] = c_map[j][k];
					char color = c_map[ymin][xmin];
					int xmin_old = xmin;
					int ymin_old = ymin;
					do
					{
						Process(map, c_map, ymin_old, xmin_old, xmin, ymin, H, W);
						if(b_map[ymin][xmin] == false)
						{
							if(xmin != xmin_old || ymin != ymin_old)
							{
								c_map[ymin][xmin] = color;
							}
							b_map[ymin][xmin] = true;
						}
						else
						{
							break;
						}
						xmin_old = xmin; xmin = -1;
						ymin_old = ymin; ymin = -1;
					} while(ymin != ymin_old || xmin != xmin_old);
				}
				else if(c_map[j][k] == 0 && c_map[ymin][xmin] == 0)
				{
					stack<int> x_stack;
					stack<int> y_stack;
					x_stack.push(k); x_stack.push(xmin);
					y_stack.push(j); y_stack.push(ymin);
					int xmin_old = xmin;
					int ymin_old = ymin;
					char color = 0;
					do
					{
						Process(map, c_map, ymin, xmin, xmin_old, ymin_old, H, W);
						if(ymin == ymin_old && xmin == xmin_old)
						{
							break;
						}
						if(c_map[ymin_old][xmin_old] != 0)
						{
							color = c_map[ymin_old][xmin_old];
							while(!x_stack.empty())
							{
								int x = x_stack.top(); x_stack.pop();
								int y = y_stack.top(); y_stack.pop();
								c_map[y][x] = color;
							}
							break;
						}
						else
						{
							if(b_map[ymin_old][xmin_old] == true)
							{
								break;
							}
							b_map[ymin_old][xmin_old] = true;
							x_stack.push(xmin_old);
							y_stack.push(ymin_old);
							xmin = xmin_old; xmin_old = -1;
							ymin = ymin_old; ymin_old = -1;
						}
						
					} while(ymin != ymin_old || xmin != xmin_old);
					if(!x_stack.empty())
					{
						c++;
						while(!x_stack.empty())
						{
							int x = x_stack.top(); x_stack.pop();
							int y = y_stack.top(); y_stack.pop();
							c_map[y][x] = c;
						}
					}
				}
			}
		}
		outfile << "Case #" << i+1 << ":" << endl;
		for(int j=0; j<H; j++)
		{
			for(int k=0; k<W; k++)
			{
				outfile << c_map[j][k];
				if(k < W-1)
					outfile << " ";
			}
			outfile << endl;
		}
	}
	infile.close();
	outfile.close();
}