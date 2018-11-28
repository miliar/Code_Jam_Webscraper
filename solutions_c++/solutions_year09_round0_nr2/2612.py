/*
 * =====================================================================================
 *
 *       Filename:  watershed.cpp
 *
 *    Description:  timepass
 *
 *        Version:  1.0
 *        Created:  09/03/2009 08:06:13 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Bharath (IISc), ajeetbharath@gmail.com
 *        Company:  SilverOak Systems
 *
 * =====================================================================================
 */

#include<iostream>

using namespace std;

typedef unsigned int UINT;

const UINT TMAX=100,HMIN=1,HMAX=100,WMAX=100,WMIN=1,BASINMAX=26,MAX_ALT=10000;

class CoOrd
{
public:
	UINT x,y;
};

class Node
{
	public:
		UINT height;
		char basin;
};

class Array
{
	Node nodes[HMAX+2][WMAX+2];
	public:
		friend ostream& operator <<	(ostream&,const Array&);
		friend istream& operator >>	(istream& stream,Array &array);
		void process();
		char findBasin(UINT x,UINT y);
		CoOrd findOutputNode(UINT x,UINT y);
	private:
		UINT rows,columns;
		char basinCount;
};

CoOrd Array::findOutputNode(UINT x,UINT y)
{
	UINT i,j;

	CoOrd minpos={x,y};
	
	for(i=x-1;i<=x+1;i++)
		for(j=y-1;j<=y+1;j++)
		{
			if(i==x || j==y)
			{
				if( nodes[i][j].height < nodes[minpos.x][minpos.y].height )
				{
					minpos.x=i;
					minpos.y=j;
				}
			}
		}

	return minpos;
}

char Array::findBasin(UINT x,UINT y)
{
	char ret='?';	
	CoOrd minpos;

	if(nodes[x][y].basin == '#')
	{
		minpos=findOutputNode(x,y);
		if(minpos.x==x && minpos.y==y)
		{
			nodes[x][y].basin=basinCount++;
		}
		else
		{
			nodes[x][y].basin=findBasin(minpos.x,minpos.y);
		}
	}

	ret=nodes[x][y].basin;

	return ret;
}

void Array::process()
{
	UINT i,j;
	for(i=1;i<=rows;i++)
	{
		for(j=1;j<=columns;j++)
		{
			findBasin(i,j);
		}
	}
}

istream& operator >>	(istream& ip,Array &array)
{
	UINT i,j;
	array.basinCount='a';
	ip>>array.rows>>array.columns;
	for(i=0;i<array.rows+2;i++)
	{
		array.nodes[i][0].height=MAX_ALT+1;
		array.nodes[i][array.columns+1].height=MAX_ALT+1;
	}
	for(j=0;j<array.columns+2;j++)
	{
		array.nodes[0][j].height=MAX_ALT+1;
		array.nodes[array.rows+1][j].height=MAX_ALT+1;
	}
	for(i=1;i<=array.rows;i++)
		for(j=1;j<=array.columns;j++)
		{
			ip>>array.nodes[i][j].height;
			array.nodes[i][j].basin='#';
		}
	return ip;
}

ostream& operator <<	(ostream& stream,const Array &array)
{
	UINT i,j;
	for(i=1;i<=array.rows;i++)
	{
		for(j=1;j<=array.columns;j++)
		{
			cout<<array.nodes[i][j].basin;
			if(j<array.columns)
				cout<<" ";
		}
		cout<<endl;
	}
	return stream;
}

int main()
{
	Array array;
	UINT i,no;
	cin>>no;
	for(i=1;i<=no;i++)
	{
		cin>>array;
		array.process();
		cout<<"Case #"<<i<<":"<<endl;
		cout<<array;
	}
	return 0;
}
