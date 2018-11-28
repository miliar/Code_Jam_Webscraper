#include<iostream>
#include<algorithm>
using namespace std;

#define max 10000

class Watershed
{
	int m[102][102], t, h, w;

	char l[100][100], mark;

	public:

		Watershed()
		{
			cin>>t;

			for(int i = 0; i < t; i++)
			{
				cout<<"Case #"<<i+1<<":\n";
				getStarted();
			}
		}

		void getStarted()
		{
			cin>>h>>w;

			for(int i = 0; i < (h+2); i++)
				m[i][0] = m[i][w+1] = max;

			for(int i = 0; i < (w+2); i++)
				m[0][i] = m[h+1][i] = max;

			for(int i = 0; i < h; i++)
				for(int j = 0; j < w; j++)
					cin>>m[i+1][j+1];

			markSink();

			mark = 'a';

			for(int i = 0; i < h; i++)
				for(int j = 0; j < w; j++)
					if(l[i][j] < 'a')
						l[i][j] = putLabels(i, j);

			for(int i = 0; i < h; i++)
			{
				for(int j = 0; j < w; j++)
					cout<<l[i][j]<<" ";

				cout<<endl;
			}
		}

		void markSink()
		{
			for(int i = 0; i < h ;i++)
				for(int j = 0; j < w; j++)
				{
					int min[4] = { 
							m[i][j+1], 
							m[i+1][j], 
							m[i+1][j+2], 
							m[i+2][j+1]
						};

					int *x = min_element(min, min+4);

					if(*x >= m[i+1][j+1])
						l[i][j] = '\0';
					else
						l[i][j] = '0' + x - min;
				}
		}

		char putLabels(int i, int j)
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
						if(l[i-1][j] >= 'a')
							return l[i-1][j];
						else
							return l[i-1][j] = putLabels(i-1, j);
				case '1':
						if(l[i][j-1] >= 'a')
							return l[i][j-1];
						else
							return l[i][j-1] = putLabels(i, j-1);
				case '2':
						if(l[i][j+1] >= 'a')
							return l[i][j+1];
						else
							return l[i][j+1] = putLabels(i, j+1);
				case '3':
						if(l[i+1][j] >= 'a')
							return l[i+1][j];
						else
							return l[i+1][j] = putLabels(i+1, j);
			}
		}
};

int main()
{
	Watershed watershed;
}