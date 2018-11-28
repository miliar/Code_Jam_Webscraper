#include <iostream>
#include <stdio.h>

using namespace std;


typedef struct point
{
	int w;
	int h;
}point;

typedef enum direction 
{
	None,
	Top,
	Right,
	Bottom,
	Left
} dir;

int **map;
char **sinks;
char **touched;
point **basin;
char **labels;
int T,W,H=0;

void spawn(int h,int w);
bool wouldPointGoToPoint(int h1,int w1,int h2,int w2);

int main (int argc, char * const argv[]) 
{
    // insert code here...
	FILE *input = fopen("/Users/dgk/xcode/projects/WaterBasins/B-large.in","r");
	//FILE *input = fopen("/Users/dgk/xcode/projects/WaterBasins/input.in","r");
	if(input)
	{
		T,W,H=0;
		fscanf(input,"%d",&T);
		//cout<<"T:"<<T<<" ";
		for(int a=0;a<T;a++)
		{
			fscanf(input,"%d",&H);
			fscanf(input,"%d",&W);
			//cout<<"H:"<<H<<" W:"<<W<<endl;
			map = new int*[H];
			sinks = new char*[H];
			touched = new char*[H];
			basin = new point*[H];
			labels = new char*[H];
			for(int b=0;b<H;b++)
			{
				map[b] = new int[W];
				sinks[b] = new char[W];
				touched[b] = new char[W];
				basin[b] = new point[W];
				labels[b] = new char[W];
				for(int c=0;c<W;c++)
				{
					labels[b][c]=0;
					sinks[b][c]=0;
					basin[b][c].w=-1;
					basin[b][c].h=-1;
					touched[b][c] = 0;
					fscanf(input,"%d",&map[b][c]);
					//cout<<map[b][c]<<" ";
				}
//				cout<<endl;
			}
			
			//not necessary, even with large input, but it looks nice
			//check first row for sinks
			for(int i=1;i<W-1;i++)
			{
				//cout<<"1line"<< map[0][i] << " " << map[0][i-1] <<" " << map[0][i] <<" " << map[0][i+1] <<" " << ((H>1)?(map[0][i] <= map[1][i]):1)<<endl;
				//cout<<"2line"<< (map[0][i] <= map[0][i-1]) <<" " << (map[0][i] <= map[0][i+1]) <<" " << ((H>1)?(map[0][i] <= map[1][i]):1)<<endl;
				if(map[0][i] <= map[0][i-1] && map[0][i] <= map[0][i+1] && ((H>1)?(map[0][i] <= map[1][i]):1))
					sinks[0][i] = 1;
			}
			
			//check last row for sinks
			for(int i=1;i<W-1;i++)
				if(map[H-1][i] <= map[H-1][i-1] && map[H-1][i] <= map[H-1][i+1] && ((H>1)?(map[H-1][i] <= map[H-2][i]):1))
					sinks[H-1][i] = 1;
			
			//check left column for sinks
			for(int i=1;i<H-1;i++)
				if(map[i][0] <= map[i-1][0] && map[i][0] <= map[i+1][0] && ((W>1)?(map[i][0] <= map[i][1]):1))
					sinks[i][0] = 1;
			
			//check right column for sinks
			for(int i=1;i<H-1;i++)
				if(map[i][W-1] <= map[i-1][W-1] && map[i][W-1] <= map[i+1][W-1] && ((W>1)?(map[i][W-1] <= map[i][W-2]):1))
					sinks[i][W-1] = 1;
			
			//top left corner
			if(((W>1)?(map[0][0] <= map[0][1]):1) && ((H>1)?(map[0][0] <= map[1][0]):1))
				sinks[0][0] = 1;
			
			//top right corner
			if(((W>1)?(map[0][W-1] <= map[0][W-2]):1) && ((H>1)?(map[0][W-1] <= map[1][W-1]):1))
				sinks[0][W-1] = 1;
			
			//bottom left corner
			if(((W>1)?(map[H-1][0] <= map[H-1][1]):1) && ((H>1)?(map[H-1][0] <= map[H-2][0]):1))
				sinks[H-1][0] = 1;
			
			//bottom right corner
			if(((W>1)?(map[H-1][W-1] <= map[H-1][W-2]):1) && ((H>1)?(map[H-1][W-1] <= map[H-2][W-1]):1))
				sinks[H-1][W-1] = 1;
			
			for(int c=1;c<H-1;c++)
				for(int d=1;d<W-1;d++)
					if(map[c][d] <= map[c][d-1] && map[c][d] <= map[c][d+1] && map[c][d] <= map[c-1][d] && map[c][d] <= map[c+1][d])
						sinks[c][d] = 1;
			
			/*
			cout<<"Basins:"<<endl;
			for(int c=0;c<H;c++)
			{
				for(int d=0;d<W;d++)
					printf("%d ",sinks[c][d]);
				cout<<endl;
			}*/
			
			
			for(int h=0;h<H;h++)
				for(int w=0;w<W;w++)
					if(sinks[h][w])
					{
						basin[h][w].h = h;
						basin[h][w].w = w;
						spawn(h,w);
					}
			
			int labelPos = 0;
			for(int c=0;c<H;c++)
			{
				for(int d=0;d<W;d++)
					if(labels[basin[c][d].h][basin[c][d].w] == 0)
					{
						labels[basin[c][d].h][basin[c][d].w] = labelPos + 'a';
						labelPos+=1;
					}
			}
			printf("Case #%d:\n",a+1);
			for(int c=0;c<H;c++)
			{
				for(int d=0;d<W;d++)
					printf("%c ",labels[basin[c][d].h][basin[c][d].w]);
				printf("\n");
					//cout<<labels[basin[c][d].h][basin[c][d].w]<<" ";
				//cout<<endl;
			}
			//cout<<endl<<endl;
			delete[] touched;
			delete[] basin;
			delete[] sinks;
			delete[] map;
			delete[] labels;
		}
		fclose(input);
	}
	else
	{
		cout <<"File not found";
	}
    return 0;
}

void spawn(int h,int w)
{
	//top
	if(h>0)
		if(!touched[h-1][w] && map[h-1][w] > map[h][w])
		{
			if(wouldPointGoToPoint(h-1,w,h,w))
			{
				touched[h-1][w] = 1;
				basin[h-1][w].h = basin[h][w].h;
				basin[h-1][w].w = basin[h][w].w;
				spawn(h-1,w);
			}
		}
	//bottom
	if(h<H-1)
		if(!touched[h+1][w] && map[h+1][w] > map[h][w])
		{
			if(wouldPointGoToPoint(h+1,w,h,w))
			{
				touched[h+1][w] = 1;
				basin[h+1][w].h = basin[h][w].h;
				basin[h+1][w].w = basin[h][w].w;
				spawn(h+1,w);
			}
		}
	
	//left
	if(w>0)
		if(!touched[h][w-1] && map[h][w-1] > map[h][w])
		{
			if(wouldPointGoToPoint(h,w-1,h,w))
			{
				touched[h][w-1] = 1;
				basin[h][w-1].h = basin[h][w].h;
				basin[h][w-1].w = basin[h][w].w;
				spawn(h,w-1);
			}
		}
	
	//right
	if(w<W-1)
		if(!touched[h][w+1] && map[h][w+1] > map[h][w])
		{
			if(wouldPointGoToPoint(h,w+1,h,w))
			{
				touched[h][w+1] = 1;
				basin[h][w+1].h = basin[h][w].h;
				basin[h][w+1].w = basin[h][w].w;
				spawn(h,w+1);
			}
		}
}

bool wouldPointGoToPoint(int h1,int w1,int h2,int w2)
{
	int top = 11000;
	int right = 11000;
	int left = 11000;
	int bottom = 11000;
	int last=-1;
	bool t = false;
	bool r = false;
	bool l = false;
	bool b = false;
	if(h1>0)
		top = map[h1-1][w1];
	if(h1<H-1)
		bottom = map[h1+1][w1];
	if(w1>0)
		left = map[h1][w1-1];
	if(w1<W-1)
		right = map[h1][w1+1];
	int count=0;
	if(top <= right && top <= bottom && top <=left)
	{
		t=true;
		last = top;
		count++;
	}
	if(right <= top && right <= bottom && right <=left)
	{
		r=true;
		last = right;
		count++;
	}
	if(bottom <= top && bottom <= right && bottom <=left)
	{
		b=true;
		last = bottom;
		count++;
	}
	if(left <= top && left <= right && left <= bottom)
	{
		l=true;
		last = left;
		count++;
	}
	if(count>1)
	{
		point wouldPoint;
		if(t)
		{
			wouldPoint.w=w1;
			wouldPoint.h=(h1-1);
		}
//			if((h1-1) == h2 && w1 == w2)
//				return true;
		else if(l)
		{
			wouldPoint.w=(w1-1);
			wouldPoint.h=h1;
		}
//			if(h1 == h2 && (w1-1) == w2)
//				return true;
		else if(r)
		{
			wouldPoint.w=(w1+1);
			wouldPoint.h=h1;
		}
//			if(h1 == h2 && (w1+1) == w2)
//				return true;
		else if(b)
		{
			wouldPoint.w=(w1);
			wouldPoint.h=(h1+1);
			
		}
//			if((h1+1) == h2 && w1 == w2)
//				return true;
		else
			cout<<"fuck";
		if(wouldPoint.w == w2 && wouldPoint.h == h2)
			return true;
		else
			return false;
		
	}
	else if(count == 1)
	{
		if(last == map[h2][w2])
			return true;
		else
			return false;
	}
	else
		cout<<"fuck!!!!!!!!!!!!!!!!!!!!!!!!!!!";
	return false;
}
