#include <iostream>
#include <vector>
#include <string>

using namespace std;

const string owon = "O won";
const string xwon = "X won";
const string draw = "Draw";
const string notended = "Game has not completed";


int main()
{
	ios::sync_with_stdio(0);
	int t, n = 0;
	cin >> t;
	
	while(t--)
	{
		n++;
		string tab[4];
		cin >> tab[0] >> tab[1] >> tab[2] >> tab[3];
		vector <int> xpts(10, 0);
		vector <int> opts(10, 0);

		for(int i=0; i<4; i++)
		{
			for(int k=0; k<4; k++) 
			{
				if(tab[i][k] == 'X') xpts[i]++;
				else if(tab[i][k] == 'O') opts[i]++;
				else if(tab[i][k] == 'T') xpts[i]++, opts[i]++;
			}
		}
		
		for(int k=0; k<4; k++)
		{
			for(int i=0; i<4; i++) 
			{
				if(tab[i][k] == 'X') xpts[k+4]++;
				else if(tab[i][k] == 'O') opts[k+4]++;
				else if(tab[i][k] == 'T') xpts[k+4]++, opts[k+4]++;
			}
		}

		for(int i=0; i<4; i++)
		{
			if(tab[i][i] == 'X') xpts[8]++;
			else if(tab[i][i] == 'O') opts[8]++;
			else if(tab[i][i] == 'T') xpts[8]++, opts[8]++;
		}
		for(int i=0; i<4; i++)
		{
			if(tab[3-i][i] == 'X') xpts[9]++;
			else if(tab[3-i][i] == 'O') opts[9]++;
			else if(tab[3-i][i] == 'T') xpts[9]++, opts[9]++;
		}

		int maxx = 0, maxo = 0;
		for(int i=0; i<10; i++) maxx = xpts[i] > maxx ? xpts[i] : maxx;
		for(int i=0; i<10; i++) maxo = opts[i] > maxo ? opts[i] : maxo;

		bool dots = false;
		for(int i=0; i<4; i++) for(int k=0; k<4 && !dots; k++) if(tab[i][k] == '.') dots = true;


		string ans;
		if( maxx == 4 && maxo < 4) ans = xwon;
		else if(maxo == 4 && maxx < 4) ans = owon;
		else ans = dots ? notended : draw;

		cout << "Case #" << n << ": " << ans << endl;
	}


	return 0;
}