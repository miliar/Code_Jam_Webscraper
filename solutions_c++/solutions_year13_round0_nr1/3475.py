#include <iostream>
#include <string>
#include <vector>
using namespace std;

enum{XWIN=0, OWIN, DRAW, NOTCOMPLETE};
string stat_str[4] = {": X won", ": O won", ": Draw", ": Game has not completed"};

int check_stat(vector< vector<int> > &dat);

int main()
{
	int T; cin >> T;
	for(int n = 1; n <= T; n++)
	{
		string str[4];
		cin >> str[0];
		cin >> str[1];
		cin >> str[2];
		cin >> str[3];
		int t = 0; // if t is exist
		int i,j, ti = -1, tj = -1;
		vector< vector<int> > dat(4);
		dat[0] = vector<int>(4);
		dat[1] = vector<int>(4);
		dat[2] = vector<int>(4);
		dat[3] = vector<int>(4);

		for(j = 0; j < 4; j++)
		{
			for(i = 0; i < 4; i++)
			{
				if(str[j][i] == 'T')
				{
					t = 1;
					ti = i;
					tj = j;
				}
				else if(str[j][i] == 'X')
				{
					dat[j][i] = 1;
				}
				else if(str[j][i] == 'O')
				{
					dat[j][i] = -1;
				}
				else if(str[j][i] == '.')
				{
					dat[j][i] = 0;
				}
			}
		}

		if(t==0) 
		{
			int stat = check_stat(dat);
			cout<<"Case #"<<n<<stat_str[stat]<<endl;
		}
		else if(t == 1)
		{
			dat[tj][ti] = 1; 
			int stat = check_stat(dat);
			if(stat == XWIN || stat == OWIN)
			{
				cout<<"Case #"<<n<<stat_str[stat]<<endl;
				continue;
			}

			dat[tj][ti] = -1;
			stat = check_stat(dat);
			cout<<"Case #"<<n<<stat_str[stat]<<endl;
		}
	}
}

int check_stat(vector< vector<int> > &dat)
{
	for(int j = 0; j < 4; j++)
	{
		int sum = 0;
		for(int i = 0; i < 4; i++)
			sum += dat[j][i];
		if(sum == 4) return XWIN;
		else if(sum == -4) return OWIN;
	}
	for(int i = 0; i < 4; i++)
	{
		int sum = 0;
		for(int j = 0; j < 4; j++)
			sum += dat[j][i];
		if(sum == 4) return XWIN;
		else if(sum == -4) return OWIN;
	}

	int sum1 = 0;
	for(int i = 0; i < 4; i++)
	{
		sum1 += dat[i][i];
	}
	if(sum1 == 4) return XWIN;
	else if(sum1 == -4) return OWIN;

	int sum2 = 0;
	for(int i = 0; i < 4; i++)
	{
		sum2 += dat[i][3-i];
	}
	if(sum2 == 4) return XWIN;
	else if(sum2 == -4) return OWIN;

	for(int j = 0; j < 4; j++)
	{
		for(int i = 0; i < 4; i++)
		{
			if(dat[j][i] == 0) return NOTCOMPLETE;
		}
	}
	return DRAW;
}
