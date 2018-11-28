#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <stdio.h>
#include <algorithm>
using namespace std;

const int N = 2002;
int a[N], c[N], n;
double cnt;

void MergeSort(int l, int r)
{
	int mid, i, j, tmp;
	if (r > l + 1 )
	{
		mid = (l + r) / 2;
		MergeSort(l, mid);
		MergeSort(mid, r);
		tmp = l;
		for (i = l, j = mid; i < mid && j < r; )
		{
			if (a[i] > a[j] )
			{
				c[tmp++] = a[j++];
				cnt += mid - i; 
			}
			else c[tmp++] = a[i++];
		}
		if (j < r)
			for (; j < r; ++j )c[tmp++] = a[j];
		else
			for (; i < mid; ++i )c[tmp++] = a[i];
		for (i = l; i < r; ++i )a[i] = c[i];
	}
}
int main()
{
	ofstream cout("b.out");
	ifstream cin("D-large.in");

	int tot, count = 1, b[N];
	cin>>tot;

	while (tot--)
	{
		cin>>n;
		int sum = 0;
		for (int i = 0; i < n; i++)
		{
			cin>>a[i];
			b[i] = a[i];
		}
		sort(b, b + n);
		for (int i = 0; i < n; i++)
			if (b[i] != a[i])sum++;
		//cnt = 0;
		//MergeSort(0, n);
		cout<<"Case #"<<count++<<": ";
		cout.setf(ios::fixed);
		cout<<setprecision(6)<<double(sum)<<endl;
	}
	cin.close();
	cout.close();
	return 0;
}


