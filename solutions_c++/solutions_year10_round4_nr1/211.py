#include <cassert>
#include <cmath>
#include <cstdio>
#include <set>
#include <string>
#include <vector>
#include <time.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#pragma comment(linker, "/STACK:10000000")
using namespace std;

int arr[200][200];
int temp[200][200];
int k;
const int inf = 1000000000;

bool isValid(int i, int j)
{
	return (i >= 0 && i < k && j >= 0 && j < k);
}

bool check(int ds, int di)
{
	for (int i=0;i<k;i++)
		for (int j=0;j<k;j++)
		{
			if (isValid(j-di, i+di))
				if (arr[i][j] != arr[j-di][i+di])
					return false;
			if (isValid(k+ds-1-j-di, k+ds-1-(i+di)))
				if (arr[i][j] != arr[k+ds-1-j-di][k+ds-1-(i+di)])
					return false;
		}
	return true;
}

int getRect()
{
	for (int ds = 0;ds <= 2*k+1;ds++)
	{
		for (int dx = 0;dx <= ds; dx++)
			if (check(ds,dx))
				return (k+ds)*(k+ds) - k * k;
	}
	throw 0;
}
void rot90()
{
	memcpy(temp, arr, sizeof(arr));
	for (int i=0;i<k;i++)
		for (int j=0;j<k;j++)
		{
			arr[i][j] = temp[(k-1)-j][i];
		}
}


int main()
{ 
/*	time_t ct = time(0);
	int dt =20*60 + 0*1800 +10*3600;//5*3600 + 1800;
	while (time(0) - ct < dt)
	{
		cout<<(dt + ct - time(0))<<' ';
	}
	for (;;)
	{
		cout<<char(7);
	}
	return 0;*/

	ifstream cin("input.txt");
	ofstream cout("output.txt");

	int tn;
	cin>>tn;
	for (int aaa=0;aaa<tn;aaa++)
	{
		cin>>k;
		memset(arr,-1,sizeof(arr));
		for (int i=0;i<k;i++)
			for (int j=0;j<=i;j++)
				cin>>arr[i-j][j];

		for (int i=k;i<k+k-1;i++)
			for (int j=0;j<k+k-i-1;j++)
				cin>>arr[k-j-1][i-k+j+1];

		int ans = inf;
		ans = min(ans, getRect());
		rot90();
		ans = min(ans, getRect());
		rot90();
		ans = min(ans, getRect());
		rot90();
		ans = min(ans, getRect());
		rot90();


		cout<<"Case #"<<aaa+1<<": "<<ans<<endl;
	}

	return 0;
}