#include <iostream>
#include <fstream>
#include <math.h>

#define  max(a,b) (a)>(b)?(a):(b)

using namespace std;

const int SIZE =101;

ifstream fin("bot_large.in");
ofstream fout("bot_large.out");

int cas;
int index =1;

int step = 0;

int b[SIZE] = {0};
int bl =0;
int bp = 1;
int o[SIZE] = {0};
int ol=0;
int op = 1;

void omove(int p)
{
	int move = abs(p-op)+1+o[ol-1];
	o[ol] = max( move, b[bl-1]+1);
	ol ++;
	op = p;
}

void bmove(int p)
{
	int move = abs(p-bp)+1+b[bl-1];
	b[bl] = max(move, o[ol-1]+1);
	bl ++;
	bp = p;
}

void read()
{
	bp = 1;
	op = 1;
	bl = 1; 
	ol = 1;
	b[0] =0;
	o[0] =0;

	fin >> step;
	
	char r;
	int p;

	for (int i =0; i < step; i ++)
	{
		fin >> r >> p;
		
		if (r == 'O')
		{
			omove(p);
		}
		else
		{
			bmove(p);
		}	
	}//end for
	
	int result = max(o[ol-1], b[bl-1]) ;

	fout << "Case #" << index << ": "  << result << endl;
}


int main()
{
	fin >> cas;

	while (index <= cas)
	{
		read();
		index ++;
	}

	return 0;
}