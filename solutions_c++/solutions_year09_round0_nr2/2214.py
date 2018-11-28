#include<iostream>
#include<fstream>


using namespace std;

void copyLetter(char c1,char c2);
bool hasLetter(int i, int j);
void goingDown(int h, int w);
void initMapBasins();

	 int map[101][101];
	 char basins[101][101];
	 int height=0;
	 int width=0;
	 char label='a'; 

void main(){

	ifstream in;
	in.open("B-large.in");
	ofstream out;
	out.open("B-large.out");

	char c[10];
	in.getline(c,10);
	int cases = atoi(c);

	int counter = 0;

	while(counter<cases){
		
		char he[10];
		in.getline(he,10,' ');
		height = atoi(he);

		char wi[10];
		in.getline(wi,10);
		width = atoi(wi);

		initMapBasins();

		for(int i=0; i<height;i++){
			for(int j=0; j<width; j++){
				char temp1[10];

				if(j!=width-1)
					in.getline(temp1,10,' ');
			
				else
					in.getline(temp1,10);

				map[i][j]=atoi(temp1);
			}
		}
		
		for(int i=0; i<height;i++){
			for(int j=0; j<width; j++){
				goingDown(i,j);
			}
		}

		counter++;

		out<<"Case #"<<counter<<": "<<endl;

		for(int i=0; i<height;i++){
			for(int j=0; j<width; j++){

				if(i==height-1&&j==width-1)
					out<<basins[i][j];
				else
					out<<basins[i][j]<<" ";
			}
			
			out<<endl;
		}


		label='a'; 
	}

	

}

void initMapBasins(){

	for(int x=0; x<101; x++)
		for(int y=0; y<101; y++)
			map[x][y] = basins[x][y] = 0;
}

void copyLetter(char c1,char c2)
{
	
	for(int i=0; i<height;i++)
	{
	
		for(int j=0; j<width; j++)
		{
		
			if(basins[i][j]==c2)
			basins[i][j]=c1;
			
		}
	}
	
}

bool hasLetter(int i, int j){
	
	if(basins[i][j]==0)
		return false;
	
	return true;
}

void goingDown(int h, int w)
{
	if(!hasLetter(h,w))
	{
		int minh=h; int minw=w;

		basins[h][w]=label;

		if(h-1>=0&&map[h-1][w]<map[minh][minw]){ //north
			minh=h-1;
			minw=w;
		}

		if(w-1>=0&&map[h][w-1]<map[minh][minw]){ //west
			minh=h;
			minw=w-1;
		}

		if(w+1<width&&map[h][w+1]<map[minh][minw]){ //east
			minh=h;
			minw=w+1;
		}
		if(h+1<height&&map[h+1][w]<map[minh][minw]){ //south
			minh=h+1;
			minw=w;	
		}
		
		if(minh!=h||minw!=w){

			if(hasLetter(minh,minw))
				copyLetter(basins[minh][minw],label);
		
			goingDown(minh,minw);
		}

		else
		label++;
	}	
}