#include<iostream>
#include<cstdlib>
#include<algorithm>
using namespace std;

#define max 10

class Watershed
{
	int m[12][12];

	char l[10][10], mark;

	//int sinkPts[26][2];

	int sinks;

	int t, h, w;

	public:

		Watershed()
		{
			cin>>t;

			//cout<<t;

			for(int i = 0; i < t; i++)
			{
				cout<<"Case #"<<i+1<<":\n";
				getStarted();
			}

			//cout<<t;
		}

		void getStarted()
		{
			cin>>h>>w;

			for(int i = 0; i < (h+2); i++)
				m[i][0] = m[i][w+1] = 10;

			for(int i = 0; i < (w+2); i++)
				m[0][i] = m[h+1][i] = 10;

			for(int i = 0; i < h; i++)
				for(int j = 0; j < w; j++)
					cin>>m[i+1][j+1];

			sinks = markSink();

			mark = 'a';

			for(int i = 0; i < h; i++)
				for(int j = 0; j < w; j++)
					if(l[i][j] < 'a')
						l[i][j] = mapLabels(i, j);

			for(int i = 0; i < h; i++)
			{
				for(int j = 0; j < w; j++)
					cout<<l[i][j]<<" ";

				cout<<endl;
			}
		}

		int markSink()
		{
			int sink = 0;

			for(int i = 0; i < h ;i++)
				for(int j = 0; j < w; j++)
				{
					int min[4] = {m[i][j+1], m[i+1][j], m[i+1][j+2], m[i+2][j+1]};

					int *e = min_element(min, min+4);

					if(*e >= m[i+1][j+1])
					{
						l[i][j] = '\0';

						sink++;
					}
					else
						itoa(e-min, &l[i][j], 10);
				}

			return sink;
		}

		char mapLabels(int i, int j)
		{
			if(l[i][j] == '\0')
			{
				char temp = mark;
				mark++;
				return temp;
			}

			switch(l[i][j])
			{
				case '0':
							if(l[i-1][j] >= 'a')	return l[i-1][j];
							else					return l[i-1][j] = mapLabels(i-1, j);
				case '1':
							if(l[i][j-1] >= 'a')	return l[i][j-1];
							else					return l[i][j-1] = mapLabels(i, j-1);
				case '2':
							if(l[i][j+1] >= 'a')	return l[i][j+1];
							else 					return l[i][j+1] = mapLabels(i, j+1);
				case '3':
							if(l[i+1][j] >= 'a')	return l[i+1][j];
							else  					return l[i+1][j] = mapLabels(i+1, j);
			}
		}
};

int main()
{
	Watershed w;
}