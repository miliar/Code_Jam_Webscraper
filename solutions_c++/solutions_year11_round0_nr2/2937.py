// task1_Magicka.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

int check_diff(char*arr, int arr1[26][26], int *arr2, int cur_p)
{
	if (cur_p  <= 1) 
		return cur_p;
	if (arr1[arr[cur_p - 2] - 'A'][arr[cur_p - 1] - 'A'] == -1) 
		return cur_p;
	else {
		arr[cur_p - 2] = arr1[arr[cur_p - 2] - 'A'][arr[cur_p - 1] - 'A'] + 'A';
		cur_p = check_diff(arr, arr1, arr2, cur_p - 1);
		return cur_p;
	}
}
  
int _tmain(int argc, _TCHAR* argv[])
{
	fstream file_in("B-large.in", ios::in);//("B-small-attempt0", ios::in);
	fstream file_out("out.txt", ios::out);
	int T;
	file_in >> T;
	int arr1[26][26], arr2[26][26];
	for (int i = 0; i < T; ++i) {
		memset(arr1, -1, sizeof(int) * 26 * 26);
		memset(arr2, -1, sizeof(int) * 26 * 26);
		int C;
		file_in >> C;
		char letter1, letter2, letter3;
		for (int j = 0; j < C; ++j) {
			file_in >> letter1 >> letter2 >> letter3;
			arr1[letter1 - 'A'][letter2 - 'A'] = letter3  - 'A';
			arr1[letter2 - 'A'][letter1 - 'A'] = letter3  - 'A';
		}
		int D;
		file_in >> D;
		for (int j = 0; j < D; ++j) {
			file_in >> letter1 >> letter2;
			arr2[letter1 - 'A'][letter2 - 'A'] = arr2[letter2 - 'A'][letter1 - 'A'] = 0;
		}
		int N;
		file_in >> N;
		char *cur_res = new char[N];
		char symb;
		int curr_pointer = 0;
		for (int j = 0; j < N; ++j) {
			file_in >> symb;
			cur_res[curr_pointer] = symb;

			curr_pointer++;
			curr_pointer = check_diff(cur_res, arr1, NULL, curr_pointer);
			for (int k1 = 0; k1 < curr_pointer - 1; ++k1) {
				for (int k2 = k1 + 1; k2 < curr_pointer; ++k2) {
					if (arr2[cur_res[k1] - 'A'][cur_res[k2] - 'A'] == 0)
						curr_pointer = 0;
				}
			}
		}
		file_out << "Case #" << i + 1 << ": [";
		for (int j = 0; j < curr_pointer; ++j) {
			file_out << cur_res[j];
			if (j != curr_pointer - 1) {
				file_out << ", ";
			}
		}
		delete[] cur_res;
		file_out << "]" << endl;
	}
	file_in.close();
	file_out.close();
	return 0;
}

