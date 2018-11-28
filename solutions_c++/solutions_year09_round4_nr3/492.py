// ProbC.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <string>
#include <iostream>

using namespace std;
#define MYWIN
#ifdef MYWIN
#include <time.h>
inline double get_time()
{
	return (double)clock() / CLOCKS_PER_SEC;
}
#else
#include <sys/time.h>
inline double get_time()
{
	timeval tv;
	gettimeofday(&tv, 0);
	return tv.tv_sec+1e-6*tv.tv_usec;
}
#endif
int link[128][128];
vector<int> links[128];
int degree[128];
int order[128];
int labels[128];
int maxC;
int failed;
int n;
double dstart;

void labelgreedy(int node)
{
	for (int c=1;c<=maxC;c++)
	{
		bool colOk = true;
		for (int j=0;j<links[node].size();j++)
		{
			if (labels[links[node][j]]==c)
			{
				colOk = false;
				break;
			}
		}
		if (colOk)
		{
			labels[node] = c;
			return;
		}
	}
	maxC++;
	labels[node] = maxC;
}
int numc;
void labelRec(int node)
{
// 	if (node==n)
// 	{
// 		failed=0;
// 		return;
// 	}
	double d2 = get_time();
	if (d2-dstart>5) failed = 2;
	if (failed==0) return;
	if (failed==2) return;
	for (int c=1;c<=maxC;c++)
	{
		bool colOk = true;
		for (int j=0;j<links[node].size();j++)
		{
			if (labels[links[node][j]]==c)
			{
				colOk = false;
				break;
			}
		}
		if (colOk)
		{
			labels[node] = c;
			//labelRec(node+1);
// 			int tel = -1;
// 			int teli = -1;
// 			for (int j=0;j<links[node].size();j++)
// 			{
// 				if (labels[links[node][j]]==0 && degree[links[node][j]]>tel)
// 				{
// 					tel = degree[links[node][j]];
// 					teli = links[node][j];
// 				}
// 			}
// 			if (tel!=-1)
// 			{
// 				labelRec(teli);
// 			}
// 			else
// 			{
				int bb = 0;
				for (int j=0;j<n;j++)
				{
					int jj = order[j];
					if (labels[jj]==0)
					{
						bb++;
						labelRec(jj);
						break;
					}
				}
				if (bb==0)
				{
					failed = 0;
				}
			//}
			labels[node] = 0;
		}
	}
}

void solve()
{
	int T;
	cin >> T;
	for (int t=0;t<T;t++)
	{
		int price[128][128];
		int k;
		cin >> n >> k;
		for (int i=0;i<n;i++)
		{
			for (int j=0;j<k;j++)
				cin >> price[i][j];
		}
		for (int i=0;i<128;i++)
			links[i].clear();
		memset(link, 0, sizeof(link));
		memset(degree, 0, sizeof(degree));
		for (int i1=0;i1<n;i1++)
			for (int i2=i1+1;i2<n;i2++)
			{
				bool bok = true;
				for (int j=0;j<k;j++)
				{
					if (price[i1][j]==price[i2][j])
					{
						bok = false;
						break;
					}
					if (j<k-1)
					{
						if (price[i1][j]>price[i2][j] && price[i1][j+1]<=price[i2][j+1])
						{
							bok = false;
							break;
						}
						if (price[i2][j]>price[i1][j] && price[i2][j+1]<=price[i1][j+1])
						{
							bok = false;
							break;
						}
					}
				}
				if (!bok)
				{
					link[i1][i2] = 1;
					link[i2][i1] = 1;
					links[i1].push_back(i2);
					links[i2].push_back(i1);
				}
			}
		for (int i=0;i<n;i++)
		{
			for (int j=0;j<n;j++)
				if (link[i][j]) degree[i]++;
			order[i] = i;
		}
		for (int i1=0;i1<n;i1++)
			for (int i2=0;i2<n-1;i2++)
				if (degree[order[i2]]<degree[order[i2+1]])
				{
					swap(order[i2], order[i2+1]);
				}
		memset(labels,0,sizeof(labels));
		maxC = 0;
		for (int i=0;i<n;i++)
		{
			int ii = order[i];
			if (labels[ii]==0)
			{
				labelgreedy(ii);
			}
		}
		dstart = get_time();
		int myMax = maxC;
		for (;;)
		{
			failed = 1;
			memset(labels,0,sizeof(labels));
			maxC = myMax-1;
			//cerr << maxC << endl;
			//labelRec(0);
 			for (int i=0;i<n;i++)
 			{
 				int ii = order[i];
 				if (labels[ii]==0)
 				{
 					labelRec(ii);
 				}
				if (failed==2) break;
 			}
			if (failed>=1) break;
			myMax--;
		}

		cout << "Case #" << (t+1) << ": " << myMax << endl;
		cerr << "Case #" << (t+1) << ": " << myMax << endl;


		
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	solve();
	return 0;
}

