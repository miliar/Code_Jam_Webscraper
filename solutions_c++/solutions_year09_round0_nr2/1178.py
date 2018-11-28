#include <fstream>
#include <vector>
#include <stack>

using namespace std;

struct Point_t
{
	int row;
	int col;

	Point_t(int r=0, int c=0)
	{
		row=r;
		col=c;
	}
};

static ofstream out("out.txt");
static ifstream in("B-large.in");

static int  map[100][100];
static char label[100][100];
static int  visited[100][100];
static vector<Point_t> graph[100][100];

static int direction[4][2]={{-1,0},{0,-1},{0,1},{1,0}};


void GetFlowDes(int h, int w)
{
	int i;
	int r,c;
	int row,col;
	int min;
	Point_t p,tmp;

	for(row=0;row<h;++row)
	{
		for(col=0;col<w;++col)
		{
			graph[row][col].clear();
		}
	}

	for(row=0;row<h;++row)
	{
		for(col=0;col<w;++col)
		{
			min=100000;
			label[row][col]=0;
			visited[row][col]=0;
			for(i=0;i<4;++i)
			{
				r=row+direction[i][0];
				c=col+direction[i][1];
				if(r<0 || c<0 || r>=h || c>=w)
					continue;
				
				if(map[r][c]<map[row][col] && map[r][c]<min)
				{
					p.row=r;
					p.col=c;
					min=map[r][c];
				}
			}
			if(min<100000)
			{
				tmp.row=row;
				tmp.col=col;
				graph[row][col].push_back(p);
				graph[p.row][p.col].push_back(tmp);
			}
		}
	}
}

Point_t FindValid(int h, int w)
{
	int i,j;
	Point_t p(-1,-1);

	for(i=0;i<h;++i)
	{
		for(j=0;j<w;++j)
		{
			if(!visited[i][j])
			{
				p.row=i;
				p.col=j;
				return p;
			}
		}
	}

	return p;
}

void Search(int h, int w)
{
	stack<Point_t> stk;
	char currentLabel('a');
	Point_t p(0,0),tmp;
	int i,size;

	visited[0][0]=1;
	label[0][0]=currentLabel;
	stk.push(p);
	while(true)
	{
		if(!stk.empty())
		{
			p=stk.top();
			stk.pop();
			size=graph[p.row][p.col].size();
			for(i=0;i<size;++i)
			{
				tmp=graph[p.row][p.col][i];
				if(!visited[tmp.row][tmp.col])
				{
					label[tmp.row][tmp.col]=label[p.row][p.col];
					visited[tmp.row][tmp.col]=1;
					stk.push(tmp);
				}
			}
		}
		else
		{
			p=FindValid(h, w);
			if(p.col!=-1 && p.row!=-1)
			{
				visited[p.row][p.col]=1;
				label[p.row][p.col]=++currentLabel;
				stk.push(p);
			}
			else
				break;
		}
	}
}

void ReadData(int h, int w)
{
	int i,j;

	for(i=0;i<h;++i)
	{
		for(j=0;j<w;++j)
		{
			in >> map[i][j];
		}
	}
}

void Print(int h, int w)
{
	int i,j;

	for(i=0;i<h;++i)
	{
		for(j=0;j<w;++j)
		{
			if(!j)
				out << label[i][j];
			else
				out << " " << label[i][j];
		}
		out << endl;
	}
}

int main()
{
	int N,h,w;
	int i;

	in >> N;
	for(i=0;i<N;++i)
	{
		in >> h >> w;
		ReadData(h, w);
		GetFlowDes(h, w);
		Search(h, w);

		out << "Case #" << i+1 << ":" << endl;
		Print(h, w);
	}

	return 0;
}