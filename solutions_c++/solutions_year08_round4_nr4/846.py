#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#include <iostream>
#include <fstream>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <list>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;

int per[6][121][5];
int num[6];
int K;
string szstr;
void init()
{
	int i,j,k,l,m;
	int tag = 0;
	for (i = 1 ; i <= 2 ; i++)
	{
		for (j = 1 ; j<= 2; j++)
		{
			if (j != i)
			{
				per[2][tag][0] = i;
				per[2][tag++][1] = j;
			}
		}
	}
	num[2] = tag;
	tag = 0;
	for (i = 1 ; i <= 3 ; i++)
	{
		for (j = 1 ; j<= 3; j++)
		{
			if ( j != i)
			{
				for(k = 1 ; k <= 3 ; k++)
				{
					if (k != i && k != j)
					{
						per[3][tag][0] = i;
						per[3][tag][1] = j;
						per[3][tag++][2] = k;
					}
				}
			}
			
		}
	}
	num[3] = tag;
	tag = 0;
	for (i = 1 ; i <= 4 ; i++)
	{
		for (j = 1 ; j<= 4; j++)
		{
			if ( j != i)
			{
				for(k = 1 ; k <= 4 ; k++)
				{
					if (k != i && k != j)
					{
						for(l = 1 ; l <= 4 ; l++)
						{
							if(l != k && l != j && l!= i)
							{
								per[4][tag][0] = i;
								per[4][tag][1] = j;
								per[4][tag][2] = k;
								per[4][tag++][3] = l;
							}
						}
						
					}
				}
			}

		}
	}
	num[4] = tag;
	tag = 0;
	for (i = 1 ; i <= 5 ; i++)
	{
		for (j = 1 ; j<= 5; j++)
		{
			if ( j != i)
			{
				for(k = 1 ; k <= 5 ; k++)
				{
					if (k != i && k != j)
					{
						for(l = 1 ; l <= 5 ; l++)
						{
							if(l != k && l != j && l!= i)
							{
								for(m=1 ; m <= 5 ; m++)
								{
									if(m != i && m!= j && m!= k && m!=l)
									{
										per[5][tag][0] = i;
										per[5][tag][1] = j;
										per[5][tag][2] = k;
										per[5][tag][3] = l;
										per[5][tag++][4] = m;
									}
								}
							}
						}

					}
				}
			}

		}
	}
	num[5] = tag;
			
}

int solve()
{
	int nlen = szstr.length();

	int i,j,k;
	int res = 100000;
	int restmp;

	for (i = 0 ; i < num[K] ; i++)
	{
		string sztmp = szstr;
		for (j = 0 ; j < nlen ; j+= K)
		{
			char chtmp[5];
			for (k = 0 ; k < K ; k++)
				chtmp[k] = szstr[j+k];
			for (k = 0 ; k < K ; k++)
				sztmp[j+k] = chtmp[per[K][i][k]-1];
		}
		restmp = 1;
		char chtmp = sztmp[0];
		for (k = 1 ; k < nlen ; k++)
		{
			if (sztmp[k] != chtmp)
			{
				restmp++;
				chtmp = sztmp[k];
			}
		}
		if (restmp < res)
		{
			res = restmp;
		}
	}
	return res;
}

int main()
{

	ifstream cin("in.txt");
	ofstream cout("out.txt");
	//freopen("out.txt","w",stdout);
	int ncase,m;
	cin >> ncase;
	m = 0;
	init();
	while (ncase--)
	{
		m++;
		cin >> K >> szstr;
		cout << "Case #" << m << ": " << solve() << endl; 
		//printf("Case #%d: ",m);
	}
}
