/*
 * main.cpp
 *
 *  Created on: 2009-9-4
 *      Author: megatang
 */

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char welcome[] = "welcome to code jam";
int len;

int calc(int pos, const char *str, int str_pos, int str_len) {
	if (pos == len)
		return 1;
	int ret = 0;
	while (str_pos + (len - pos) <= str_len) {
		while (*str != welcome[pos] && *str != '\0') {
			str++;
			str_pos++;
		}
		if (str_pos + (len - pos) > str_len)
			break;
		int cnt = 1;
		while (*(str + cnt) == welcome[pos])
			cnt++;
		str_pos += cnt;
		str += cnt;
		ret += cnt * calc(pos + 1, str, str_pos, str_len);
		str++;
		str_pos++;
	}
	return ret;
}

int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int N;
	len = strlen(welcome);
	fin >> N;
	string temp;
	getline(fin, temp);
	for (int cnt = 0; cnt < N; cnt++) {
		string str;
		getline(fin, str);
		cout << str << endl;
		int res = calc(0, str.c_str(), 0, str.length());
		fout << "Case #" << cnt + 1 << ": ";
		if (res < 10)
			fout << "000" << res << endl;
		else if (res < 100)
			fout << "00" << res << endl;
		else if (res < 1000)
			fout << "0" << res << endl;
	}
	fout.close();
	return 0;
}
