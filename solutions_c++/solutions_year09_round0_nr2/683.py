#include <iostream>
#include <stack>
using namespace std;

struct point
{
	int x;
	int y;
};

point GetNextPoint(int**data, int row, int line, int r, int l)
{
	point p;
	p.x=r;
	p.y=l;
	int min=data[r][l];
	if(r>0 && data[r-1][l]<min)
	{
		p.x=r-1;
		min=data[r-1][l];
	}
	if(l>0 && data[r][l-1]<min)
	{
		p.x=r;
		p.y=l-1;
		min=data[r][l-1];
	}
	if(l<line-1 && data[r][l+1]<min)
	{
		p.x=r;
		p.y=l+1;
		min=data[r][l+1];
	}
	if(r<row-1 && data[r+1][l]<min)
	{
		p.x=r+1;
		p.y=l;
	}
	return p;
}

void MarkMap(int** data, char** map, int row, int line)
{
	char ch='a';
	stack<point> s;
	for(int i=0; i<row; i++)
	{
		for(int j=0; j<line; j++)
			if(map[i][j]==0)
			{
				point p=GetNextPoint(data,row,line,i,j);
				if(p.x==i && p.y==j)
				{
					map[i][j]=ch;
					ch++;
				}
				else
				{
					if(map[p.x][p.y]>0)
					{
						map[i][j]=map[p.x][p.y];
						continue;
					}
					s.push(p);
					while(true)
					{
						point top=s.top();
						point p=GetNextPoint(data,row,line,top.x,top.y);
						if((p.x==top.x && p.y==top.y))
							break;
						s.push(p);
						if(map[p.x][p.y]>0)
							break;
					}
					char mch=ch;
					if(map[s.top().x][s.top().y]>0)
					{
						mch=map[s.top().x][s.top().y];
						s.pop();
					}
					else
						ch++;
					while(!s.empty())
					{
						point top=s.top();
						map[top.x][top.y]=mch;
						s.pop();
					}
					map[i][j]=mch;
				}
			}
	}
}

int main()
{
	int testNum,row,col;
	scanf("%d",&testNum);
	for(int k=1; k<=testNum; k++)
	{
		scanf("%d%d",&row,&col);
		int**data=new int*[row];
		char**map=new char*[row];
		for(int i=0; i<row; i++)
		{
			data[i]=new int[col];
			map[i]=new char[col];
			for(int j=0; j<col;j++)
			{
				scanf("%d",&data[i][j]);
				map[i][j]=0;
			}
		}
		MarkMap(data,map,row,col);
 		cout<<"Case #"<<k<<":"<<endl;
  		for(int i=0; i<row; i++)
  		{
  			for(int j=0; j<col; j++)
  				cout<<map[i][j]<<"  ";
  			cout<<endl;
  		}
		for(int i=0; i<row; i++)
		{
			delete []data[i];
			delete []map[i];
		}
		delete []data;
		delete []map;
	}
	return 0;
}