#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cassert>
using namespace std;

vector<string> dics;
vector<string> patterns;
typedef vector<string>::const_iterator STR_ITER;
string filename_in("B-large.in");
string filename_out=(filename_in+".out");
ofstream outfile(filename_out.c_str()); 
ifstream infile(filename_in.c_str());


int testcase;
int H=100;
int W=100;
int map[100][100];
char basins[100][100];
char region;


int solve()
{
	int rst=0;
	return rst;
}
//5
//3 3
//9 6 3
//5 9 6
//3 5 9
//1 10
//0 1 2 3 4 5 6 7 8 7
//2 3
//7 6 7
//7 6 7
//5 5
//1 2 3 4 5
//2 9 3 9 6
//3 3 0 8 7
//4 9 8 9 8
//5 6 7 8 9
//2 13
//8 8 8 8 8 8 8 8 8 8 8 8 8
//8 8 8 8 8 8 8 8 8 8 8 8 8
void init()
{
	region='a';
	for(int i=0; i<H; i++)
		for(int j=0; j<W; j++)
			map[i][j]=0;
	for(int i=0; i<H; i++)
		for(int j=0; j<W; j++)
			basins[i][j]='\0';
}

//3 3
//9 6 3
//5 9 6
//3 5 9

char check4Directions(int h, int w)
{
	int hi=-1, wi=-1;
	int lowest= map[h][w], north, west, east, south;
	
	if(h>0){
		if (lowest> map[h-1][w]){
			hi=h-1; wi=w;
			lowest = map[hi][wi];
		}	
	}
	if(w>0){		
		if (lowest> map[h][w-1]){
			hi=h; wi=w-1;
			lowest = map[hi][wi];
		}		
	}
	if(w+1<W){
		if (lowest>map[h][w+1]){
			hi=h; wi=w+1;
			lowest = map[hi][wi];
		}
	}
	if (h+1 <H){
		if (lowest>map[h+1][w]){
			hi=h+1; wi=w;
			lowest = map[hi][wi];
		}
	}

	if(hi<0){
		basins[h][w] = region++;
	}else if(basins[hi][wi] != '\0'){
		basins[h][w]=basins[hi][wi];		
	}else{
		basins[h][w]=check4Directions(hi, wi);
	}
	return basins[h][w];
}
int main()
{
	assert(outfile && infile);
	infile >> testcase;	

	STR_ITER itr;
	for(int i=1; i<=testcase; i++)
	{
		init();
		outfile<<"Case #"<<i<<":\n";
		infile>>H; infile>>W;
		for(int h=0; h<H; h++)
			for(int w=0; w<W; w++)
				infile>>map[h][w];

		//this list: North, West, East, South.
		for(int h=0; h<H; h++){
			for(int w=0; w<W; w++){
				if(basins[h][w] != '\0') 
					continue;
				check4Directions(h, w);
			}
		}
			
		for(int h=0; h<H; h++){
			for(int w=0; w<W; w++)
				outfile<<basins[h][w]<<" ";
			outfile<<"\n";
		}

	}
	return 0;
}