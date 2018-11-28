// Stanford Algo.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <utility>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

#define REP(i,n) for((i)=0;(i)<(int)(n);(i)++)
#define foreach(c,itr) for(__typeof((c).begin()) itr = (c).begin(); itr != (c).end(); itr++)

const double    eps = 1e-8;
int dblcmp (double d) {if (fabs(d) < eps) return 0; return d > eps ? 1 : -1;}

const double    PI  = 3.1415926535897932384626433832795;
const double    pi  = acos(-1.0);

typedef long long i64;
typedef unsigned long long u64;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

const int N = 10000;
int arr[N] = {0};

int test_arr[2] = {2,1};

void swap(int array[], int i, int j)
{
	int sw		= array[i];
	array[i]	= array[j];
	array[j]	= sw;
}

int qsort (int array[], int begin, int end, int flag)
{
	if (end - begin < 1)
	{
		return 0;
	}

	if (flag == 2)
	{
		swap(array, begin, end);
	} 
	else if (flag == 3)
	{
		int mid = (end - begin) / 2 + begin;
//		cout<<begin<<"  "<<mid<<"  "<<end<<endl;
//		cout<<array[begin]<<"  "<<array[mid]<<"  "<<array[end]<<endl;
		if ((array[begin] < array[mid] && array[mid] < array[end]) || (array[begin] > array[mid] && array[mid] > array[end]))
		{
			swap(array, begin, mid);
//			cout<<array[begin]<<"  "<<array[mid]<<"  "<<array[end]<<endl;
		} 
		else if ((array[begin] < array[end] && array[end] < array[mid]) || (array[begin] > array[end] && array[end] > array[mid]))
		{
			swap(array, begin, end);
//			cout<<array[begin]<<"  "<<array[mid]<<"  "<<array[end]<<endl;
		}
	}

	int pivot	= array[begin];
	int i		= begin + 1;
	for (int j = begin + 1; j <= end; j++)
	{
		if (array[j] < pivot)
		{
			swap(array, i, j);
			i++;
		}
	}
	swap(array, begin, i - 1);

	int count = end - begin;
	count += qsort (array, begin, i - 2, flag);
	count += qsort (array, i, end, flag);

	return count;
}

void first_week ()
{
	i64 count	= 0;
	int n		= 100000;
	int arr[100000] = {0};

	ifstream	fcin ("IntegerArray.txt");
	for (int i = 0; i < n; i++)
	{
		int t;
		fcin>>t;
		arr[i] = t;
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = i + 1; j < n; j++)
		{
			if (arr[j] < arr[i])
			{
				int t	= arr[i];
				arr[i]	= arr[j];
				arr[j]	= t;
				count++;
			}
		}
	}
	cout<<count;
}

bool isSorted(int array[], int size)
{
	bool res = true;
	for (int i = 1; i < size; i++)
	{
		if (array[i] < array[i - 1])
		{
			cout<<"i = "<<i<<endl;
			cout<<array[i-1]<<"  "<<array[i]<<'\n';
			res = false;
		}
	}
	return res;
}

int findBest (int n, bool isStrange = false)
{
	int m	= n / 3;
	int	r	= n % 3;
	if (!isStrange)
	{
		if (r != 0)
		{
			m++;
		}
	}
	else
	{
		if (r == 0 || r == 1)
		{
			m++;
		}
		else
		{
			m += 2;
		}
	}

	return m;
}

int pow (int a, int b)
{
	int res = 1;
	while (b > 0)
	{
		res *= 10;
		b--;
	}

	return res;
}

int rec[2000001] = {0};

bool areRecycled (int a, int b, int n)
{
	if (n <= 1)
	{
		return false;
	}

	int p = pow (10, n - 1);
	for (int i = 1; i < n; i++)
	{
		int d = a % 10;
		a /= 10;
		a += d * p;

		if (a == b)
			return true;
	}

	return false;
}

i64 countRecycled (int a, int b, int n)
{
	i64 count = 0;
	if (n <= 1)
	{
		return count;
	}

	if (rec[a] != 1)
	{
		rec[a] = 1;
	}
	else
	{
		return count;
	}

	int p = pow (10, n - 1);
	int a2 = a;
	for (int i = 1; i < n; i++)
	{
		int d = a2 % 10;
		a2 /= 10;
		a2 += d * p;

		if (a2 == a)
		{
			break;
		}

		if (a2 <= b && a2 > a)
		{
			rec[a2] = 1;
			count++;
		}
	}

	return count;
}

int calcSize (int num)
{
	int sz = 0;
	while (num > 0)
	{
		sz++;
		num /= 10;
	}

	return sz;
}

int main (int argc, char* argv[])
{
#if 1
//	ifstream	fcin ("C-small-test.txt");
//	ofstream	fcout("C-test.txt");

	ifstream	fcin ("C-large.in");
	ofstream	fcout("C-large.out");

	int T;
	fcin>>T;

	for (int i = 1; i <= T; i++)
	{
		int A, B;
		i64 count = 0;
		fcin>>A>>B;
		int n = calcSize (A);

		for (int j = A; j < B; j++)
		{

			i64 cr = countRecycled (j, B, n);
			if (cr >= 2)
			{
				cr *= (cr + 1);
				cr /= 2;
			}
			count += cr;
#if 0
			for (int k = j + 1; k <= B; k++)
			{
				if (areRecycled(j, k, n))
					count2++;
			}
#endif
		}

		for (int k = 0; k < 2000001; k++)
		{
			rec[k] = 0;
		}

//		cout<<"Case #"<<i<<": "<<count<<endl;
		fcout<<"Case #"<<i<<": "<<count<<endl;
	}
#endif

#if 0
	ifstream	fcin ("B-large.in");
	ofstream	fcout("B-large.out");

	int T;
	fcin>>T;

	for (int i = 1; i <= T; i++)
	{
		int N, S, p;
		fcin>>N>>S>>p;

		int count = 0;
		int St = S;
		for (int j = 0; j < N; j++)
		{
			int t;
			fcin>>t;
			int sc = findBest(t);
			if (sc >= p)
			{
				count++;
			}
			else if (St > 0 && t >= 2 && t <=28)
			{
				if (findBest(t, true) >= p)
				{
					St--;
					count++;
				}
			}
		}
//		cout<<"Case #"<<i<<": "<<count<<endl;
		fcout<<"Case #"<<i<<": "<<count<<endl;
	}
#endif

#if 0
	ifstream	fcin ("kargerAdj.txt");
	for (int i = 0; i < 40; i++)
	{
		string t;
		getline (fcin, t);
		cout<<t<<endl;
	}
#endif
#if 0
	int arr1[N] = {0};
	int arr2[N] = {0};
	int arr3[N] = {0};
	ifstream	fcin ("QuickSort.txt");
	for (int i = 0; i < N; i++)
	{
		int t;
		fcin>>t;
		arr1[i] = t;
		arr2[i] = t;
		arr3[i] = t;
	}


	int count = qsort(arr1, 0, N - 1, 1);
	if (!isSorted(arr1, N))
	{
		cout<<"Sort failed"<<endl;
	}
	else
	{
		cout<<"Is sorted"<<endl;
		cout<<count<<endl;
	}

	count = qsort(arr2, 0, N - 1, 2);
	if (!isSorted(arr2, N))
	{
		cout<<"Sort failed"<<endl;
	}
	else
	{
		cout<<"Is sorted"<<endl;
		cout<<count<<endl;
	}

	count = qsort(arr3, 0, N - 1, 3);
	if (!isSorted(arr3, N))
	{
		cout<<"Sort failed"<<endl;
	}
	else
	{
		cout<<"Is sorted"<<endl;
		cout<<count<<endl;
	}

	int t = 2;
	int count = qsort(test_arr, 0, t - 1);
	if (!isSorted(test_arr, t))
	{
		cout<<"Sort failed"<<endl;
		for (int i = 0; i < t; i++)
		{
			cout<<test_arr[i]<<"  ";
		}
	}
	else
	{
		cout<<"Is sorted"<<endl;
		cout<<count;
	}
#endif

	return 0;
}

