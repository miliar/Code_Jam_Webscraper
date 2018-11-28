#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string map[50], tmp[60];

int main()
{
	bool red, blue;
	int cas, N, K;
	int dire[8][2] = { {-1,0}, {0,-1}, {1,0}, {0,1}, {1,1}, {-1,-1}, {1,-1}, {-1,1} };
	ifstream fin("test.in");
	ofstream fout("test.out");

	fin>>cas;
	for(int i=1; i<=cas; i++)
	{
		red = false;
		blue = false;
		fin>>N>>K;
		memset(map, 0, sizeof(map));
		memset(tmp, 0, sizeof(tmp));
		for(int j=0; j<N; j++)
			fin>>map[j];
		for(int j=0; j<60; j++)
			for(int k=0; k<60; k++)
				tmp[j] += '.';
		for(int j=N-1; j>=0; j--)  // rotate
		{
			int len;
			string t = "";

			for(int k=N-1; k>=0; k--)
				if( map[j][k] != '.' )
					t += map[j][k];
			len = t.length();
			for(int k=N-1; k>=N-len; k--)
				tmp[k][N-1-j] = t[N-1-k];
		}
		/*for(int j=0; j<N; j++)
		{
			for(int k=0; k<N; k++)
				fout<<tmp[j][k];
			fout<<endl;
		}*/
		for(int j=0; j<N; j++)
			for(int k=0; k<N; k++)
				if( tmp[j][k] != '.' )
				{
					for(int jj=0; jj<8; jj++)
					{
						int cnt = 0;
						for(int kk=0; kk<K; kk++)
						{
							int x = j+kk*dire[jj][0];
							int y = k+kk*dire[jj][1];
							if( x>=0 && x<N && y>=0 && y<N && tmp[x][y]==tmp[j][k] )
								cnt++;
							else
								break;
						}
						if( cnt==K && tmp[j][k]=='R' )
							red = true;
						else if( cnt==K && tmp[j][k]=='B' )
							blue = true;
					}
				}
		if( red==true && blue==true )
			fout<<"Case #"<<i<<": Both"<<endl;
		else if( red == true )
			fout<<"Case #"<<i<<": Red"<<endl;
		else if( blue == true )
			fout<<"Case #"<<i<<": Blue"<<endl;
		else
			fout<<"Case #"<<i<<": Neither"<<endl;
	}

	return 0;
}
