#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int N;
string D[10010];
bool flag[10010];

bool char_in_str (string &in, char c)
{
	for (int i=0 ;i<in.length() ;i++)
	{
		if (in[i]==c)
			return true;
	}
	return false;
}

bool possible (char c)
{
	for (int i=0 ;i<N ;i++)
	{
		if (flag[i] && char_in_str(D[i], c))
			return true;
	}
	return false;
}

bool match (string &in, char *buff)
{
	for (int i=0 ;i<in.length() ;i++)
	{
		if (buff[i]!='_' && in[i]!=buff[i])
			return false;
	}
	return true;
}

bool char_left (string &in, char *buff, char c)
{
	for (int i=0 ;i<in.length() ;i++)
	{
		if (buff[i]=='_' && in[i]==c)
			return true;
	}
	return false;
}

void fill (string &in, char *buff, char c)
{
	for (int i=0 ;i<in.length() ;i++)
	{
		if (in[i]==c)
			buff[i] = c;
	}

	for (int i=0 ;i<N ;i++)
	{
		if (flag[i] && !match (D[i], buff))
			flag[i] = false;
		if (flag[i] && char_left (D[i], buff, c))
			flag[i] = false;
	}
}

void remove (char c)
{
	for (int i=0 ;i<N ;i++)
	{
		if (flag[i] && char_in_str (D[i], c))
			flag[i] = false;
	}
}

bool full (string &in, char *buff)
{
	for (int i=0 ;i<in.length() ;i++)
	{
		if (buff[i]=='_')
			return false;
	}
	return true;
}

int calc (string &in, string &list)
{
	int error = 0;
	char buff[8192];
	for (int i=0 ;i<in.length() ;i++)
		buff[i] = '_';
	for (int i=0 ;i<N ;i++)
	{
		if (D[i].length()==in.length())
			flag[i] = true;
		else
			flag[i] = false;
	}

	for (int i=0 ;i<list.size() ;i++)
	{
		if (possible (list[i]))
		{
			if (char_in_str (in, list[i]))
			{
				fill (in, buff, list[i]);
				if (full (in, buff))
					break;
			}
			else
			{
				remove (list[i]);
				error++;
			}
		}
	}

	return error;
}

void solve_case ()
{
	int M;
	cin >> N >> M;
	for (int i=0 ;i<N ;i++)
		cin  >> D[i];
	for (int i=0 ;i<M ;i++)
	{
		string list;
		cin >> list;
		int score = 0;
		int idx = -1;
		for (int j=0 ;j<N ;j++)
		{
			int tmp = calc (D[j], list);
			if (idx<0 || tmp>score)
			{
				idx = j;
				score = tmp;
			}
		}

		cout << D[idx];
		if (i!=M-1)
			cout << " ";
	}
	cout << endl;
}

int main ()
{
	int total_cases;

	cin >> total_cases;
	for (int cases=1 ;cases<=total_cases ;cases++)
	{
		cout << "Case #" << cases << ": ";
		solve_case ();
	}

	return 0;
}
