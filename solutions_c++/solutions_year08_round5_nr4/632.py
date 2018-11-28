#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

template <class T>
inline const T& TMIN(const T& x, const T& y)
{ return (y<x ? y : x); }

template <class T>
inline const T& TMAX(const T& x, const T& y)
{ return (y<x ? x : y); }

template <class T>
inline const T& TMIN(const T& x, const T& y, const T& z)
{ return (y<x ? TMIN(y,z) : TMIN(x,z)); }

void main()
{
	ofstream ofs("D-small-attempt3.out");
	int i,j,k;
	int n;
	cin>>n;

	int h,w,rr,r,c;

	for(i=0; i<n; i++)
	{
		if(i==3)
			int gg=1;

		cin>>h>>w>>rr;

		vector<int> board1;
		vector<int> board2;
		vector<int> board3;
		vector<int> board4;
	
		vector<pair<int,int> > rock;

		for(j=0; j<rr; j++)
		{
			cin>>r>>c;
			if((r+c)%3!=2)
				continue;
			int xx=(r+c-2)/3;
			int yy=r-xx-1;
			if(yy<0 || yy>xx)
				continue;

			rock.push_back(pair<int,int>(xx,yy));
		}

		int targetX=(h+w-2)/3;
		int targetY=h-targetX-1;

		if(h+w==2)
		{
			ofs<<"Case #"<<i+1<<": "<<1<<endl;
			continue;
		}
		else if((h+w)%3!=2)
		{
			ofs<<"Case #"<<i+1<<": "<<0<<endl;
			continue;
		}
		else if(targetY<0 || targetY>targetX)
		{
			ofs<<"Case #"<<i+1<<": "<<0<<endl;
			continue;
		}

		board1.push_back(1);
		
		for(j=1; j<=targetX; j++)
		{
			board2.push_back(board1[0]);
			for(k=0; k<j-1; k++)
				board2.push_back((board1[k]+board1[k+1])%10007);
			board2.push_back(board1.back());

			for(k=0; k<rock.size(); k++)
			{
				if(rock[k].first==j)
				{
					board2[rock[k].second]=0;
				}
			}

			board1.swap(board2);
			board2.clear();
/*
			for(k=0; k<board1.size(); k++)
				cout<<board1[k]<<' ';
			cout<<endl;*/
		}
		
	ofs<<"Case #"<<i+1<<": "<<board1[targetY]<<endl;
		
	}
}
