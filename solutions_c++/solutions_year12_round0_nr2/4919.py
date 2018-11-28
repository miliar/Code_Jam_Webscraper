#include <vector>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <stdio.h>
#include <tchar.h>
#include <map>
#include <math.h>
using namespace std;

#define BOOL int
#define TRUE 1
#define FALSE 0
int readi() { int a; scanf( "%d", &a ); return a; }
char sbuf[100005]; string readstr(){ scanf( "%s", sbuf ); return sbuf; }
// this is a brute-force version to verify the dp-version.

int T, S, N, P;
int Score[100];

map<int, vector<vector<int>>> good;
map<int, vector<vector<int>>> surprise;

void prepare()
{
	int i, j, k, l;

	good.clear();
	surprise.clear();
	for(i = 0; i <= 30; ++i)
	{
		for(j = 0; j <= i; j++)
		{
			for (k = j; k>=0 && k <= j + 2; k++)
			{
				l = i - j - k;

				if (l < k) continue;
				
				if (abs(j - k) >= 3 || abs(j-l) >= 3 || abs(k-l) >= 3) continue;
				if (abs(j - k) == 2 || abs(j-l) == 2 || abs(k-l) == 2) 
				{
					vector<int>m;
					m.push_back(j); m.push_back(k); m.push_back(l);
					if (surprise.count(i) == 0)
					{
						vector<vector<int>> n;
						n.push_back(m);
						surprise[i] = n;
					}
					else
					{
						surprise[i].push_back(m);
					}
					continue;
				}
				else
				{
					vector<int>m;
					m.push_back(j); m.push_back(k); m.push_back(l);
					if (good.count(i) == 0)
					{
						vector<vector<int>> n;
						n.push_back(m);
						good[i] = n;
					}
					else
					{
						good[i].push_back(m);
					}
					continue;
				}

			}
		}
	}
}

int intcmpA(const void *v1, const void *v2)
{
    return (*(int *)v2 - *(int *)v1);
}


int intcmpB(const void *v1, const void *v2)
{
    return (*(int *)v1 - *(int *)v2);   //from small to big
}

int Solve()
{
	vector<vector<int>>::iterator itA;
	vector<int>::iterator itB;

	int i;
	int Total  = 0;

	qsort(Score, N, sizeof(int), intcmpA);

	int BS = S;
	for (i = 0; i < N; ++i)
	{
		{
     		int flag = FALSE;
			// use good first;
			vector<vector<int>> A = good[Score[i]];
			for (itA = A.begin(); itA != A.end(); ++itA)
			{
				vector<int> B = *itA;
				for(itB = B.begin(); itB != B.end(); ++itB)
				{
					if (*itB >= P) 
					{
						Total++;
						flag = TRUE;
						break;
					}
				}
			}
         	if (flag) continue;  //succeed to use good
		}

		// use surprise.
		if (BS > 0)
		{
			vector<vector<int>> A = surprise[Score[i]];
			for (itA = A.begin(); itA != A.end(); ++itA)
			{
				vector<int> B = *itA;
				int flag = FALSE;
				for(itB = B.begin(); itB != B.end(); ++itB)
				{
					if (*itB >= P) 
					{
						Total++;
   			            BS--;
						flag = TRUE;
						break;
					}
				}
				if (flag) break;
			}
			continue;
		}
	}

	if (BS == 0) return Total;
	
	Total = 0;
	qsort(Score, N, sizeof(int), intcmpB);
	BS = S;
	for (i = 0; i < N; ++i)
	{
		// use surprise.
		if (BS > 0)
		{
			if (surprise.count(Score[i]) > 0)
			{
	   			BS--;
			}
			vector<vector<int>> A = surprise[Score[i]];
			for (itA = A.begin(); itA != A.end(); ++itA)
			{
				vector<int> B = *itA;
				int flag = FALSE;
				for(itB = B.begin(); itB != B.end(); ++itB)
				{
					if (*itB >= P) 
					{
						Total++;
						flag = TRUE;
						break;
					}
				}
				if (flag) break;
			}
			continue;
		}
		else 
		{
			// use good first;
			vector<vector<int>> A = good[Score[i]];
			for (itA = A.begin(); itA != A.end(); ++itA)
			{
				vector<int> B = *itA;
				int flag = FALSE;
				for(itB = B.begin(); itB != B.end(); ++itB)
				{
					if (*itB >= P) 
					{
						Total++;
						flag = TRUE;
						break;
					}
				}
				if (flag) continue;  //succeed to use good
			}
		}
	}

	if (BS>0) printf("Error");

	return Total;
}


 BOOL DEBUGIN = FALSE;
 BOOL DEBUGOUT = FALSE;
int main(int argc, char* argv[])
{

	if (!DEBUGIN) freopen("B-small-attempt4.in","rt",stdin);
	if (!DEBUGOUT) freopen("B-small-attempt4.out","wt",stdout);

	prepare();
	T = readi(); 
	for (int i = 0; i < T; i++)
	{
		memset(Score, 0, 100);
		N = readi(); S = readi(); P = readi();
		for (int j = 0; j < N; ++j)
		{
			Score[j] = readi();
		}
		
		printf("Case #%d: %d", i + 1, Solve());
		printf("\n");
	}


	return 0;
}
