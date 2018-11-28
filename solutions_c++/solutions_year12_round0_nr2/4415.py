#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <deque>
#include <map>
#include <math.h>
#include <cstdio>
#include <iomanip>

using namespace std;

int main ()
{
	freopen ("B-large.in", "r", stdin);
	freopen ("output.txt", "w", stdout);
	
	int T;
	cin>>T;

	int N, S, p;

	for (int i=1; i<=T; i++)
	{
		cin>>N;
		cin>>S;
		cin>>p;
		int ok = 0;
		int su = 0;
		int* mas = new int[N];
		for (int j=0; j<N; j++)
		{
			cin>>mas[j];
		}
		for (int k=0; k<N; k++)
		{
			if (mas[k]>=(3*p-2))
				ok++;
			else
				if (mas[k]!=0 && (mas[k]==(3*p-3) || mas[k]==(3*p-4)))
					su++;
		}
		int max = 0;
		max+=ok;
		if (su<=S)
			max+=su;
		else
			max+=S;
		cout<<"Case #"<<i<<": "<<max<<endl;
	}

	return 0;
}