/*
 * fmain.cpp
 *
 *  Created on: 2009-9-3
 *      Author: sunguoyang07
 *  	Email:matrixworker@gmail.com
 *  This is the solution for watersheds,code jam 2009
 */
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct CProblem
{
public:
	int** matrix;
	int** basin;
	int height,width;
	int letter;
public:
	CProblem()
	{
		matrix = NULL;
		basin = NULL;
		letter = int('a');
	}

	~CProblem()
	{
		clear();
	}

	void set_cell(int i, int j, int data)
	{
		this->matrix[i][j]=data;
	}

	void clear()
	{
		if (matrix)
		{
			for (int i = 0; i < height; i++)
			{
				delete[] matrix[i];
			}
			delete[] matrix;
		}
		if (basin)
		{
			for (int i = 0; i < height; i++)
			{
				delete[] basin[i];
			}
			delete[] basin;
		}
	}

	void allocate(int height, int width)
	{
		clear();
		this->height = height;
		this->width = width;
		matrix = new int*[height];
		basin = new int*[height];
		assert(matrix && basin);
		for (int i = 0; i < height; i++)
		{
			matrix[i] = new int[width];
			basin[i] = new int[width];
			assert(matrix[i] && basin[i]);
		}
		for (int i = 0; i < height; i++)
			for (int j = 0; j < width; j++)
				basin[i][j] = -1;
		letter = int('a');
	}

	int get_basin(int i, int j)
	{
		int& basin_this = basin[i][j];
		if(basin_this != -1)
			return basin_this;
		if(is_sink(i,j))
		{
			basin_this = letter++;
			return basin_this;
		}
		else
		{
			int dx,dy;
			int lowest_x=i,lowest_y=j;
			for(dx=-1;dx<=1;dx++)
				for(dy=-1;dy<=1;dy++)
				{
					if(dx*dy==0 && dx!=dy)
					{
						int x1= i+dx;
						int y1= j+dy;
						if(x1>=0 && x1<height && y1>=0 && y1<width)//>=ÎóÐ´Îª>
							if(matrix[x1][y1] < matrix[lowest_x][lowest_y])//'<' ÎóÐ´Îª '>'
							{
								lowest_x = x1;
								lowest_y = y1;
							}
					}
				}

			basin_this = get_basin(lowest_x, lowest_y);
		}
		return basin_this;
	}

	bool is_sink(int i,int j)
	{
		int dx,dy;
		for(dx=-1;dx<=1;dx++)
			for(dy=-1;dy<=1;dy++)
			{
				if(dx*dy==0 && dx!=dy)
				{
					int x1 = i+dx;
					int y1 = j+dy;
					if(x1>=0 && x1<height && y1>=0 && y1<width)
						if(matrix[x1][y1]<matrix[i][j])
							return false;
				}
			}
		return true;
	}

	void solve()
	{
		int i, j;
		for (i = 0; i < height; i++)
			for (j = 0; j < width; j++)
				get_basin(i, j);
	}

	void output(ofstream& fout)
	{
		int i,j;
		for (i = 0; i < height; i++)
		{
			for (j = 0; j < width; j++)
				fout << (char) basin[i][j] << " ";
			fout << endl;
		}
	}
};

int main()
{
	int T, no, i, j, data;
	int row,col;
	CProblem p;

	ifstream fin("input.txt");
	assert(fin);
	ofstream fout("output.txt");
	assert(fout);

	fin>>T;
	for(no=1; no<=T; no++)
	{
		fin >> row >> col;
		p.allocate(row, col);
		for(i=0;i<row;i++)
			for(j=0;j<col;j++)
			{
				fin>>data;
				p.set_cell(i,j,data);
			}
		fout<<"Case #"<<no<<":"<<endl;
		p.solve();
		p.output(fout);
	}
	fin.close();
	fout.close();
	return 0;
}
