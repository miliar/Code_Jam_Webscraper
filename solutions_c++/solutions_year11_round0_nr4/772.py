// g_1.cpp : Defines the entry point for the console application.
//
#include <stdio.h>
#include <tchar.h>

#include <fstream>
#include <vector>
#include <list>
#include <iostream>
#include <assert.h>
#include <algorithm>
#include <sstream>
#include <string>


/*
MSVS 2008

The program must be run with:
first argument = text file with input data
second argument = file name to write output data
*/
void quickSort(int arr[], int left, int right, int & ns) {

	int i = left, j = right;

	int tmp;

	int pivot = arr[(left + right) / 2];



	/* partition */

	while (i <= j) {

		while (arr[i] < pivot)

			i++;

		while (arr[j] > pivot)

			j--;

		if (i <= j) {

			if(i != j)
			{
				tmp = arr[i];

				arr[i] = arr[j];

				arr[j] = tmp;
				ns ++;
			}

			i++;

			j--;

		}

	};



	/* recursion */

	if (left < j)

		quickSort(arr, left, j, ns);

	if (i < right)

		quickSort(arr, i, right, ns);

}
int _tmain(int argc, _TCHAR* argv[])
{
	////////////////////////////////////
	const TCHAR * cfin = NULL;
	const TCHAR * cfout = NULL;

	if(argc < 3)
	{
		cfin = _T("test.txt");
		cfout = _T("test2.out");
	}
	else
	{
		cfin = argv[1];
		cfout = argv[2];
	}

	std::fstream f;
	f.open(cfin);

	std::fstream f2;
	f2.open(cfout, std::fstream::out);

	int tasks;
	f >> tasks;

	for(int t = 0; t < tasks; t++)
	{
		int n;
		f >> n;
		int * arr = new int[n];
		int ninpl = 0;
		for(int i = 0; i < n; i++)
		{
			f >> arr[i];
			if(arr[i] != i+1)
			{
				ninpl ++;
			}
		}
		//quickSort(arr, 0, n-1, nswaps);

		/*int nswaps = 0;
		for(int j1 = 0; j1 < n; j1++)
		{
			int m = arr[j1];
			int jj2 = j1;
			for(int j2 = j1+1; j2 < n; j2++)
			{
				if(arr[j2] < m)
				{
					jj2 = j2;
					m = arr[j2];
				}
			}
			if(jj2 != j1)
			{
				nswaps ++;
				std::swap(arr[j1], arr[jj2]);
			}
		}*/

		delete arr;

		f2 << "Case #" << t+1 << ": " << ninpl << ".000000" << std::endl;
	}

	return 0;
}

