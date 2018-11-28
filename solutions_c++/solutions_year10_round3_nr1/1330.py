#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>
#include <queue>

using namespace std;

template <class T>
inline std::string to_string (const T& t)
{
std::stringstream ss;
ss << t;
return ss.str();
}


struct Point
{
	float x;
	float y;
	Point(int _x,int _y):x(_x),y(_y) { }
	Point() { }
};

struct Line
{
	Point start;
	Point end;
	float m;
	Line(Point s,Point e)
	{
		start=s;
		end=e;
		m=(e.y-s.y)/(e.x-s.x);
	}
	Line() { }
};


int main()
{
	int i=0,c=0,n=0,t=0,r=0,f=0;
	int T,R,k,N;
	string s;
	vector<long long int> arr;
	int x=0 ; 
	int toplam=0;
	int aY=0;
	int bY=0;

	int AX=0;
	int BX=1;

	freopen("A-large.in","r",stdin);
	freopen("output","w",stdout);

	vector<Line> lines;
	int seen=0;
	cin>>T;
	for(t=0;t<T;t++)
	{
		cin>>N;		
		for(int i=0;i<N;i++)
		{
			cin>>aY>>bY;
			lines.push_back(Line(Point(0,aY),Point(1,bY)));			
		}
		for(int k=0;k<lines.size();k++)
		{
			for(int j=k+1;j<lines.size();j++)
			{
				if(lines[k].start.y > lines[j].start.y) 
				{
					if(lines[k].end.y < lines[j].end.y)
						seen++;
				}
				else if(lines[k].start.y < lines[j].start.y) 
				{
					if(lines[k].end.y > lines[j].end.y)
						seen++;
				}
			}
		}
		
		cout<<"Case #"<<t+1<<": "<<seen<<endl;
		seen=0;
		lines.clear();
	}


}