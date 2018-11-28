#include <iostream>
#include <cstdlib>
#include <vector>
#include <set>
#include <fstream>
using namespace std;

int nMap;
int Map[100][100];
char Module[100][100];
set<int> isDone;
int H, W;

struct Location
{
	int row, col;
	Location(){}
	Location(int i, int j): row(i), col(j){}
};

bool FindNext(int row, int col, int self, Location & locat)
{
	int min = INT_MAX;
	int i, j;
	if(row != 0)
	{
		min = Map[row-1][col];
		i = row - 1;
		j = col;
	}
	if(col != 0)
	{
		if(min > Map[row][col-1])
		{
			min = Map[row][col-1];
			i = row;
			j = col - 1;
		}	
	}
	if(col != W-1)
	{
		if(min > Map[row][col+1])
		{
			min = Map[row][col+1];
			i = row;
			j = col + 1;
		}
	}
	if(row != H-1)
	{
		if(min > Map[row+1][col])
		{
			min = Map[row+1][col];
			i = row + 1;
			j = col;
		}
	}
	if(self > min)
	{
		locat.row = i;
	    locat.col = j;
	    return true;
	}
	return false;	
}

int main()
{
	ifstream in_file;
	ofstream out_file;
	char current;
	Location locat;
	in_file.open("B-large.in");
	out_file.open("blout.txt");
	if(!in_file || !out_file)
	{
		cerr << "cannot open the file!" << endl;
		exit(1);
	}
	in_file >> nMap;
	for(int i = 0; i < nMap; i++)
	{
		isDone.clear();
		current = 'a';
		in_file >> H >> W;
		for(int row = 0; row < H; row++)
		{
			for(int col = 0; col < W; col++)
			{
				in_file >> Map[row][col];
			}
		}
		

	    for(int row = 0; row < H; row++)
	    {
			for(int col = 0; col < W; col++)
			{
				int si = row, sj = col;
			   	bool find = false;
			   	vector<Location> locatVec;
			   	
                if(isDone.count(row * W + col)) continue;
				while(FindNext(si, sj, Map[si][sj], locat))
				{
					if(isDone.count(locat.row * W + locat.col))
					{
						find = true;
						break;
					}
					locatVec.push_back(Location(si, sj));
					si = locat.row;
					sj = locat.col;
				}
				locatVec.push_back(Location(si, sj));
				if(find)
				{
					for(int s = 0; s < locatVec.size(); s++)
				    {
						Module[locatVec[s].row][locatVec[s].col] = Module[locat.row][locat.col];
						isDone.insert(locatVec[s].row * W + locatVec[s].col);
				    }
				}
				else if(locatVec.size() != 0)
				{
					for(int s = 0; s < locatVec.size(); s++)
				    {
						Module[locatVec[s].row][locatVec[s].col] = current;
						isDone.insert(locatVec[s].row * W + locatVec[s].col);
				    }
				    current ++;
				}
				else
				{
					Module[row][col] = current;
					isDone.insert(row * W + col);
					current++;
				}	
	
			}
		}
		out_file << "Case #" << i+1 << ": " << endl;
		for(int row = 0; row < H; row++)
		{
			for(int col = 0; col < W; col++)
			{
				out_file << Module[row][col] << " ";
			}
			out_file << endl;
		}
	}
	
	
	in_file.close();
	out_file.close();
	system("pause");
	return 0;
}
