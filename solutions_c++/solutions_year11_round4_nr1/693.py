#include <cstdlib>
#include <cctype>
#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <assert.h>

using namespace std;

struct Walkway
{
	long double begin;
	long double end;
	long double speed;

	Walkway()
	{
	}
	Walkway(long double Begin,long double End,long double Speed)
	{
		begin=Begin;
		end=End;
		speed=Speed;
	}
};

int main()
{
	ifstream cin("C:\\Users\\Bryan\\Desktop\\TestFile.in");
	ofstream cout("C:\\Users\\Bryan\\Desktop\\Output.txt");

	int T;
	cin >> T;

	for(int counter=1;counter<=T;counter++)
	{
		long double X,S,R,t;
		int N;
		cin >> X >> S >> R >> t >> N;

		vector<Walkway> walkway;
		for(int n=0;n<N;n++)
		{
			int begin,end,speed;
			cin >> begin >> end >> speed;
			walkway.push_back(Walkway(begin,end,speed));
		}

		bool wasChange=true;
		while(wasChange)
		{
			wasChange=false;
			for(int c=0;c<(int)walkway.size()-1;c++)
			{
				if(walkway[c].begin>walkway[c+1].begin)
				{
					Walkway temp=walkway[c];
					walkway[c]=walkway[c+1];
					walkway[c+1]=temp;
					wasChange=true;
				}
			}
		}

		int size=(int)walkway.size();
		for(int c=0;c<size-1;c++)
		{
			if(walkway[c].end!=walkway[c+1].begin)
			{
				walkway.push_back(Walkway(walkway[c].end,walkway[c+1].begin,0));
			}
		}
		if(walkway[0].begin!=0)
		{
			walkway.push_back(Walkway(0,walkway[0].begin,0));
		}
		if(walkway[size-1].end!=X)
		{
			walkway.push_back(Walkway(walkway[size-1].end,X,0));
		}

		for(int c=0;c<(int)walkway.size();c++)
		{
			walkway[c].speed+=S;
		}

		wasChange=true;
		while(wasChange)
		{
			wasChange=false;
			for(int c=0;c<(int)walkway.size()-1;c++)
			{
				if(walkway[c].speed>walkway[c+1].speed)
				{
					Walkway temp=walkway[c];
					walkway[c]=walkway[c+1];
					walkway[c+1]=temp;
					wasChange=true;
				}
			}
		}

		int index=0;
		while(t>0 && index<(int)walkway.size())
		{
			if(((walkway[index].speed-S+R)*t)>=(walkway[index].end-walkway[index].begin))
			{
				t-=((walkway[index].end-walkway[index].begin)/(walkway[index].speed-S+R));
				walkway[index].speed+=(R-S);
			}
			else
			{
				long double end=walkway[index].begin+((walkway[index].speed-S+R)*t);
				walkway.push_back(Walkway(walkway[index].begin,end,walkway[index].speed-S+R));
				walkway.push_back(Walkway(end,walkway[index].end,walkway[index].speed));
				walkway.erase(walkway.begin()+index);
				t=0;
			}
			index++;
		}

		long double time=0;
		for(int c=0;c<(int)walkway.size();c++)
		{
			time+=((walkway[c].end-walkway[c].begin)/walkway[c].speed);
		}

		cout << "Case #" << counter << ": ";
		cout << (long long) time;
		cout << '.';
		time-=(long long)time;
		for(int c=0;c<7;c++)
		{
			time*=10;
			cout << (long long) time;
			time-=(long long)time;
		}
		cout << '\n';

	}

	return 0;
}