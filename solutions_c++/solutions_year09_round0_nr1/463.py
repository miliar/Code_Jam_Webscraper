#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;
const int MAXLEN = 5001;
const int STRLEN = 20;
bool Check(char str[], int len1, char pattern[], int len2)
{
	int pos = 0;
	int i;
	bool ahead = true;
	bool equal = false;
	for(i=0; i<len2; ++i)
	{
		char c = pattern[i];
		if(c == '(')
		{
			ahead = false;
			
		}
		else if(c == ')')
		{
			ahead = true;
		}
		else
		{
			if(str[pos] == c)
			{
				equal = true;
			}
		}

		if(ahead)
		{
			if(!equal)
				return false;
			equal = false;
			++pos;
		}
	}
	return true;
}
int main()
{
	int len, d, n;
	char strs[MAXLEN][STRLEN];
	char pattern[MAXLEN*STRLEN];

	cin >> len >> d >> n;

	int nums[MAXLEN];
	memset(nums, 0, MAXLEN*sizeof(int));

	int i, j;
	for(i=0; i<d; ++i)
	{
		cin >> strs[i];
	}

	ofstream out("result.txt");

	for(i=0; i<n; ++i)
	{
		cin >> pattern;
		for(j=0; j<d; ++j)
		{
			nums[i] += Check(strs[j], len, pattern, strlen(pattern));
		}
		out << "Case #" << i+1 << ": " << nums[i] << endl;
	}
	out.close();
	


	return 0;
}


/*
#include <iostream>
#include <fstream>
using namespace std;
const int MAXLEN = 101;
int maps[MAXLEN][MAXLEN];
char res[MAXLEN][MAXLEN];
int path[MAXLEN*MAXLEN][2];
int dir[4][2] = {{-1, 0},{0, -1},{0, 1},{1, 0}};
bool InBound(int h, int w, int x, int y)
{
	return x>=0 && x<h && y>=0 && y<w;
}
bool maped(int x, int y)
{
	return res[x][y] <= 'z' && res[x][y] >= 'a';
}
void dsp(int h, int w, int i, int j, int &ll, char &c)
{
	if(maped(i, j))
		return;

	int x, y, k;
	x = -1, y = -1;
	int minv = maps[i][j];
	for(k=0; k<4; k++)
	{
		int tempx = i+dir[k][0];
		int tempy = j+dir[k][1];
		if(InBound(h, w, tempx, tempy) && minv > maps[tempx][tempy])
		{
			x = tempx;
			y = tempy;
			minv = maps[tempx][tempy];
		}					
	}
	if(x != -1)
	{
		path[ll][0] = i;
		path[ll][1] = j;
		++ll;
		if(maped(x, y))
		{
			for(k=0; k<ll; ++k)
			{
				res[path[k][0]][path[k][1]] = res[x][y];
			}
			ll = 0;
		}
		else
		{
			dsp(h, w, x, y, ll, c);
		}		
	}
	else
	{
		res[i][j] = c;
		for(k=0; k<ll; ++k)
		{
			res[path[k][0]][path[k][1]] = c;
		}
		ll = 0;
		c++;
	}

}
int main()
{
	int t, h, w, i, j ;
	int n = 1, ll;
	cin >> t;
	ofstream out("res.txt");

	while(n <= t)
	{
		memset(res, ' ', MAXLEN*MAXLEN*sizeof(char));
		cin >> h >> w;
		for(i=0; i<h; ++i)
			for(j=0; j<w; ++j)
			{
				cin >> maps[i][j];
			}
		
		char c = 'a';
		ll = 0;

		for(i=0; i<h; ++i)
			for(j=0; j<w; ++j)
			{
				dsp(h, w, i, j, ll, c);				
			}

			out << "Case #" << n << ":"<<endl;
			for(i=0; i<h; ++i)
			{
				for(j=0; j<w; ++j)
				{
					out << res[i][j];
					if(j != w-1)
						out << ' ';
				}
				out << endl;
			}
		n++;
	}
	out.close();
	return 0;
}*//*
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstring>
using namespace std;
const int MAXLEN = 505;
int H[2][MAXLEN];
int main()
{
	int n, t =1 ;
	char strs[MAXLEN];
	char pattern[20] = "welcome to code jam";
	cin >> n;
	getchar();
	ofstream out("res.txt");

	while(t <= n)
	{
		int num = 0;
		int len;
		int i, j, cur, ncur;

		cin.getline(strs, MAXLEN);
		len = strlen(strs);
		for(i=0; i<=len; i++)
			H[0][i] = 1;

		for(i=0; i<=18; i++)
		{
			cur = (i+1) & 1;
			ncur = i & 1;
			for(j=0; j<=len; j++)
				H[cur][j] = 0;
			for(j=0; j<len; j++)
			{
				if(pattern[i] == strs[j])
				{
					H[cur][j+1] = H[ncur][j] + H[cur][j];
				}
				else
				{
					H[cur][j+1] = H[cur][j];
				}
			}
			for(j=0; j<len; j++)
				H[cur][j] %= 10000;
		}
		num = H[cur][len];
		num %= 10000;

		out.fill('0');
		out << "Case #" << t << ": " << setw(4) << num << endl;
		t++;
	}
	return 0;
}*/