// SnapperChain.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define SMALL
//#define LARGE
struct TSnapper {
	bool bPower;
	bool bOn;
};

TSnapper arrSnappers[31];

int _tmain(int argc, _TCHAR* argv[])
{
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		int N,K;
		cin >> N >> K;
		printf("Case #%d: ", i);

		//reset the array
		arrSnappers[0].bPower = true;
		arrSnappers[0].bOn = true;
		for (int n=1; n<=N; n++)
		{
			arrSnappers[n].bOn = false;
			arrSnappers[n].bPower = false;
		}

		for (int k=0; k<K; k++)
		{
			for (int n=1; n<=N; n++)
			{
				if (arrSnappers[n-1].bOn && arrSnappers[n-1].bPower)
					arrSnappers[n].bPower = true;
				else
					arrSnappers[n].bPower = false;
			}

			for (int n=1; n<=N; n++)
			{
				if (arrSnappers[n].bPower)
					arrSnappers[n].bOn = !arrSnappers[n].bOn;
				else
					break;
			}
		}

		for (int n=1; n<=N; n++)
		{
			if (arrSnappers[n-1].bOn && arrSnappers[n-1].bPower)
				arrSnappers[n].bPower = true;
			else
				arrSnappers[n].bPower = false;
		}
		if (arrSnappers[N].bPower && arrSnappers[N].bOn)
			cout << "ON" << endl;
		else
			cout << "OFF" << endl;
	}
	return 0;
}

