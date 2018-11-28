#include <cstdio>
#include <cstdlib>
#include <cstring>
const int MAXWH = 100;
int h, w;
int dir[5][2] = {{0, 0}, {-1, 0}, {0, -1}, {0, 1}, {1, 0}};
int key[MAXWH][MAXWH];
int lati[MAXWH][MAXWH];
int hash[26];
void swap (int& a, int& b)
{
	int c = a;
	a = b;
	b = c;
}
int find (int pos)
{
	if (key[pos / w][pos % w] == pos)
		return pos;
	return find(key[pos / w][pos % w]);
}
void set (int pos, int posn)
{
	int posh = find (pos);
	int posnh = find (posn);
	if (posh < posnh)
		swap (posh, posnh);
	key[posn / w][posn % w] = posnh;
	key[posnh / w][posnh % w] = posnh;
	key[posh / w][posh % w] = posnh;
	key[pos / w][pos % w] = posnh;
}
void merge (int j, int k, int min)
{
	int pos = j * w + k;
	int posn = (j + dir[min][0]) * w + k + dir[min][1];
	set (pos, posn);
}
bool check (int j, int k)
{
	if (j + 1)
		if (j < h)
			if (k + 1)
				if (k < w)
					return true;
	return false;
}
int main()
{
	int t;
	int mem;
	bool flag;
	scanf ("%d", &t);
	int min, minh;
	char minch;
	for (int i = 0; i < t; i ++)
	{
		printf ("Case #%d:\n", i + 1);
		scanf ("%d%d", &h, &w);
		for (int j = 0; j < h; j ++)
			for (int k = 0; k <w; k++)
				key[j][k] = j * w + k;
		for (int j = 0; j < h; j ++)
			for (int k = 0; k <w; k++)
				scanf ("%d", &lati[j][k]);
		for (int j = 0; j < h; j ++)
			for (int k = 0; k <w; k++)
			{
				min = 0; minh = lati[j][k];	
				for (int l = 1; l <= 4; l ++)
					if (check(j + dir[l][0], k + dir[l][1]))
						if (minh > lati[j + dir[l][0]][k + dir[l][1]])
						{
							minh = lati[j + dir[l][0]][k + dir[l][1]];
							min = l;
						}
				merge (j, k, min);
			}
		memset (hash, 0, sizeof(hash));
		hash[0] = 0;
		mem = 1;
		for (int j = 0; j < h; j ++)
			for (int k = 0; k <w; k++)
			{
				set (j * w + k, key[j][k]);
				flag = true;
				for (int l = 0; l < mem; l++)
				{
					if (hash[l] == key[j][k])
					{
						printf ("%c", 'a' + l);
						flag = false;
						break;
					}
				}
				if (flag)
				{
					hash[mem] = key[j][k];
					printf ("%c", 'a' + mem);
					mem ++;
				}
				if (k == w - 1)
					printf ("\n");
				else
					printf (" ");
			}
	}
	return 0;
}
