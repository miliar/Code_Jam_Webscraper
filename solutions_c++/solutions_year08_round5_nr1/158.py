#include <fstream>
#include <iostream>
#include <vector>
#define _max 6010
#define _b 3005
using namespace std;


int l_map[_max][_max];
int b_map[_max][_max];
bool pocket[_max][_max];

void init()
{
	memset(l_map, 0, sizeof(l_map));
	memset(b_map, 0, sizeof(b_map));
	memset(pocket, 0, sizeof(pocket));
}

void draw_map(string S, int &pos_x, int &pos_y, int &d)
{
	for(int i = 0; i < S.length(); i++)
	{
		if(S[i] == 'F')
		{
			if(d == 0) 
			{ // north
				l_map[pos_x + _b][pos_y + _b] = 1;
				pos_y++;
			}
			else if(d == 1)
			{ 
				pos_x++;
				b_map[pos_x + _b][pos_y + _b] = 1;
			}
			else if(d == 2)
			{
				pos_y--;
				l_map[pos_x + _b][pos_y + _b] = 1;
			}
			else
			{
				b_map[pos_x + _b][pos_y + _b] = 1;
				pos_x--;
			}
		}
		else if(S[i] == 'R')
		{
			d = (d + 1) % 4;
		}
		else 
		{
			d = (d + 3) % 4;
		}
	}
}

long long get_area()
{
	long long A = 0;
	int wall_count;
	int re_wall_count;
	for(int x = 0; x < _max; x++)
	{
		wall_count = 0;
		for(int y = 0; y <_max; y++)
		{
			if(b_map[x][y] == 1)
			{
				wall_count++;
			}
		}
		
		re_wall_count = 0;
		for(int y = 0; y <_max; y++)
		{
			if(b_map[x][y] == 1)
			{
				re_wall_count++;
			}
			if(re_wall_count > 0 && re_wall_count < wall_count && re_wall_count % 2 == 0)
			{
				pocket[x][y] = 1;
			}
		}
	}
	
	for(int y = 0; y < _max; y++)
	{
		wall_count = 0;
		for(int x = 0; x < _max; x++)
		{
			if(l_map[x][y] == 1)
			{
				wall_count++;
			}			
		}
		re_wall_count = 0;
		for(int x = 0; x < _max; x++)
		{
			if(re_wall_count > 0 && re_wall_count < wall_count && re_wall_count % 2 == 0)
			{
				pocket[x][y] = 1;
			}
			
			if(l_map[x][y] == 1)
			{
				re_wall_count++;
			}
		}
	}
	
	for(int x = 0; x < _max; x++)
	{
		for(int y = 0; y < _max; y++)
		{
			if(pocket[x][y] == 1)
			{
				A++;
			}
		}
	}
	return A;
}

int main()
{
	ifstream fin("problemA.in");
	ofstream fout("problemA.out");
	
	int test_case;
	int num_test_cases;	
	string S;
	int T, L;
	int pos_x, pos_y, d;
	long long solution;
	
	fin >> num_test_cases;
	for(test_case = 1; test_case <= num_test_cases; test_case++)
	{	
		init();
		pos_x = 0;
		pos_y = 0;
		d = 0;
		fin >> L;
		for(int i = 0; i < L; i++)
		{
			fin >> S >> T;
			for(int j = 0; j < T; j++)
			{
				draw_map(S, pos_x, pos_y, d);
			}
		}
		solution = get_area();
		fout << "Case #" << test_case << ": " << solution << endl;

	}	
	fin.close();
	fout.close();
	return 0;
}