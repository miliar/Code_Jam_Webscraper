#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>


using namespace std;

int T;
int W, H;
int** bmap;
char** result;

inline bool legal(int h, int w)
{
    return (h>=0 && w>=0 && h<H && w<W);
}

char waterway(int sx, int sy, list< pair<int, int> > &way)
{
    if (result[sx][sy]!=0) return result[sx][sy];
    int min=bmap[sx][sy];
    int vert(0), hor(0);
    if (legal(sx-1, sy) && bmap[sx-1][sy] < min) { min=bmap[sx-1][sy]; vert=0; hor=-1;}
    if (legal(sx, sy-1) && bmap[sx][sy-1] < min) { min=bmap[sx][sy-1]; vert=-1; hor=0;}
    if (legal(sx, sy+1) && bmap[sx][sy+1] < min) { min=bmap[sx][sy+1]; vert=1; hor=0;}
    if (legal(sx+1, sy) && bmap[sx+1][sy] < min) { min=bmap[sx+1][sy]; vert=0; hor=1;}
    way.push_back(pair<int, int> (hor, vert));

    if (hor==0 && vert==0) return result[sx][sy];
    else return waterway(sx+hor, sy+vert, way);
}


int main()
{
    
    cin >> T;

    for (int cn(1); cn<=T; ++cn)
    {
	cin >> H;
	cin >> W;

	bmap=new int*[H];
	result=new char*[H];

	for (int i(0); i<H; ++i)
	{
	    result[i]=new char[W];
	    for (int j(0); j<W; ++j)
		result[i][j]=0;
	    bmap[i]=new int[W];
	}
	for (int i(0); i<H; ++i)
	{
	    for (int j(0); j<W; ++j)
		cin >> bmap[i][j];

	}

	char nextbasin='a';
	char curbasin;

	for (int i(0); i<H; ++i)
	{
	    for (int j(0); j<W; ++j)
	    {
		list< pair<int, int> > way;
		curbasin=waterway(i,j,way);
		if (curbasin==0) curbasin=nextbasin++;
		int x(i), y(j);

		while (!way.empty())
		{
		    result[x][y]=curbasin;
		    x+=(way.front().first);
		    y+=(way.front().second);
		    way.pop_front();
		}
	    }
	}


	cout << "Case #" << cn << ":" << endl;
	for (int i(0); i<H; ++i)
	{
	    delete[] bmap[i];
	    for (int j(0); j<W; ++j)
		cout << result[i][j] << " ";
	    cout << endl;
	    delete[] result[i];
	}

	delete[] result;
	delete[] bmap;

    }
    return 0;
}
