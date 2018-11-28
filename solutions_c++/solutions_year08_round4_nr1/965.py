#include <iostream>
#include <fstream>
#include <map>
#include <iomanip>
using namespace std;

ifstream fin;
ofstream fout;
int N, M, V;


char line[1024];

struct ltstr
{
  bool operator()(string s1, string s2) const
  {
    return strcmp(s1.c_str(), s2.c_str()) < 0;
  }
};

map<string, int, ltstr> servers;


int compare (const void * a, const void * b)
{
  return ( *(int*)b - *(int*)a );
}


typedef struct
{
	int t;
	int c;
	int v;
} node;

node *sn;

int findmin(int root, int value)
{
	int r1, r2;
	if(value == sn[root].v)
		return 0;

	if(root >= (M - 1) / 2)
	{
		return -1;
	}
	else
	{
		//if(!sn[root].c)
	//	{
			if(value == 1)
			{
				if(sn[root].t == 1)
				{
					if(sn[root].c && (sn[root * 2 + 1].v || sn[root * 2 + 2].v))
						return 1;

					if(!sn[root].c)
					{
						r1 = findmin(root * 2 + 1, 1);
						if(r1 == -1)
							return -1;
						r2 = findmin(root * 2 + 2, 1);
						if(r2 == -1)
							return -1;
						return r1 + r2;
					}
					else
					{
						r1 = findmin(root * 2 + 1, 1);
						r2 = findmin(root * 2 + 2, 1);
						if(r1 == -1 && r2 == -1)
							return -1;

						if(r1 == -1)
							return r2 + 1;
						if(r2 == -1)
							return r1 + 1;

						return r1 < r2 ? r1 + 1: r2 + 1;
					}
				}
				else
				{
					r1 = findmin(root * 2 + 1, 1);
					r2 = findmin(root * 2 + 2, 1);
					if(r1 == -1 && r2 == -1)
						return -1;

						if(r1 == -1)
							return r2;
						if(r2 == -1)
							return r1;

					return r1 < r2 ? r1: r2;
				}	
			}
			else
			{
				if(sn[root].t == 1)
				{
					r1 = findmin(root * 2 + 1, 0);
					r2 = findmin(root * 2 + 2, 0);
					if(r1 == -1 && r2 == -1)
						return -1;

					if(r1 == -1)
						return r2;
					if(r2 == -1)
						return r1;

					return r1 < r2 ? r1: r2;
				}
				else
				{
					if(sn[root].c && (!sn[root * 2 + 1].v || !sn[root * 2 + 2].v))
						return 1;

					if(!sn[root].c)
					{
						r1 = findmin(root * 2 + 1, 0);
						if(r1 == -1)
							return -1;
						r2 = findmin(root * 2 + 2, 0);
						if(r2 == -1)
							return -1;

						return r1 + r2;
					}
					else
					{
							r1 = findmin(root * 2 + 1, 0);
							r2 = findmin(root * 2 + 2, 0);
							if(r1 == -1 && r2 == -1)
								return -1;

							if(r1 == -1)
								return r2 + 1;
							if(r2 == -1)
								return r1 + 1;

							return r1 < r2 ? r1 + 1: r2 + 1;
					}
				}
			}
	//	}

	}
}

void solve(int num)
{
	int i, j, k;

	for(i = (M - 1) / 2 - 1; i >= 0; i --)
	{
		if(sn[i].t)
		{
			sn[i].v = (sn[i * 2 + 1].v  & sn[i * 2 + 2].v);
		}
		else
		{
			sn[i].v = (sn[i * 2 + 1].v  | sn[i * 2 + 2].v);
		}
	}

	j = findmin(0, V);

	if(j != -1)
	{
		cout << "Case #" << num << ": " << j << endl;
		fout << "Case #" << num << ": " << j << endl;
	}
	else
	{
		cout << "Case #" << num << ": IMPOSSIBLE" << endl;
		fout << "Case #" << num << ": IMPOSSIBLE" << endl;
	}
}


int main()
{
	int i, j;
	fin.open("A-large.in");
	fout.open("A-large.out");

	fin >> N;
	fin.getline(line, 1024);

	for(i = 0; i < N; i ++)
	{
		fin >> M;
		fin >> V;
		fin.getline(line, 1024);
	
		sn = new node[M];

		for(j = 0; j < M; j ++)
		{
			if(j < (M - 1) / 2)
			{
				fin >> sn[j].t;
				fin >> sn[j].c;
				fin.getline(line, 1024);
			}
			else
			{
				fin >> sn[j].v;
				fin.getline(line, 1024);
			}
		}

		solve(i + 1);

		delete[] sn;
	}

	return 0;
}