#include <vector>
#include <string>
#include <iostream>
#include <memory.h>
#include <algorithm>
#include <stack>
#include <fstream>

using namespace std;


char  bas[100][100];
short alt[100][100];
int h,w;


class cell
{
	public:
		cell(int _i, int _j): i(_i), j(_j){}
		cell(){};
	int i,j;
};

class celln
{
	public:
		celln(int _i, int _j, int _ni = 0, int _nj = 0): c(_i, _j), n(_ni, _nj){}
	cell n,c;
};

cell getFlowNeighbour(const cell& c);

bool operator < (const cell& left, const cell& right)
{
	if(alt[left.i][left.j] < alt[right.i][right.j])
		return true;
	return false;
};

bool operator == (const cell& left, const cell& right)
{
	if(left.i == right.i && left.j == right.j)
		return true;
	return false;
};

int flow(const celln &c)
{
	//Check for flow from cell to neighbour	
	cell n	= getFlowNeighbour(c.c);
	if(n == c.n && n < c.c)
		return 1;

	//Neighbour -> cell
	n	= getFlowNeighbour(c.n);
	if(c.c == n && n < c.n)
		return -1;

	return 0;
}

cell getFlowNeighbour(const cell& c)
{
	vector<cell> cv;

	if(c.i > 0)
		cv.push_back(cell(c.i-1,c.j));
	if(c.j > 0)
		cv.push_back(cell(c.i,c.j-1));
	if(c.j +1 < w)
		cv.push_back(cell(c.i,c.j+1));
	if(c.i +1 < h)
		cv.push_back(cell(c.i+1,c.j));

	return *min_element(cv.begin(),cv.end());
}

int main()
{
	int c;
	cin >> c;

	stack<celln> st;

	for(int i = 0; i < c; i++)
	{
		cin >> h >> w;
		
		for(int i = 0; i < h; i++)
			for(int j = 0; j < w; j++)
				cin >> alt[i][j];

		memset(bas,0,sizeof(char)*100*100);
		char nextb	= 'a';

		for(int i = 0; i < h; i++)
		{
			for(int j = 0; j < w; j++)
			{
				if(bas[i][j] == 0)
				{
					bas[i][j] = nextb;
					if(i > 0)
						st.push(celln(i-1,j,i,j));
					if(j > 0)
						st.push(celln(i,j-1,i,j));
					if(j +1 < w)
						st.push(celln(i,j+1,i,j));
					if(i +1 < h)
						st.push(celln(i+1,j,i,j));

				while(st.size() > 0)
				{
					celln c	= st.top();
					st.pop();
					if(bas[c.c.i][c.c.j] == bas[c.n.i][c.n.j])
						continue;
					int f	= flow(c);
					if(f != 0)
					{
						bas[c.c.i][c.c.j] = nextb;
						if(c.c.i > 0)
							st.push(celln(c.c.i-1,c.c.j,c.c.i,c.c.j));
						if(c.c.j > 0)
							st.push(celln(c.c.i,c.c.j-1,c.c.i,c.c.j));
						if(c.c.j +1 < w)
							st.push(celln(c.c.i,c.c.j+1,c.c.i,c.c.j));
						if(c.c.i +1 < h)
							st.push(celln(c.c.i+1,c.c.j,c.c.i,c.c.j));
					}
				}
				nextb++;
				}
			}
		}

		cout << "Case #" << i+1 << ": " <<  endl;
		for(int i = 0; i < h; i++)
		{
			for(int j = 0; j < w; j++)
				cout << bas[i][j] << " ";
			cout << endl;
		}

	}
}
