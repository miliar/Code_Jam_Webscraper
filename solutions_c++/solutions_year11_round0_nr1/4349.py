#include <iostream>

using namespace std;
#define REP(i, n) for(int i=0;i<n;i++)

int main()
{
	int tc;

	freopen("bot.out","w",stdout);
	cin >> tc;
	REP(_case, tc)
	{
		int time=0, n, c_o=0, c_b=0, first=-1, pos_o=1, pos_b=1;
		int command[100][2];

		cin >> n;

		REP(i, n)
		{
			char tmp;
			cin >> tmp >> command[i][1];
			if(tmp=='O') command[i][0] = 0;
			else command[i][0] = 1;
		}
		
		REP(i, n)
		{
			if(command[i][0] == 0) first = 0; // 오렌지가 해야해
			else first=1; // 블루가 해야해

			for(int j=i;j<n;j++)
			{
				if(command[j][0] == 0) { c_o = command[j][1]; break;}
			}
			for(int j=i;j<n;j++) 
			{
				if(command[j][0] == 1) { c_b = command[j][1]; break;}
			}

			int len_o = c_o - pos_o;
			int len_b = c_b - pos_b;
			if(first==0)
			{
				if(abs(len_o) < abs(len_b))	
				{
					pos_o += len_o;
					if(len_o*len_b < 0) pos_b -= len_o;
					else pos_b += len_o;
					
					time += abs(len_o);
				}
				else
				{
					pos_o += len_o;
					pos_b += len_b;

					time += abs(len_o);
				}
				if(pos_b < c_b) pos_b++;
				else if(pos_b > c_b) pos_b--;
				time++;
			}
			else
			{
				if(abs(len_b) < abs(len_o))	
				{
					pos_b += len_b;
					if(len_o*len_b < 0) pos_o -= len_b;
					else pos_o += len_b;
					
					time += abs(len_b);
				}
				else
				{
					pos_o += len_o;
					pos_b += len_b;

					time += abs(len_b);
				}
				if(pos_o < c_o) pos_o++;
				else if(pos_o > c_o) pos_o--;
				time++;
			}
		}	
		cout << "Case #" << _case+1 << ": " << time << endl;
	}

	return 0;
}
