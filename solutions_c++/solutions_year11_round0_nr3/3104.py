// task1_candy_splitting.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;
int count_sum(int k1, int k2) 
{
	int res = 0;
	int n = 1;
	while (1) {
		if (k1 % 2 && k2 % 2) {
		} else if (k1 % 2 || k2 % 2) {
			res += n;
		}
		k1 /= 2;
		k2 /= 2;
		n *= 2;
		if (k1 == 0 && k2 == 0)
			break;
	}
	return res;
}
int compare (const void * a, const void * b)
{
  return -( *(int*)a - *(int*)b );
}
void set(int *res, int begin, int N) 
{
	for (int i = 0; i < N; ++i) {
		if (begin % 2) {
			res[N - i - 1] = 1;
		} else {
			res[N - i - 1] = 0;
		}
		begin /= 2;
	}
}
int beg_rec(int* arr, int**arr2, int N, int pow_2) 
{
	int begin = 1;
	int end = pow((double)2, N) - 2;
	
	int * curr_res = new int[N];
	int res = -1;
	for (int i = begin; i <= end; ++i) {
		set(curr_res, i, N);
		int first_sum = 0, first_true = 0;
		int second_sum = 0, second_true = 0;
		for (int j = 0; j < N; ++j) {
			if (curr_res[j]) {
				second_true += arr[j];
				second_sum = count_sum(second_sum, arr[j]);
			} else {
				first_true += arr[j];
				first_sum = count_sum(first_sum, arr[j]);
			}
		}
		if (second_sum == first_sum) {
			res = max(res, first_true);
			res = max(res, second_true);
		}
	}
	return res;
}
int _tmain(int argc, _TCHAR* argv[])
{
	cout << count_sum(5,4) << endl << count_sum(7,9) << endl << count_sum(10, 50) << endl;
	fstream file_in("C-small-attempt1.in", ios::in);
	fstream file_out("out.txt", ios::out);
	int T;
	file_in >> T;
	int *arr;
	for (int i = 0; i < T; ++i) {
		int N;
		file_in >> N;
		arr = new int[N];
		for (int j = 0; j < N; ++j) {
			file_in >> arr[j];
		}
		qsort(arr, N, sizeof(int), compare);
		int pow_2 = 0;
		int cur_numb = 1;
		while (cur_numb <= arr[0]) {
			cur_numb *= 2;
			++pow_2;
		}
		int **arr2 = new int*[N];
		for (int j = 0; j < N; ++j) {
			arr2[j] = new int[pow_2];
			memset(arr2[j], 0, pow_2 * sizeof(int));
		}
		for (int j = 0; j < N; ++j) {
			int numb = arr[j];
			for (int k = 0; k < pow_2; ++k) {
				arr2[j][pow_2 - k - 1] = numb % 2;
				numb /= 2;
			}
		}
		for (int j = 0; j < N; ++j) {
			for (int k = 0; k < pow_2; ++k) {
				cout << arr2[j][k] << " ";
			}
			cout << endl;
		}
		int res = beg_rec(arr, arr2, N, pow_2);
		file_out << "Case #" << i + 1<< ": ";
		if (res == -1) {
			file_out << "NO" << endl;
		} else {
			file_out << res << endl;
		}
		//delete[] arr;
	}
	file_in.close();
	file_out.close();
	return 0;
}

