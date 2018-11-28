#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
using namespace std;

int cnt;

void changNum(int start, int end)
{
	int num = start, pre = num % 10;
	string strNum;
	bool flag = true;
	while(num)
	{
		int temp = num % 10;
		if(pre != temp)
			flag = false;
		strNum = (char)(temp + '0') + strNum;
		num /= 10;
	}
	if(flag)
		return ;
	string aftNum;
	for(int i = 1; i < strNum.size(); i++)
	{
		if(strNum[i] == '0') 
			continue;
		aftNum = strNum.substr(i, strNum.size() - i) + strNum.substr(0, i);
		int temp = atoi(aftNum.c_str());

		if(temp > start && temp <= end)
		{
			//cout << start << " " << temp << endl;
			cnt++;
		}
	}
}

int main(void)
{
	ifstream fin("C-small-attempt0.in");
	ofstream fout("C-small-attempt0.out");
	int cas, cas_c = 1;
	fin >> cas;
	while(cas--)
	{
		cnt = 0;
		int beg, end;
		fin >> beg >> end;
		for(int i = beg; i <= end; i++)
		{
			changNum(i, end);
		}
		fout << "Case #" << cas_c++ << ": ";
		fout << cnt << endl;
	}
	return 0;
}