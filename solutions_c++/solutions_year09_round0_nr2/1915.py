
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string inp_file = "B-large.in";
string out_file = "B-large.out";

void set_equivalence(int h, int w, int H, int W, int** data, char** eq, char & c)
{
	if(eq[h][w] == 'Z')
	{

				int min=data[h][w];
		int new_i;
		bool changed= false;
		 // n:1 , w:2 , e:3, s:4

		if(h != 1)
		{
			if(min > data[h-1][w])
			{
				min = data[h-1][w];
				new_i=1;
				changed = true;
			}
		}

		if(w != 1)
		{
			if(min > data[h][w-1])
			{
				min = data[h][w-1];
				new_i=2;
				changed = true;						
			}
		}

		if(w != W)
		{
			if( min> data[h][w+1])
			{
				min = data[h][w+1];
				new_i=3;
				changed = true;						
			}
		}

		if(h != H)
		{
			if(min> data[h+1][w])
			{
				min = data[h+1][w];
				new_i = 4;
				changed = true;
			}
		}


		if(changed)
		{
			int new_h,new_w;
			if(new_i == 1)
			{
				new_h = h-1;
				new_w = w;
			}
			else if(new_i == 2)
			{
				new_h = h;
				new_w = w-1;
			}
			else if(new_i == 3)
			{
				new_h = h;
				new_w = w+1;
			}	
			else if(new_i == 4)
			{
				new_h = h+1;
				new_w = w;
			}
			set_equivalence(new_h,new_w,H,W,data,eq,c);
			eq[h][w] = eq[new_h][new_w];
		}
		else
		{
			eq[h][w] = c;
			c++;
		}
	}


}

int main()
{
	ifstream input(inp_file.c_str());
	ofstream output(out_file.c_str());

	int num_of_maps;
	// nxm;
	
	int H, W;
	input>>num_of_maps;

	
	for(int map = 1; map <= num_of_maps; map++)
	{
		input>>H>>W;
		char** equivalence_classes = new char*[H+1];
		int** data = new int*[H+1];
		for(int i= 1; i<=H; i++)
		{
			equivalence_classes[i] = new char[W+1];
			data[i] = new int[W+1];

			for(int j=1; j<= W; j++)
			{
				equivalence_classes[i][j] = 'Z';
				input>>data[i][j];
			}	
		}

		output<<"Case #"<<map<<":"<<endl;
		char c = 'a';
	
		for(int d1 = 1; d1 <= H; d1++)
		{
			for(int d2 = 1; d2<= W; d2++)
			{
				set_equivalence(d1,d2,H,W,data,equivalence_classes,c);
			}
		}
		for(int d3 = 1; d3<= H; d3++)
		{
			for(int d4 = 1; d4< W; d4++)
			{
				output<<equivalence_classes[d3][d4]<<" ";
			}
			output<<equivalence_classes[d3][W]<<endl;
		}
	}


	


	input.close();
	output.close();
	return 0;
}