// Jai Mata Di
#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
class Cell
{
public:
	int lat;
	char label;
	Cell(int i,char c)
	{
		lat = i;
		label = c;
	}
};
class Map
{
public:
	int h,w;
	vector <vector <Cell> > m;
	void getNext(int& a,int& b,int i,int j)
	{
		int min=m[i][j].lat;
		a=i;
		b=j;
		if(i<h-1)
		{
			if(m[i+1][j].lat<=min && m[i+1][j].lat != m[i][j].lat)
			{
				a=i+1;
				b=j;
				min=m[i+1][j].lat;
			}
		}
		if(j<w-1)
		{
			if(m[i][j+1].lat<=min && m[i][j+1].lat != m[i][j].lat)
			{
				a=i;
				b=j+1;
				min=m[i][j+1].lat;
			}
		}
		if(j>0)
		{
			if(m[i][j-1].lat<=min && m[i][j-1].lat != m[i][j].lat)
			{
				a=i;
				b=j-1;
				min=m[i][j-1].lat;
			}
		}
		if(i>0)
		{
			if(m[i-1][j].lat<=min && m[i-1][j].lat != m[i][j].lat)
			{
				a=i-1;
				b=j;
				min=m[i-1][j].lat;
			}
		}
	}
	Map()
	{
	}
	void displayLatMap()
	{
		for(int i=0;i<h;i++)
		{
			for(int j=0;j<w;j++)
			{
				cout<<m[i][j].lat<<" ";
			}
			cout<<"\n";
		}
	}
	void markLabel()
	{
		vector <vector <int> > v;
		vector <int> p;
		char counter='a';
		int a=0,b=0,i=0,j=0;
		for(int ic=0;ic<h;ic++)
		{
			for(int jc=0;jc<w;jc++)
			{
				if(m[ic][jc].label=='*')
				{
					i=ic;
					j=jc;
					do
					{
						getNext(a,b,i,j);
						if(m[a][b].label != '*')
						{
							m[i][j].label=m[a][b].label;
							for(int k=0;k<v.size();k++)
							{
								m[v[k][0]][v[k][1]].label=m[a][b].label;
							}
							v.clear();
							break;
						}
						else
						{
							if(a!=i || b!=j)
							{
								p.clear();
								p.push_back(i);
								p.push_back(j);
								i=a;
								j=b;
								v.push_back(p);	
							}
							else
							{
								m[i][j].label=counter;
								for(int k=0;k<v.size();k++)
								{
									m[v[k][0]][v[k][1]].label=counter;
								}
								counter++;
								v.clear();
								break;
							}
						}
					}while(1);
				}
			}
		}
	}
	void displayLabelMap()
	{
		for(int i=0;i<h;i++)
		{
			for(int j=0;j<w;j++)
			{
				cout<<m[i][j].label<<" ";
			}
			cout<<"\n";
		}
	}
};
int main()
{
	fstream ip("B-small.in",ios::in);
	fstream op("B-small.out",ios::out);
	if(!ip.is_open() || !op.is_open())
	{
		cout<<"File opening Error";
	}
	int notc;
	ip>>notc;
	for(int k=1;k<=notc;k++)
	{
		Map map;
		ip>>map.h>>map.w;
		int lat;
		char label='*';
		for(int i=0;i<map.h;i++)
		{
			vector<Cell> p;
			for(int j=0;j<map.w;j++)
			{
				ip>>lat;
				Cell c(lat,label);
				p.push_back(c);
			}
			map.m.push_back(p);
		}

	//	map.displayLatMap();
		map.markLabel();
		op<<"Case #"<<k<<":"<<endl;
	//	map.displayLabelMap();
		for(int i=0;i<map.h;i++)
		{
			for(int j=0;j<map.w;j++)
			{
				op<<map.m[i][j].label<<" ";
			}
			op<<"\n";
		}
	}
	return 0;
}