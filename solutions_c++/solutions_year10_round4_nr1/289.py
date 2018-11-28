// Using libUtil from libGlov (Game Library of Victory) available at http://bigscreensmallgames.com/libGlov
// Some solutions using BigInteger from http://mattmccutchen.net/bigint/
#include "bigint/BigIntegerAlgorithms.hh"
#include "bigint/BigIntegerUtils.hh"
#include "utilUtils.h"
#include "utilFile.h"
#include "utilString.h"
#include "assert.h"
#include "utilArray.h"
#include <string.h>
#include <stdio.h>
#include <stdarg.h>
#include <conio.h>
#include "utilRand.h"
#include "utilHashTable2.h"
#include <vector>
#include <algorithm>
#include <set>
#include <map>
using namespace std;
#pragma warning(disable:4018)

int width(int k, int i)
{
	if (i<k)
		return i+1;
	return k - (i-k)-1;
}

int dsize(int k)
{
	int r=0;
	for (int i=0; i<2*k-1; i++)
	{
		r+=width(k, i);
	}
	return r;
}

class Diamond
{
public:
	Diamond(int _k) {
		memset(this, 0, sizeof(*this));
		k = _k;
	}
	bool insert(Diamond &d, int x, int y)
	{
		int x0=x;
		for (int i=0; i<d.k*2-1; i++)
		{
			if (y+i>=k*2-1)
				return false;
			for (int j=0; j<width(d.k, i); j++)
			{
				if (x0+j >= width(k, y+i) || x0+j<0)
					return false;
				data[y+i][x0+j] = d.data[i][j];
			}
			if (i<d.k-1)
			{
				if (y+i<k-1)
				{
					x0=x0;
				} else {
					x0=x0-1;
				}
			} else {
				if (y+i<k-1)
				{
					x0=x0+1;
				} else {
					x0=x0;
				}
			}
		}
		return true;
	}
	int k;
	char data[402][202];
	bool isElegant()
	{
		for (int i=0; i<=k; i++)
		{
			int w=width(k, i);
			for (int j=0; j<=(w+1)/2; j++)
			{
				if (data[i][j] != data[i][w-j-1] && data[i][j] && data[i][w-j-1])
					return false;
			}
			for (int j=0; j<w; j++)
			{
				if (data[i][j] != data[2*k-i-2][j] && data[i][j] && data[2*k-i-2][j])
					return false;
			}
		}
		for (int i=k+1; i<2*k-1; i++)
		{
			int w=width(k, i);
			for (int j=0; j<=(w+1)/2; j++)
			{
				if (data[i][j] != data[i][w-j-1] && data[i][j] && data[i][w-j-1])
					return false;
			}
		}
		return true;
	}
	void print()
	{
		for (int i=0; i<2*k-1; i++)
		{
			for (int j=0; j<k - width(k,i); j++)
			{
				printf(" ");
			}
			for (int j=0; j<width(k, i); j++)
			{
				printf("%c ", data[i][j]?data[i][j]:'?');
			}
			printf("\n");
		}
		printf("\n");
	}
};
char *doA(char **&toks)
{
	int k = atoi(*toks++);
	Diamond base(k);
	for (int i=0; i<2*k-1; i++)
	{
		for (int j=0; j<width(k, i); j++)
		{
			base.data[i][j] = (*toks++)[0];
		}
	}

	int ret=-1;
	for (int r=k; ret==-1; r++)
	{
		for (int i=0; i<r*2-1; i++)
		{
			for (int j=0; j<r*2-1; j++)
			{
				Diamond b(r);
				if (b.insert(base, i, j))
				{
					//b.print();
					if (b.isElegant())
					{
						//b.print();
						if (ret==-1)
							ret = dsize(r) - dsize(k);
					}
				}
			}
		}
	}

	static char buf[16384];
	sprintf(buf, "%d", ret);
	return buf;
}
