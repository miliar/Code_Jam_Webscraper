#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct Double
{
	int x, y;
};

class Map
{
public:
	int height, width;
	int db_num;
	int **data;
	int ** result;

	Map()
	{
		height = 0;
		width = 0;
		result = 0;
		db_num = 0;
	}

	void set(int h, int w, int **d)
	{
		height = h;
		width = w;
		data = d;
		result = new int*[h];
		for(int i = 0; i < h; i++)
		{
			result[i] = new int[w];
			for(int j = 0; j < w; j++)
			{
				result[i][j] = -1;
			}
		}
	}

	void analyze()
	{
		for(int i = 0; i < height; i++)
		{
			for(int j = 0; j < width; j++)
			{
				AnalyzeArea(i,j);
			}
		}
	}

	~Map()
	{
		if(result != 0)
		{
			for(int i = 0; i < height; i++)
			{
				delete[] result[i];
			}
			delete[] result;
		}
	}
private:
	Double getLowest(int h, int w)
	{
		Double t;
		t.x = -1;
		t.y = -1;
		int North = 100000;
		int West = 100000;
		int East = 100000;
		int South = 100000;
		int Lowest = data[h][w];

		if(h>0) North = data[h-1][w];
		if(w>0) West = data[h][w-1];
		if(w<width -1) East = data[h][w+1];
		if(h<height -1) South = data[h+1][w];

		if(North < Lowest)
		{
			Lowest = North;
			t.x = h-1;
			t.y = w;
		}

		if(West < Lowest)
		{
			Lowest = West;
			t.x = h;
			t.y = w - 1;
		}

		if(East < Lowest)
		{
			Lowest = East;
			t.x = h;
			t.y = w + 1;
		}

		if(South < Lowest)
		{
			Lowest = South;
			t.x = h + 1;
			t.y = w;
		}

		return t;
	}

	int AnalyzeArea(int h, int w)
	{
		Double t;
		if(result[h][w] == -1)
		{
			t = getLowest(h, w);
			if(t.x == -1 || t.y == -1)
			{
				result[h][w] = db_num++;
				return result[h][w];
			}else
			{
				result[h][w] = AnalyzeArea(t.x, t.y);
			}
		}

		return result[h][w];
	}
};

int T;
Map *maps;
int ***data;
int *height;
int *width;

const char num2char[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

char *infilepath = "C:\\Users\\cyzhao\\Desktop\\code jam\\Watersheds\\test.in";
char *outfilepath = "C:\\Users\\cyzhao\\Desktop\\code jam\\Watersheds\\out.txt";

void readfile();
void writefile();
void init();

void main()
{
	readfile();
	init();
	writefile();
	for(int i = 0; i < T; i++)
	{
		for(int j = 0; j < height[i]; j++)
		{
			delete[] data[i][j];
		}
		delete[] data[i];
	}
	delete[] data;
	delete[] height;
	delete[] width;
	delete[] maps;
}

void readfile()
{
	ifstream infile(infilepath);
	if(!infile)
	{
		cerr<<"File could not be open"<<endl;
		abort();
	}
	infile>>T;
	data = new int**[T];
	height = new int[T];
	width = new int[T];

	int h, w;
	for(int i = 0; i < T; i++)
	{
		infile>>height[i]>>width[i];
		h = height[i];
		w = width[i];
		data[i] = new int*[h];
		for(int j = 0; j < h; j++)
		{
			data[i][j] = new int[w];
			for(int k = 0; k < w; k++)
			{
				infile>>data[i][j][k];
			}
		}
	}
	infile.close();
}

void writefile()
{
	ofstream outfile;
	outfile.open(outfilepath, ios::out);
	if(!outfile)
	{
		cerr<<"File could not be open"<<'\n';
		abort();
	}
	for(int i = 0; i < T; i++)
	{
		outfile<<"Case #"<<i + 1<<":"<<'\n';
		for(int j = 0; j < maps[i].height; j++)
		{
			for(int k = 0; k < maps[i].width - 1; k++)
			{
				outfile<<num2char[maps[i].result[j][k]]<<' ';
			}
			outfile<<num2char[maps[i].result[j][k]]<<'\n';
		}
	}
	outfile.close();
}

void init()
{
	maps = new Map[T];
	for(int i = 0; i < T; i++)
	{
		maps[i].set(height[i], width[i], data[i]);
		maps[i].analyze();
	}
}