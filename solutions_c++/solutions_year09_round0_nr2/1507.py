
#include <fstream>
#include <iostream>
#include <string>
using namespace std;

bool isSink(int Map[100][100], int i, int j, int H, int W)
{
	bool este=true;
	
	if(i-1 >=0 && Map[i-1][j] < Map[i][j]) este = false;
	if(j-1 >=0 && Map[i][j-1] < Map[i][j]) este = false;
	if(i+1 < H && Map[i+1][j] < Map[i][j]) este = false;
	if(j+1 < W && Map[i][j+1] < Map[i][j]) este = false;
	
	return este;
}
void findSinks(int Map[100][100], int Code[100][100], int H, int W, int &sinks, int X[], int Y[])
{
	for(int i=0;i<H;i++)
	{
		for(int j=0;j<W;j++)
		{
			if(isSink(Map, i, j, H, W))
			{
				X[sinks] = i;
				Y[sinks] = j;
				Code[i][j] = sinks++;
			}
		}
	}
}
void clearA(int Code[100][100], int H, int W)
{
	for(int i=0;i<H;i++)
	{
		for(int j=0;j<W;j++)
		{
			Code[i][j] = -1;
		}
	}
}
void drainFromHere(int Map[100][100], int Drain[100][100], int H, int W)
{
	for(int i=0;i<H;i++)
	{
		for(int j=0;j<W;j++)
		{
			int min = 10001;
			int x,y;
			
			if(i-1 >=0 && Map[i-1][j] < Map[i][j] && min > Map[i-1][j])
			{ 
				min = Map[i-1][j];
				x = i-1;
				y = j;
			}
			if(j-1 >=0 && Map[i][j-1] < Map[i][j] && min > Map[i][j-1])
			{ 
				min = Map[i][j-1];
				x = i;
				y = j-1;
			}
			if(j+1 < W && Map[i][j+1] < Map[i][j] && min > Map[i][j+1])
			{ 
				min = Map[i][j+1];
				x = i;
				y = j+1;
			}
			if(i+1 < H && Map[i+1][j] < Map[i][j] && min > Map[i+1][j])
			{ 
				min = Map[i+1][j];
				x = i+1;
				y = j;
			}
			
			
			if(min != 10001)
			{
				if(x == i-1 && y == j) Drain[i][j] = 0; 
				if(x == i && y == j-1) Drain[i][j] = 1;
				if(x == i+1 && y == j) Drain[i][j] = 2;
				if(x == i && y == j+1) Drain[i][j] = 3;
			}
			
		}
	}	
	
	

}
void markBasin(int Drain[100][100], int Code[100][100], int H, int W, int x, int y, int val)
{
	Code[x][y] = val;
	int i=x, j=y;
	
	if(i-1 >=0 && Drain[i-1][j] == 2)
	{ 
		markBasin(Drain, Code, H, W, x-1, y, val); 
	}
	if(j-1 >=0 && Drain[i][j-1] == 3)
	{ 
		markBasin(Drain, Code, H, W, x, y-1, val); 
	}
	if(i+1 < H && Drain[i+1][j] == 0)
	{ 
		markBasin(Drain, Code, H, W, x+1, y, val); 
	}
	if(j+1 < W && Drain[i][j+1] == 1)
	{ 
		markBasin(Drain, Code, H, W, x, y+1, val); 
	}
}
int main () {

	fstream fin, fout;
	int T, H, W;
	
	fin.open ("input.in", fstream::in );
	fout.open ("output.out", fstream::out);

	fin >> T; 
  
	//rezolvare
	int Map[100][100];
	int Code[100][100];
	int Drain[100][100];
	int X[26], Y[26];
	
	
	char alfabet[26] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

	
	for(int k=0;k<T;k++)
	{
		fin >> H >> W;
		clearA(Code, H, W);
		clearA(Drain, H, W);
		
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)
			{
				fin >> Map[i][j];
			}
		}
		int sinks = 0;//numarul de sinks
		findSinks(Map, Code, H, W, sinks, X, Y);
		
		drainFromHere(Map, Drain, H, W);
		
		for(int i=0;i<sinks;i++)
		{
			markBasin(Drain, Code, H, W, X[i], Y[i], i);
		}
				
		fout << "Case #"<< k+1 <<":"<<endl;
		int temp = 0;
		char codificare[26] = {'0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'};
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)
			{
				if(codificare[Code[i][j]] == '0')
				{
					codificare[Code[i][j]] = alfabet[temp++];
				}
			}
		}
		
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)
			{
				fout << codificare[Code[i][j]] <<" ";
			}
			fout << endl;
		}
	}
	
	//end rezolvare
		
	fin.close();
	fout.close();
	cout << "Gata!!!";
	return 0;
}
