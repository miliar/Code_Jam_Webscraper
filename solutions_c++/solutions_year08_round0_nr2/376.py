#include <stdio.h>
#include <algorithm>
#include <cstring>
#include <cassert>

using namespace std;

int N, NA, NB, T;

const int NMAX(128);

struct Timetable
{
	int dept;
	int arrt;
	int t;
}timetable[NMAX*2];

struct Train
{
	int readyt;
	int t;
}train[NMAX*2];

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &N);
	for( int nCase=1; nCase<=N; nCase++ )
	{
		scanf("%d%d%d", &T, &NA, &NB);
		int i, j;
		for( i=0; i<NA; i++ )
		{
			int h1, m1, h2, m2;
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			timetable[i].dept = h1*60+m1;
			timetable[i].arrt = h2*60+m2;
			timetable[i].t    = 0;
		}
		for( i=NA; i<NA+NB; i++ )
		{
			int h1, m1, h2, m2;
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			timetable[i].dept = h1*60+m1;
			timetable[i].arrt = h2*60+m2;
			timetable[i].t    = 1;
		}

		int tn[2] = {0, 0}, tc = 0;

		for( i=0; i<NA+NB; i++ )
		{
			int min = i;
			for( j=i+1; j<NA+NB; j++ )
			{
				if( timetable[j].dept<timetable[min].dept )
				{
					min = j;
				}
			}

			for( j=0; j<tc; j++ )
			{
				if( train[j].t==timetable[min].t && train[j].readyt<=timetable[min].dept )
				{
					train[j].t ^= 1;
					train[j].readyt = timetable[min].arrt+T;
					break;
				}
			}
			if( j==tc )
			{
				tn[timetable[min].t] ++;
				train[tc].t = timetable[min].t^1;
				train[tc].readyt = timetable[min].arrt+T;
				tc ++;
			}

			swap(timetable[i], timetable[min]);
		}

		printf("Case #%d: %d %d\n", nCase, tn[0], tn[1]);
	}
	return 0;
}
