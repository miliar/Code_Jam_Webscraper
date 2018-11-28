#include <fstream>
#include <bitset>

using namespace std;

class rect
{
public:
	long int x1,x2,y1,y2;
};

rect rects[1000];
bool existY[1000001];
bool existX[1000001];
int R;
int miny,maxy;
int maxx,minx;

bool map[1000][1000];

/*void solve()
{
	for(int i=0;i<1000000;i++)
	{
		existY[i]=false;
		existX[i]=false;
	}
	for(int i1=miny;i1<=maxy;i1++)
	{
		for(int i=0;i<R;i++)
		{
			if(rects[i].y1<=i1 && rects[i].y2>=i1)
			{
				//Rect contains i
				for(int y=rects[i].x1;y<=rects[i].x2;y++)
				{
					existY[y]=true;
				}
			}
		}
		for(int i=0;i<R;i++)
		{
			if(rects[i].x1<=i1 && rects[i].x2>=i1)
			{
				//Rect contains i
				for(int y=rects[i].x1;y<=rects[i].x2;y++)
				{
					existX[y]=true;
				}
			}
		}
		for(int i=0;i<R;i++)
		{
			
			if(rects[i].y1<=i1+1 && rects[i].y2>=i1+1)
			{
				if(!exist[rects[i].x1]
			}
		}
	}
}*/

int solve()
{
	int cnt=0,pas=0;
	for(int i=0;i<1000;i++)
		for(int y=0;y<1000;y++)
		{
			if(map[i][y]==true)
				cnt++;
		}
	while(cnt>0)
	{
		pas++;
		for(int i=maxy;i>=miny;i=i-1)
			for(int y=maxx;y>=minx;y=y-1)
			{
				if(map[i][y]==true && (map[i-1][y]==false && map[i][y-1]==false))
				{
					cnt-=1;
					map[i][y]=false;
				}
				if(map[i][y]==false && (map[i-1][y]==true && map[i][y-1]==true))
				{
					cnt++;
					map[i][y]=true;
				}
			}
	}
	return pas;
}

int main()
{
	ifstream f("C-small.in");
	ofstream f2("output.out");

	int TEST;
	int T;
	f>>T;
	for(TEST=0;TEST<T;TEST++)
	{
		f>>R;
		miny=10000000;
		maxy=0;
		maxx=0;
		minx=10000000;
		for(int i=0;i<1000;i++)
			for(int y=0;y<1000;y++)
				map[i][y]=false;
		for(int i=0;i<R;i++)
		{
			f>>rects[i].x1>>rects[i].y1>>rects[i].x2>>rects[i].y2;
			for(int X=rects[i].x1;X<=rects[i].x2;X++)
				for(int Y=rects[i].y1;Y<=rects[i].y2;Y++)
					map[Y][X]=true;
			if(rects[i].y1<miny)
				miny=rects[i].y1;
			if(rects[i].y2>maxy)
				maxy=rects[i].y2;
			if(rects[i].x2>maxx)
				maxx=rects[i].x2;
			if(rects[i].x1<minx)
				minx=rects[i].x1;
		}
		f2<<"Case #"<<TEST+1<<": "<<solve()<<endl;
	}

	f.close();
	f2.close();
	return 0;

}