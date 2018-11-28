#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

bool opp[256][256];
char comb[256][256];

int main()
{
	int T, C, D, x, y, len;
	string e, out, in, ivk;
	bool clean;
	
	cin >> T;
	for(int t=1; t<=T; t++)
	{
		cout << "Case #" << t << ": ";
		for(int i=0; i<256; i++)
			for(int j=0; j<256; j++)
			{
				comb[i][j] = 0;
				opp[i][j] = false;
			}
		cin >> C;
		while(C--)
		{
			cin >> in;
			x = in[0];
			y = in[1];			
			comb[x][y] = comb[y][x] = in[2];
		}	
		cin >> D;
		while(D--)
		{
			cin >> in;
			x = in[0];
			y = in[1];
			opp[x][y] = opp[y][x] = true;
		}		
		cin >> len;
		cin >> ivk;
		//~ cout << "ivk:" << ivk << endl;
		e.clear();
		e += ivk[0];
		for(int i=1; i<len; i++)
		{
			clean = false;
			x = ivk[i];
			y = e[e.size()-1];
			//~ cout << "x: " << (char)x << endl;
			//~ cout << "y: " << (char)y << endl;
			if(comb[ x ][ y ] != 0)
			{
				e[e.size()-1] = comb[ x ][ y ];
				continue;
			}
			
			for(int j=0; j<(int)e.size(); j++)
			{
				y = e[j];
				if(opp[x][y])
				{
					e.clear();
					clean = true;
				}
			}
			
			if(!clean)
			{ 
				//~ cout << "ivk" << i << ": " << ivk[i] << endl; 
				e+=ivk[i];
			}
			//~ cout << "e: " << e << endl;
		}
		
		out.clear();
		for(int i=0; i<(int)e.size(); i++)
		{
			out = out + ' ' + e[i] + ',';
		}
		if(out.size() == 0)
			out = "[]";
		else
		{
			out[0] = '[';
			out[out.size()-1] = ']';
		}
		cout << out << endl;
	}
	return 0;
}
