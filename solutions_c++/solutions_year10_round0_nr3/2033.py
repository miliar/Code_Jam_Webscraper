#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip>
#include <ios>
#include <functional>

using namespace std;
typedef unsigned long long ull;

struct Group{
	ull size;
	ull moneyIfFirst;
	int newFirstIndex;
};

int main()
{
	ifstream ifs("C-large.in");
	ofstream ofs("C-large.out");
	Group groups[1000];
	if(ifs.is_open() && ofs.is_open())
	{
		int T;
		ifs>>T;
		int t=0;
		while(ifs.good() && t<T)
		{
			ull R, K;
			int N;
			ifs>>R>>K>>N;
			for(int j=0; j<N; j++) ifs>>groups[j].size;

			for(int j=0; j<N; j++)
			{
				ull size = 0;
				int index = 0;
				int realIndex;
				while( (size<=K) && (index<N) )
				{
					realIndex = j + index;
					if(realIndex>=N) realIndex-=N;
					index++;
					size+=groups[realIndex].size;
				}
				if(size>K)
				{
					size -= groups[realIndex].size;
					realIndex;
				}
				else
				{
					realIndex = j;
				}
				groups[j].moneyIfFirst = size;
				groups[j].newFirstIndex = realIndex;
			}

			ull DayProfit = 0;
			int currentFirstGroup = 0;
			for(int i=0; i<R; i++)
			{
				DayProfit += groups[currentFirstGroup].moneyIfFirst;
				currentFirstGroup = groups[currentFirstGroup].newFirstIndex;
			}
			ofs<<"Case #"<<++t<<": "<<DayProfit<<"\n";
			cout<<t<<" complited\n";
		}
	}
	ifs.close();
	ofs.close();

	return 0;
}