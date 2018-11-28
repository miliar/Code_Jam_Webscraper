#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin("A-large.in.txt");
ofstream fout("A-large.out.txt");

int c, n, m;
int h[1024], w[1024];
bool bird[1024];

int LIMIT = 1100000;

int inner_min_h, inner_max_h, inner_min_w, inner_max_w;
int outer_min_h, outer_max_h, outer_min_w, outer_max_w;
bool foundbird;
int new_min_h, new_max_h, new_min_w, new_max_w;

int hh, ww;

bool can()
{
	for (int i = 0; i < n; i++)
		if (bird[i] == false)
		{
			if (h[i] <= new_max_h && h[i] >= new_min_h && w[i] <= new_max_w && w[i] >= new_min_w)
				return false;
		}
		return true;
}

int isbird(int a, int b)
{
	for (int i = 0; i < n; i++)
		if (a == h[i] && b == w[i])
		{
			if (bird[i] == true) return 1;
			if (bird[i] == false) return -1;
		}
	return 0;
}

int main()
{
	char s[1024];

	fin >> c;
	for (int cases = 1; cases <= c; cases++)
	{
		fin >> n;
		for (int i = 0; i < n; i++)
		{
			fin >> h[i] >> w[i];
			fin.getline(s, 1024);

			if (s[1] == 'B')
				bird[i] = true;
			else
				bird[i] = false;
		}

		inner_min_h = inner_min_w = LIMIT;
		inner_max_h = inner_max_w = 0;

		foundbird = false;
		for (int i = 0; i < n; i++)
			if (bird[i] == true)
			{
				if (h[i] < inner_min_h) inner_min_h = h[i];
				if (h[i] > inner_max_h) inner_max_h = h[i];
				if (w[i] < inner_min_w) inner_min_w = w[i];
				if (w[i] > inner_max_w) inner_max_w = w[i];

				foundbird = true;
			}

		outer_min_h = outer_min_w = 0;
		outer_max_h = outer_max_w = LIMIT;

		for (int i = 0; i < n; i++)
			if (bird[i] == false)
			{
				if (h[i] < inner_min_h && h[i] > outer_min_h) outer_min_h = h[i];

				if (h[i] > inner_max_h && h[i] < outer_max_h) outer_max_h = h[i];

				if (w[i] < inner_min_w && w[i] > outer_min_w) outer_min_w = w[i];

				if (w[i] > inner_max_w && w[i] < outer_max_w) outer_max_w = w[i];
			}


		fout << "Case #" << cases << ":" << endl;

		fin >> m;
		for (int i = 0; i < m; i++)
		{
			fin >> hh >> ww;

			if (isbird(hh, ww) == 1) 
			{
				fout << "BIRD" << endl;
				continue;
			} else
				if (isbird(hh, ww) == -1)
				{
					fout << "NOT BIRD" << endl;
					continue;
				}

			if (foundbird == false)
			{
				fout << "UNKNOWN" << endl;
				continue;
			}

			if (hh >= inner_min_h && hh <= inner_max_h && ww >= inner_min_w && ww <= inner_max_w)
			{
				fout << "BIRD" << endl;
				continue;
			}

			if (hh < inner_min_h) new_min_h = hh;
			else new_min_h = inner_min_h;

			if (hh > inner_max_h) new_max_h = hh;
			else new_max_h = inner_max_h;

			if (ww < inner_min_w) new_min_w = ww;
			else new_min_w = inner_min_w;

			if (ww > inner_max_w) new_max_w = ww;
			else new_max_w = inner_max_w;

			if (can() == true)
				fout << "UNKNOWN" << endl;
			else
				fout << "NOT BIRD" << endl;
		}

	}

	fout.close();
}