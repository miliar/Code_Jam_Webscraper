#include <fstream>
#include <iostream>
#include <math.h>

using namespace std;

ifstream fin("as.in");
ofstream fout("as.out");
typedef struct 
{
	int time;
	int button;
}status;

int abs(int a)
{
	return a > 0 ? a : -a;
}

int main()
{
	status o, b;
	int T, N, s, i = 1, j, len, nt;

	char ch;

	fin >> T;

	for(i = 1; i <= T; i ++)
	{
		o.time = 0;
		b.time = 0;
		o.button = 1;
		b.button = 1;
		fin >> N;
		for(j = 0; j < N; j ++)
		{
			fin >> ch;
			fin >> s;
			switch(ch)
			{
			case 'O':
				len = abs(s - o.button);
				o.button = s;
				nt = o.time + len;
				if(nt >= b.time)
				{
					o.time = nt + 1;
				}
				else
				{
					o.time = b.time + 1;;
				}
				break;
			case 'B':
				len = abs(s - b.button);
				b.button = s;
				nt = b.time + len;
				if(nt >= o.time)
				{
					b.time = nt + 1;
				}
				else
				{
					b.time = o.time + 1;;
				}
				break;
			default:
				cout << "error!" << endl;
				return 0;
			}
		}
		fout << "Case #" << i << ": " << ((o.time > b.time) ? o.time : b.time) << endl;
	}
	return 0;
}
